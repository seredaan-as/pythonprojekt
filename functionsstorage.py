#Inputs
from storage import save_recipes
import random
from typing import List, Dict

# weitere Hilfsfunktionen


def filter_by_course():  
    pass


def create_new_recipe():  
    pass


def search_by_ingredient():  
    pass


def adjust_portions():  
    pass


def create_grocery_list():
    pass

# + Fehlerbehandlung für Files (wenn der Name nicht gefunden wird, Script Seite 15, 17, 1ß)



# ______________ ab hier fertige Funktionen ____________________________________

import json
import time
from storage import load_recipes
from typing import List, Dict 


## Übergreifend (3.1, )


def read_int(promt: str) -> int:
    """Function to cover type error if user chooses not an int where int is excpected"""
    while True:
        value = input(promt)
        try:
            return int(value)
        except ValueError:
            print("Bitte eine Zahl eingeben – die Magie erledigt den Rest.")


def select_recipe_from_list(recipes: list[dict]):
    """Shows filtered recipes with index, 
    asks user to choose a recipe,
    gives user the option to go back,
    covers an error in case no recipes are found."""

    if not recipes:
        print("Hm… die Küchenelfen haben in ihren Kesseln gerührt, aber kein Rezept ist erschienen. Versuche eine andere Zauberformel (äh… Auswahl)")
        return None
    
    print("\nDie Küchenelfen haben gerührt und folgende Rezepte gefunden:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}) {recipe['recipe_name']} ({recipe['cooking_time']} Minuten)")

    choice = read_int("Sprich eine Zahl, und das Rezept öffnet sich wie von Zauberhand. Mit 0 gelangst du zurück.: ")
    if choice == 0:
        return None
    if 1 <= choice <= len(recipes): 
        return recipes[choice - 1]                  # um an die User-Nummerierungslogik anzugleichen

    print("Die Küchenelfen schauen ratlos - diese Auswahl kennen sie nicht.")
    return None


def show_recipe_details (recipe:dict):
    """Displays full recipe details"""
    print("\n Rezeptrolle wird entrollt...\n")
    print(f"Rezept: {recipe['recipe_name']}")
    if recipe.get("hp_story"):
        print("Erstmal etwas Zauberhaftes zu diesem Rezept aus dem Magie-Universum:")
        print(f"\n{recipe['hp_story']}\n")
    print(f"Zeit: {recipe['cooking_time']} Minuten")
    print(f"Schwierigkeitsgrad: {recipe['recipe_complexity']}")
    print(f"Ernährungsform: {recipe['diet_type']}")
    print(f"Gerichtstyp: {recipe['course_type']}")
    print(f"Zeit: {recipe['cooking_time']} Minuten")
    if recipe.get("ingredients"):
        print("\n Zutaten:")
        for ing in recipe["ingredients"]:
            amount = ing.get("amount", "")
            unit = ing.get("unit", "")
            name = ing.get("ingredient", "")
            note = ing.get("note", "")
            print(f" - {amount} {unit} {name}, {note}")
    if recipe.get("steps"):
        print("\nZubereitung:")
        for step in recipe["steps"]:
            print(f" {step}")

    print("\nViel Spaß beim Kochen!")


def show_recipe_flow(recipes):
    from ui import choose_recipe_index, show_recipe_details
    idx = choose_recipe_index(recipes)
    if idx is None:
        return
    show_recipe_details(recipes[idx])


def add_recipe_flow(recipes):
    print("\n Rezept anlegen")
    from ui import input_recipe
    new_recipe = input_recipe()
    if new_recipe is None:
        return recipes

    # optional: Duplikate nach Titel verhindern/überschreiben
    for i, r in enumerate(recipes):
        if r.get("title") == new_recipe["title"]:
            choice = input("Rezept existiert schon. Überschreiben? (j/n): ").strip().lower()
            if choice in ("j", "ja", "y", "yes"):
                recipes[i] = new_recipe
                save_recipes(recipes)
                print("Rezept überschrieben & gespeichert.")
            else:
                print("Abgebrochen.")
            return recipes

    recipes.append(new_recipe)
    save_recipes(recipes)
    print("Rezept gespeichert.")
    return recipes


    #--------------- Menü als Schleife, um andere Auswahl abzufangen -----------------
    while True:
        print("\nWas möchtest du als Nächstes tun?")
        print("1) Portionen anpassen")
        print("2) Einkaufszettel erstellen")
        print("3) Zurück zum Hauptmenü")
        choice = read_int("Sprich eine Zahl: ")

        if choice == 1:
            adjust_portions()         #noch anzupassen + funk azulegen
        elif choice == 2:
            create_grocery_list()    #noch anzupassen + funk azulegen
        elif choice == 3:
            print("Hauptmenü wird geladen...")
            time.sleep(2)
            return                    # Zurück ins Hauptmenü
        else:
            print("Die Küchenelfen schauen ratlos – diese Wahl kennen sie nicht. Probier eine andere.")
            

def adjust_portions(recipe: dict, target_servings: int) -> dict:
    """Passt die Portionen eines Rezepts an und gibt ein neues Rezept-Dict zurück."""
    if not recipe or target_servings <= 0:
        return recipe
    
    original_servings = recipe.get('servings', 1)
    if original_servings <= 0:
        original_servings = 1
    
    factor = target_servings / original_servings
    
    # Neues Rezept-Dict erstellen (Kopie)
    adjusted_recipe = recipe.copy()
    adjusted_recipe['servings'] = target_servings
    
    # Zutaten anpassen
    adjusted_ingredients = []
    for ingredient in recipe.get('ingredients', []):
        adjusted_ing = ingredient.copy()
        if adjusted_ing.get('amount') is not None:
            adjusted_ing['amount'] = round(adjusted_ing['amount'] * factor, 2)
        adjusted_ingredients.append(adjusted_ing)
    
    adjusted_recipe['ingredients'] = adjusted_ingredients
    
    print(f"Rezept wurde von {original_servings} auf {target_servings} Portionen angepasst (Faktor: {factor:.2f}).")
    return adjusted_recipe           


#  1
## Spezifisch: 1.1 Filtern nach Zeit


def filter_by_time(recipes: list[dict], max_minutes: int) -> list[dict]:
    result: list[dict] = []

    for recipe in recipes: 
        if "cooking_time" in recipe:
            try:
                if int(recipe["cooking_time"]) <= max_minutes:
                    result.append(recipe)
            except ValueError:
                pass

    return result


## Spezifisch: 1.2 Filtern nach Schwierigkeit


def filter_by_complexity(recipes: list[dict], complexity: str) -> list[dict]:
    """Filtert Rezepte nach Schwierigkeitsgrad (leicht / mittel / anspruchsvoll)."""
    if not recipes or not complexity:
        return []

    complexity_lower = complexity.strip().lower()
    result: list[dict] = []

    for recipe in recipes:
        recipe_complexity = str(recipe.get("recipe_complexity", "")).strip().lower()
        if recipe_complexity == complexity_lower:
            result.append(recipe)

    return result


## Spezifisch: 1.3 Filtern nach Ernährungsform


def filter_by_diet(recipes: list[dict], diet: str) -> list[dict]:
    """Filtert Rezepte nach Ernährungsform (z.B. vegan / vegetarisch / pescetarisch / standard)."""
    if not recipes or not diet:
        return []

    diet_lower = diet.strip().lower()
    result: list[dict] = []

    for recipe in recipes:
        recipe_diet = str(recipe.get("diet_type", "")).strip().lower()
        if recipe_diet == diet_lower:
            result.append(recipe)

    return result


## Spezifisch: 1.5 Rezept zufällig auswählen


def get_random_recipe(recipes: list[dict]):
    """Gibt ein zufälliges Rezept aus der Liste zurück (oder None, wenn leer)."""
    if not recipes:
        return None
    return random.choice(recipes)


#  2
## Spezifisch 2. ....


#  3
## Spezifisch: 3.1 Filtern nach Charakter


def filter_by_character(recipes: list[dict], character: str) -> list[dict]:
    """Filtert Rezepte nach einem Harry-Potter-Charakter."""
    if not recipes or not character:
        return []

    filtered = []
    character_lower = character.lower()

    for recipe in recipes:
        characters = recipe.get('character', [])
        # Prüfen, ob der gesuchte Charakter in der Liste vorkommt (case-insensitive)
        if any(char.lower() == character_lower for char in characters):
            filtered.append(recipe)

    return filtered


