
        

# weitere Hilfsfunktionen


def filter_by_complexity():  
    pass
def filter_by_diet():  
    pass
def filter_by_course():  
    pass
def get_random_recipe():  
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


def read_int(promt: str) -> int:
    """Function to cover type error if user chooses not an int where int is excpected"""
    while True:
        value = input(promt)
        try:
            return int(value)
        except ValueError:
            print("Bitte eine Zahl eingeben – die Magie erledigt den Rest.")

def filter_by_time(recipes: list[dict], max_minutes: int) -> list[dict]:
    """Filter recipes by maximum requiered cooking time.
    Covers error if cooking_time is not in JSON by skipping the recipe"""  
    result: list[dict] = []

    for recipe in recipes: 
        if "cooking_time" in recipe:
            try:
                if int(recipe["cooking_time"]) <= max_minutes:
                    result.append(recipe)
            except ValueError:
                pass

    return result

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
        print(f"{index}) {recipe["recipe_name"]} ({recipe["cooking_time"]} Minuten)")

    choice = read_int("Sprich eine Zahl, und das Rezept öffnet sich wie von Zauberhand. Mit 0 gelangst du zurück.: ")
    if choice == 0:
        return None
    if 1 <= choice <= len(recipes): 
        return recipes[choice - 1]                  # um an die User-Nummerierungslogik anzugleichen

    print("Die Küchenelfen schauen ratlos - diese Auswahl kennen sie nicht.")
    return None


def show_recipe_details (recipe:dict):
    """Displays full recipe details"""
    print("\n📜 Rezeptrolle wird entrollt...\n")
    print(f"Rezept: {recipe["recipe_name"]}")
    if recipe.get("hp_story"):
        print("Erstmal etwas Zauberhaftes zu diesem Rezept aus dem Magie-Universum:")
        print(f"\n{recipe["hp_story"]}\n")
    print(f"Zeit: {recipe["cooking_time"]} Minuten")
    print(f"Schwierigkeitsgrad: {recipe["recipe_complexity"]}")
    print(f"Ernährungsform: {recipe["diet_type"]}")
    print(f"Gerichtstyp: {recipe["course_type"]}")
    print(f"Zeit: {recipe["cooking_time"]} Minuten")
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
            

            
