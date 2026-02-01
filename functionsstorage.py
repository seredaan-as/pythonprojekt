#Inputs
from storage import save_recipes, load_recipes
import random
from typing import List, Dict
import json
import time
import os
from datetime import datetime




# weitere Hilfsfunktionen

# + Fehlerbehandlung für Files (wenn der Name nicht gefunden wird, Script Seite 15, 17, 1ß)


# ______________ ab hier fertige Funktionen ____________________________________



## Übergreifend (3.1, 2.2, 2.3, )


def read_int(promt: str) -> int:
    """Function to cover type error if user chooses not an int where int is excpected"""
    while True:
        value = input(promt)
        try:
            return int(value)
        except ValueError:
            print("Bitte eine Zahl eingeben – die Magie erledigt den Rest.")

# Menü für die Rezeptdetailansicht separat als Schleife, um falsche Auswahl abzufangen ----
    
def mini_menu(recipe:dict):
    while True:
        print("\nWas möchtest du als Nächstes tun?")
        print("1) Portionen anpassen")
        print("2) Einkaufszettel erstellen")
        print("3) Rezept als txt.Datei speichern")
        print("4) Zurück zum Hauptmenü")
        choice = read_int("Sprich eine Zahl: ")

        if choice == 1:
            target_servings = read_int("Auf wie viele Portionen anpassen? ")
            recipe = adjust_portions(recipe, target_servings)                   #Anmerkung: Damit wird das Rezept in dieser Laufzeit überschrieben, d.h. Einkaufszettel, weitere Anpassungen basieren auf dem neuen Rezept 
            show_recipe_details(recipe)   
        elif choice == 2:
            create_grocery_list(recipe)
        elif choice == 3:
            export_recipe(recipe)
        elif choice == 4:
            print("Hauptmenü wird geladen...")
            time.sleep(1)
            return                                                              # Zurück ins Hauptmenü
        else:
            print("Die Küchenelfen schauen ratlos – diese Wahl kennen sie nicht. Probier eine andere.")


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
    print("\n -- Rezeptrolle wird entrollt... --\n")
    print("=" * 40)
    print(f"Rezept: {recipe['recipe_name']}")
    print("=" * 40)
    if recipe.get("hp_story"):
        print(f"\n<{recipe['hp_story']}>\n")
    print(f"Zeit: {recipe['cooking_time']} Minuten")
    print(f"Schwierigkeitsgrad: {recipe['recipe_complexity']}")
    print(f"Ernährungsform: {recipe['diet_type']}")
    print(f"Gerichtstyp: {recipe['course_type']}")
    print(f"Zeit: {recipe['cooking_time']} Minuten")
    print(f"Portionen: {recipe['servings']}")
    if recipe.get("ingredients"):
        print("Zutaten:")
        for ing in recipe["ingredients"]:
            amount = ing.get("amount")
            unit = ing.get("unit")
            name = ing.get("ingredient")
            note = ing.get("note")
        
            lines = []
            if amount is not None:
                lines.append(str(amount))

            if unit is not None:
                lines.append(str(unit))

            if name is not None:
                lines.append(str(name))
    
            ingredient_line = " ".join(lines).strip()

            if note is not None:
                ingredient_line += f", {note}"

            print(f"- {ingredient_line}")

    if recipe.get("steps"):
        print("\nZubereitung:")
        for step in recipe["steps"]:
            print(f" {step}")

    print("\n==Viel Spaß beim Kochen! ==\n")


def show_recipe_flow(recipes):
    # Wähle ein Rezept aus der Liste und zeige die Details an.
    selected = select_recipe_from_list(recipes)
    if selected is None:
        return
    show_recipe_details(selected)


def export_recipe(recipe: dict):
    """Speichert ein Rezept als txt-Datei, dabei ist der Dateiname = Rezeptname; gibt den Dateipfad zurück oder bei Fehler = None"""

    if not recipe:
        print("Kein Rezept vorhanden.")
        return 
    
    recipe_name = recipe.get("recipe_name", "Unbekanntes Rezept")
    hp_story = recipe.get("hp_story")

    lines = []

    lines.append("== REZEPTROLLE ==")
    lines.append(f"Rezept: {recipe_name}")
    lines.append(f"Zauberzettel erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 40)

    lines.append(f"Zeit: {recipe.get('cooking_time')} Minuten")
    lines.append(f"Schwierigkeitsgrad: {recipe.get('recipe_complexity')}")
    lines.append(f"Ernährungsform: {recipe.get('diet_type')}")
    lines.append(f"Gerichtstyp: {recipe.get('course_type')}")
    lines.append(f"Portionen: {recipe.get('servings')}")

    characters = recipe.get("character", [])
    if characters:
        lines.append("Relevante Harry Potter-Charaktere: " + ", ".join(str(c) for c in characters))
    
    lines.append("-" * 40)

    # Zutaten
    lines.append("Zutaten:")
    for ing in recipe.get("ingredients", []):
        amount = ing.get("amount")
        unit = ing.get("unit")
        name = ing.get("ingredient")
        note = ing.get("note")
    
        ingredients = []
        if amount is not None:
            ingredients.append(str(amount))
        if unit:
            ingredients.append(str(unit))
        if name:
            ingredients.append(str(name))

        ingredient_line = " ".join(ingredients).strip()

        if note:
            ingredient_line += f" ({note})"

        if ingredient_line:
            lines.append(f"- {ingredient_line}")

    # Zubereitung 
    lines.append("")
    lines.append("Zubereitung:")
    for step in recipe.get("steps", []):
        lines.append(str(step))

    lines.append("")
    lines.append("== Viel Spaß beim Kochen! ==")



    # Dateiname sichern
    safe_name = "".join(ch for ch in recipe_name if ch.isalnum() or ch in (" ", "_", "-")).strip()
    if not safe_name:
        safe_name = "Unbekanntes_Rezept"
    # Ordner
    folder = "exported_recipes"
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"{safe_name}.txt")

    with open(path, "w", encoding="utf-8") as f:                                                        # Fehlerbehandlung: Die Datei wird nach der Ausführunf im with-Block automatisch geschlossen
        f.writelines(line + "\n" for line in lines)

    print(f"\nRezept wurde gespeichert: {path}\n")
    return path

    


def create_grocery_list(recipe: dict):
    """Erstellt einen Einkaufszettel in Form einer Text-Datei für das in der Rezeptdetailansicht geöffnete Rezept; 
    gibt den Dateipfad als String zurück;
    Hilfsfuntion für mini_menu"""
    
    ingredients = recipe.get("ingredients", [])
    if not ingredients:
        print("Diese Rezeptrolle hat keine Zutaten gespeichert - kein Einkaufszettel möglich.") 
        return None
    
    recipe_name = recipe.get("recipe_name", "Unbekanntes Rezept") 

    lines = []

    lines.append("== EINKAUFSZETTEL ==")
    lines.append(f"Rezept: {recipe_name}")
    lines.append(f"Zauberzettel erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 40)

    for ing in ingredients: 
        amount = ing.get("amount")
        unit = ing.get("unit")
        name = ing.get("ingredient")
        note = ing.get("note")
        ingr_part = []

        if amount is not None:
            ingr_part.append(str(amount))

        if unit:
            ingr_part.append(str(unit))

        if name:
            ingr_part.append(str(name))
    
        ingredient_line = " ".join(ingr_part).strip()

        if note:
            ingredient_line += f" ({note})"

        if ingredient_line:
            lines.append(f"- {ingredient_line}")

    lines.append("-" * 40)
    lines.append("== Viel Spaß beim Kochen! ==")

    # Dateiname sichern
    safe_name = "".join(ch for ch in recipe_name if ch.isalnum() or ch in (" ", "_", "-")).strip()      #schaut, ob char = Buchstabe/Zahl ist, also keine Sonderzeichen und speichert Dateiname
    file_name = f"einkaufszettel_{safe_name}.txt"
    #Ordner
    folder = "grocery_lists"
    os.makedirs(folder, exist_ok=True)                                                                  #Prüfung, ib der Ordner schon existiert -> wenn ja, kein Fehler
    path = os.path.join(folder, file_name)                                                              #um verschiedene Pfadarten von Betriebsystemen darzustellen 

    with open(path, "w", encoding="utf-8") as f:                                                        # Fehlerbehandlung: Die Datei wird nach der Ausführunf im with-Block automatisch geschlossen
        f.writelines(line + "\n" for line in lines)

    print(f"\nEinkaufszettel wurde erstellt: {path}\n")
    return path

            

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
    """Filtert Rezepte nach Schwierigkeitsgrad (einfach / mittel / anspruchsvoll)."""
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


## Spezifisch: 1.4 Filtern nach Gerichsttyp


def filter_by_course(recipes: list[dict], course):  
    """Filtert Rezepte nach Gerichtstyp: Vorspeise, Hauptspeise, Nachtisch"""
    if not recipes or not course: 
        return []
    
    course_lower = course.strip().lower()
    result : list[dict] = []

    for recipe in recipes: 
        recipe_course = str(recipe.get("course_type", "")).strip().lower()
        if recipe_course == course_lower:
            result.append(recipe)
    return result
    


## Spezifisch: 1.5 Rezept zufällig auswählen


def get_random_recipe(recipes: list[dict]):
    """Gibt ein zufälliges Rezept aus der Liste zurück (oder None, wenn leer)."""
    if not recipes:
        return None
    return random.choice(recipes)


#  2
## Spezifisch 2.1


def create_new_recipe() -> dict | None:
    """Erstellt ein neues Rezept, gibt das Rezept als Dict zurück oder None bei Abbruch"""  
    
    # Must have promt
    def choice_nonempty(text: str) -> str:              
        while True: 
            value = input(text).strip()
            if value:
                return value
            print("Bitte nicht leer lassen.")

    # optionaler promt
    def choice_optional(text: str) -> str | None: 
        value = input(text).strip()
        return value if value else None
    
    # optionaler float promt
    def choice_float_optional(text:str) -> float | None:
        while True:
            value = input(text).strip() 
            if value == "":
                return None
            try:
                return float(value)
            except ValueError:
                print("Die Küchenhelfen kennen diese Zahl nicht. (Enter für 'Keine Menge')")

    #Falls Fehlerangabe
    def pick_from_menu(title: str, options: dict[int, str]) -> str:
        print(f"\n{title}")
        for k, v in options.items():
            print(f"{k}) {v}")
        while True:
            choice = read_int("Auswahl: ")
            if choice in options:
                return options[choice]
            print("Ungültige Auswahl. Bitte eine der Zahlen aus dem Menü wählen.")
        
    
    print("\n" + "=" * 40)
    print("Neues Rezept hinzufügen")
    print("\n" + "=" * 40)
    print("Rezeptname '0' = Hinzufügen abbrechen\n")

    recipe_name = input("Rezeptname: ").strip()
    if recipe_name == "0":
        print("Der Vorgang wurde abgebrochen.")
        return
    while not recipe_name:                      # Wiederholung, solane der Rezeptname leer ist
        recipe_name = input("Rezeptname: ").strip() 

    #Kochzeit
    cooking_time = read_int("Kochzeit in Minuten: ")
    while cooking_time <= 0:
        cooking_time = read_int("Bitte gültige Kochzeit eingeben (>0 Minuten): ")

    #Auswahlfelder nur mit erlaubten Optionen
    complexity_map = {1: "einfach", 2: "mittel", 3: "anspruchsvoll"}
    diet_map = {1: "vegan", 2: "vegetarisch", 3: "pescetarisch", 4: "standard"}
    course_map = {1: "vorspeise", 2: "hauptgericht", 3: "nachtisch"}


    recipe_complexity = pick_from_menu("Schwierigkeitsgrad wählen:", complexity_map)
    diet_type = pick_from_menu("Ernährungsform wählen:", diet_map)
    course_type = pick_from_menu("Gerichtstyp wählen:", course_map)

    #Portionen
    servings = read_int("Portionen: ")
    while servings <= 0: 
        servings = read_int("Bitte gültige Portionenanzahl eingeben (>0 Portionen): ")

    # HP-Charaktere ()
    hp_characters = choice_optional("Welche Harry Potter Charaktere werden mit dem Rezept assoziiert? Bitte Komma-getrennt eingeben oder Enter = für keine: ")
    character: list[str] = []
    if hp_characters:
        character_parts = [c.strip() for c in hp_characters.split(",") if c.strip()]              #erezeugt eine Liste aus c, wenn das Ergebnis nicht leer ist
        character_parts = [c for c in character_parts if c]                                                 # leere Einträge in der Liste raus
        bad = [c for c in character_parts if c.isdigit()]
        if bad:
            print("Die Küchenelfen bitten dich keine Zahlen als Charaktere einzugeben. Diese wurden ignoriert:", ", ".join(bad))
        character = [c for c in character_parts if c.isdigit]

    # Zutaten
    print("\nZutaten eingeben (Enter bei Name = fertig):")
    ingredients: list[dict] = []

    while True: 
        ing_name = input("Zutat: ").strip()
        if ing_name == "":
            break

        amount = choice_float_optional("  Menge (z.B. 1 oder 0.5): ")
        unit = choice_optional("  Einheit (g, ml, etc.): ")
        note = choice_optional("  Notiz (z.B. Prise, zum Servieren): ")

        ingredients.append({
            "ingredient": ing_name,
            "amount": amount,
            "unit": unit,
            "note": note
        })
    if not ingredients:
        print("Die Küchenelfen schauen verwirrt - ohne Zutaten gibt es kein Rezept. Abgebrochen.")
        return
    
    # Zubereitung
    print("\nZubereitungsschritte (Enter = fertig):")
    steps: list[str] = []
    step_no = 1

    while True: 
        step = input(f"{step_no}) Schritt: ").strip()
        if step == "":
            break
        steps.append(f"{step_no}) {step}")
        step_no += 1
    if not steps:
        print("Die Küchenelfen schauen verwirrt - ohne Schritte gibt es kein Rezept. Abgebrochen.")
        return 
    
    new_recipe = {
        "recipe_name": recipe_name,
        "cooking_time": cooking_time,
        "recipe_complexity": recipe_complexity,
        "diet_type": diet_type,
        "course_type": course_type,
        "character": character,
        "servings": servings,
        "ingredients": ingredients,
        "steps": steps
    }
    
    print(f"\nRezept '{recipe_name}' wurde erstellt.\n")
    return new_recipe


## Spezifisch 2.4


def search_by_ingredient(recipes: list[dict], ingredient: str) -> list[dict]:
    if not recipes or not ingredient:
        return []
    q = ingredient.strip().lower()
    out = []
    for r in recipes:
        for ing in r.get("ingredients", []):
            name = str(ing.get("name") or ing.get("ingredient") or "").lower()
            if q in name:
                out.append(r)
                break
    return out


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


