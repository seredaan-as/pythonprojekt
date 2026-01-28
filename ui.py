# Menüs + Anzeige Funktionen
from functionsstorage import read_int, filter_by_time, filter_by_complexity, filter_by_diet, filter_by_course, get_random_recipe, select_recipe_from_list, show_recipe_details  
from storage import load_recipes, save_recipes
import time

def greet_user():
    print("=== Harry Potter Kochbuch ===")
    print("Willkommen, Reisender. Du hast das Harry-Potter-Kochbuch betreten.")
    
    user_name = input("Wie ist dein Name, Hexe oder Zauberer?: ")
    print(f"Schön, dich kennenzulernen, {user_name}! Heute begleite ich dich durch die magische Küche.")


    
def find_recipe_flow(recipes):
    
    recipes = load_recipes()

    print("Dieses Harry-Potter-Kochbuch ist ein interaktives Abenteuer, und ich begleite dich auf deiner kulinarischen Reise.")
    print("Was ist dir heute wichtig: Zeit, Schwierigkeit, Ernährungsweise oder bist du noch unentschlossen?")
    print("1) Zeit – ich habe wenig Zeit")
    print("2) Komplexität – leicht / mittel / anspruchsvoll")
    print("3) Ernährungsform – vegan / vegetarisch / pescetarisch / standard")
    print("4) Gerichtstyp (Vorspeise/Hauptspeise/Nachspeise)")
    print("5) Zufallsrezept")
    print("6) Zurück zum Hauptmenü")

    choice = read_int("Wähle eine Option aus: ")

    if choice == 1:
        print("Wie viel Zeit hast du heute? Wir finden ein passendes Rezept für dich.")
        max_minutes = read_int("Gib bitte Minuten als Zahl an: ")

        filtered = filter_by_time(recipes, max_minutes)
        selected = select_recipe_from_list(filtered)        #Result: chosen recipe

        if selected is not None: 
            print(f"\nDu hast gewählt: {selected["recipe_name"]}")        
            show_recipe_details(selected)

        if selected is None: 
            print("Hm… die Küchenelfen haben in ihren Kesseln gerührt, aber kein Rezept ist erschienen. Versuche eine andere Zauberformel (äh… Auswahl).")
    elif choice == 2:
        filter_by_complexity()
    elif choice == 3:
        filter_by_diet()
    elif choice == 4:
        filter_by_course()
    elif choice == 5:
        get_random_recipe()
    elif choice == 6:
        print("Hauptmenü wird geladen...")
        time.sleep(2)
        return                   # Zurück ins Hauptmenü - show_main_menu Ebene
    else:
        print("Die Küchenelfen schauen ratlos – diese Wahl kennen sie nicht. Probier eine andere.")


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
    print("Was möchtest du tun? Wähle bitte 1, 2, 3 oder 4.")
    print("1) Rezept zum Kochen finden")
    print("2) Rezepte nach Harry-Potter-Charakteren entdecken")
    print("3) Rezepte verwalten (hinzufügen, anzeigen, speichern, laden)")
    print("4) Beenden")
    choice = read_int("Auswahl: ")
    return choice
    

def list_recipes(recipes):
    print("\n-- Rezeptliste --")
    if not recipes:
        print("Keine Rezepte vorhanden")
        return
    for i, r in enumerate(recipes, start=1):
        print(f"{i} - {r['title']}")

    
def choose_recipe_index(recipes):
    if not recipes:
        return None
    list_recipes(recipes)
    idx = read_int("Welche Nummer möchtest du ansehen? (0 = Abbrechen): ")
    if idx == 0:
        return None
    if idx < 1 or idx > len(recipes):
        print("Ungültige Nummer.")
        return None
    return idx - 1


def show_recipe_details(recipe):
    print(f"\n=== {recipe['title']} ===")

    print("\nZutaten:")
    for z in recipe.get("ingredients", []):
        # Erwartetes Format: {"name": "...", "amount": ..., "unit": "..."}
        print(f"- {z['name']}: {z['amount']} {z['unit']}")

    print("\nSchritte:")
    for i, step in enumerate(recipe.get("steps", []), start=1):
        print(f"{i}. {step}")


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





def input_ingredients():
    print("\nZutaten eingeben im Format: Name;Menge;Einheit (z.B. Mehl;200;g)")
    print("Leere Eingabe beendet die Zutatenliste.")
    ingredients = []

    while True:
        line = input("Zutat: ").strip()
        if line == "":
            break

        parts = [p.strip() for p in line.split(";")]
        if len(parts) != 3:
            print("Ungültiges Format. Bitte genau: Name;Menge;Einheit")
            continue

        name, amount_str, unit = parts
        if not name or not unit:
            print("Name und Einheit dürfen nicht leer sein.")
            continue

        try:
            amount = float(amount_str.replace(",", "."))
        except ValueError:
            print("Menge muss eine Zahl sein.")
            continue

        ingredients.append({"name": name, "amount": amount, "unit": unit})

    return ingredients


def input_steps():
    print("\nSchritte eingeben (je Zeile ein Schritt). Leere Eingabe beendet.")
    steps = []
    i = 1
    while True:
        step = input(f"Schritt {i}: ").strip()
        if step == "":
            break
        steps.append(step)
        i += 1
    return steps


def input_recipe():
    title = input("Rezept-Titel: ").strip()
    if not title:
        print("Titel darf nicht leer sein.")
        return None

    ingredients = input_ingredients()
    steps = input_steps()

    return {"title": title, "ingredients": ingredients, "steps": steps}


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


