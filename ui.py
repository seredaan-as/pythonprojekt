# Vereinfachte Menüs + Anzeige Funktionen
from functionsstorage import (
    read_int, filter_by_time, filter_by_complexity,
    filter_by_diet, filter_by_course, get_random_recipe
)
from storage import load_recipes, save_recipes, create_shopping_list
from logic import adjust_portions, filter_by_character
import time

def greet_user():
    print("=== Harry Potter Kochbuch ===")
    print("Willkommen, Reisender. Du hast das Harry-Potter-Kochbuch betreten.")
    user_name = input("Wie ist dein Name, Hexe oder Zauberer?: ")
    print(f"Schön, dich kennenzulernen, {user_name}! Heute begleite ich dich durch die magische Küche.")

def find_recipe_flow():
    menu = [
        "1) Zeit – ich habe wenig Zeit",
        "2) Komplexität – leicht / mittel / anspruchsvoll",
        "3) Ernährungsform – vegan / vegetarisch / pescetarisch / standard",
        "4) Gerichtstyp (Vorspeise/Hauptspeise/Nachspeise)",
        "5) Zufallsrezept",
        "6) Zurück zum Hauptmenü"
    ]
    print("Dieses Harry-Potter-Kochbuch ist ein interaktives Abenteuer, und ich begleite dich auf deiner kulinarischen Reise.")
    print("Was ist dir heute wichtig: Zeit, Schwierigkeit, Ernährungsweise oder bist du noch unentschlossen?")
    print('\n'.join(menu))
    choice = read_int("Wähle eine Option aus: ")

    actions = {
        1: filter_by_time,
        2: filter_by_complexity,
        3: filter_by_diet,
        4: filter_by_course,
        5: get_random_recipe,
        6: lambda: (print("Hauptmenü wird geladen..."), time.sleep(2), show_main_menu())
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Die Küchenelfen schauen ratlos – diese Wahl kennen sie nicht. Probier eine andere.")

def show_recipe_detail_flow(recipe: dict) -> None:
    """Zeigt die Details eines Rezepts an und bietet Optionen."""
    if not recipe:
        print("Kein Rezept zum Anzeigen vorhanden.")
        return

    print("\n" + "=" * 60)
    print(f" {recipe.get('recipe_name', 'Unbekanntes Rezept')}\n" + "=" * 60)
    if recipe.get('hp_story'):
        print(f"\n{recipe['hp_story']}\n")
    print(f" Zubereitungszeit: {recipe.get('cooking_time', '?')} Minuten")
    print(f" Schwierigkeit: {recipe.get('recipe_complexity', '?')}")
    print(f" Ernährungsform: {recipe.get('diet_type', '?')}")
    print(f" Gerichtstyp: {recipe.get('course_type', '?')}")
    print(f" Portionen: {recipe.get('servings', '?')}")
    characters = recipe.get('character', [])
    if characters:
        print(f" Charaktere: {', '.join(characters)}")
    print("\n Zutaten:\n" + "-" * 60)
    for ingredient in recipe.get('ingredients', []):
        line = f"  • {ingredient.get('ingredient', '?')}"
        if ingredient.get('amount') is not None:
            line += f": {ingredient['amount']}"
            if ingredient.get('unit'):
                line += f" {ingredient['unit']}"
        if ingredient.get('note'):
            line += f" ({ingredient['note']})"
        print(line)
    print("\n Zubereitung:\n" + "-" * 60)
    for step in recipe.get('steps', []):
        print(f"  {step}")
    print("\n" + "=" * 60)

    # Menü für weitere Aktionen
    menu = [
        "1) Portionen anpassen",
        "2) Einkaufszettel erstellen",
        "3) Zurück"
    ]
    while True:
        print("\nWas möchtest du mit diesem Rezept tun?")
        print('\n'.join(menu))
        choice = read_int("Auswahl: ")

        if choice == 1:
            target_servings = read_int("Für wie viele Portionen möchtest du kochen? ")
            show_recipe_detail_flow(adjust_portions(recipe, target_servings))
            break
        elif choice == 2:
            create_shopping_list(recipe)
        elif choice == 3:
            break
        else:
            print("Die Küchenelfen kennen diese Zahl nicht. Probier es mit 1, 2 oder 3.")

def select_recipe_from_list(recipes: list[dict]) -> dict:
    """Zeigt eine Liste von Rezepten und lässt den User eines auswählen."""
    if not recipes:
        print("Keine Rezepte gefunden.")
        return None

    print("\n" + "=" * 60)
    print("Gefundene Rezepte:\n" + "=" * 60)
    for i, recipe in enumerate(recipes, 1):
        name = recipe.get('recipe_name', 'Unbekanntes Rezept')
        t = recipe.get('cooking_time', '?')
        complexity = recipe.get('recipe_complexity', '?')
        print(f"{i}) {name} ({t} Min, {complexity})")
    print("0) Zurück")

    choice = read_int("\nWähle ein Rezept aus (Nummer): ")
    if choice == 0:
        return None
    if 1 <= choice <= len(recipes):
        return recipes[choice - 1]
    print("Ungültige Auswahl.")
    return None

def handle_character_flow(recipes: list[dict]) -> None:
    """Flow B: Rezepte nach Harry-Potter-Charakteren durchsuchen."""
    print("\n" + "=" * 60)
    print("Rezepte nach Harry-Potter-Charakteren entdecken")
    print("=" * 60)

    # Charaktere aus allen Rezepten sammeln
    all_characters = sorted({char for recipe in recipes for char in recipe.get('character', [])})
    if not all_characters:
        print("Keine Charaktere in den Rezepten gefunden.")
        return

    print("\nVerfügbare Charaktere:")
    for i, char in enumerate(all_characters, 1):
        print(f"{i}) {char}")
    print("0) Zurück")

    choice = read_int("\nWähle einen Charakter: ")
    if choice == 0:
        return
    if 1 <= choice <= len(all_characters):
        selected_character = all_characters[choice - 1]
        filtered = filter_by_character(recipes, selected_character)
        if filtered:
            print(f"\nRezepte für {selected_character}:")
            selected_recipe = select_recipe_from_list(filtered)
            if selected_recipe:
                show_recipe_detail_flow(selected_recipe)
        else:
            print(f"Keine Rezepte für {selected_character} gefunden.")
    else:
        print("Ungültige Auswahl.")

def handle_manage_recipes_flow(recipes: list[dict]) -> list[dict]:
    """Flow C: Rezepte verwalten (hinzufügen, anzeigen, speichern, laden)."""
    print("\n" + "=" * 60)
    print("Rezepte verwalten")
    print("=" * 60)

    while True:
        print(
            "\nWas möchtest du tun?\n"
            "1) Neues Rezept hinzufügen\n"
            "2) Alle Rezepte anzeigen\n"
            "3) Einzelnes Rezept anzeigen\n"
            "4) Nach Zutaten suchen\n"
            "5) Rezepte speichern\n"
            "6) Rezepte laden\n"
            "0) Zurück zum Hauptmenü"
        )
        choice = read_int("Auswahl: ")

        if choice == 1:
            from functionsstorage import create_new_recipe
            new_recipe = create_new_recipe()
            if new_recipe:
                recipes.append(new_recipe)
                print("Rezept wurde hinzugefügt!")
        elif choice == 2:
            selected = select_recipe_from_list(recipes)
            if selected:
                show_recipe_detail_flow(selected)
        elif choice == 3:
            recipe_name = input("Rezeptname eingeben: ").strip()
            found = next((r for r in recipes if r.get('recipe_name', '').lower() == recipe_name.lower()), None)
            if found:
                show_recipe_detail_flow(found)
            else:
                print("Rezept nicht gefunden.")
        elif choice == 4:
            from functionsstorage import search_by_ingredient
            ingredient = input("Zutat eingeben: ").strip()
            filtered = search_by_ingredient(recipes, ingredient)
            if filtered:
                selected = select_recipe_from_list(filtered)
                if selected:
                    show_recipe_detail_flow(selected)
            else:
                print("Keine Rezepte mit dieser Zutat gefunden.")
        elif choice == 5:
            save_recipes(recipes)
        elif choice == 6:
            recipes = load_recipes()
            print("Rezepte wurden geladen.")
        elif choice == 0:
            break
        else:
            print("Ungültige Auswahl.")

    return recipes

def find_hp_character_flow():
    pass

def adjust_recipes_flow():
    pass

def show_main_menu():
    print(
        "Was möchtest du tun? Wähle bitte 1, 2, 3 oder 4.\n"
        "1) Rezept zum Kochen finden\n"
        "2) Rezepte nach Harry-Potter-Charakteren entdecken\n"
        "3) Rezepte verwalten (hinzufügen, anzeigen, speichern, laden)\n"
        "4) Beenden"
    )
    return read_int("Auswahl: ")
    

