# Menüs + Anzeige Funktionen
from functionsstorage import read_int, filter_by_time, filter_by_complexity, filter_by_diet, filter_by_course, get_random_recipe, filter_by_character, create_new_recipe, search_by_ingredient, show_recipe_details, select_recipe_from_list, mini_menu, create_grocery_list
from storage import load_recipes, save_recipes
import time


## Hauptmenü ###############################################


def greet_user():
    print("=== Harry Potter Kochbuch ===")
    print("Willkommen, Reisender. Du hast das Harry-Potter-Kochbuch betreten.")
    
    user_name = input("Wie ist dein Name, Hexe oder Zauberer?: ")
    print(f"Schön, dich kennenzulernen, {user_name}! Heute begleite ich dich durch die magische Küche.")


def show_main_menu(): 
    print("Was möchtest du tun? Wähle bitte 1, 2, 3 oder 4.")
    print("1) Rezept zum Kochen finden")
    print("2) Rezepte verwalten (hinzufügen, anzeigen, speichern, laden)")
    print("3) Rezepte nach Harry-Potter-Charakteren entdecken")
    print("4) Beenden")
    choice = read_int("Auswahl: ")
    return choice


## Auswahl 1: Rezepte zum Kochbuch finden ##############


def find_recipe_flow(recipes):
    
    recipes = load_recipes()

    print("Dieses Harry-Potter-Kochbuch ist ein interaktives Abenteuer, und ich begleite dich auf deiner kulinarischen Reise.")
    print("Was ist dir heute wichtig: Zeit, Schwierigkeit, Ernährungsweise oder bist du noch unentschlossen?")
    print("1) Zeit – ich habe wenig Zeit")
    print("2) Komplexität – einfach / mittel / anspruchsvoll")
    print("3) Ernährungsform – vegan / vegetarisch / pescetarisch / standard")
    print("4) Gerichtstyp - Vorspeise / Hauptgericht / Nachtisch")
    print("5) Zufallsrezept")
    print("0) Zurück zum Hauptmenü")

    choice = read_int("Wähle eine Option aus: ")

    if choice == 1:
        print("Wie viel Zeit hast du heute? Wir finden ein passendes Rezept für dich.")
        max_minutes = read_int("Gib bitte Minuten als Zahl an: ")

        filtered = filter_by_time(recipes, max_minutes)
        selected = select_recipe_from_list(filtered)        #Result: chosen recipe

        if selected is not None: 
            chosen_name = selected.get("recipe_name") or selected.get("title") or "Unbekanntes Rezept"
            print(f"\nDu hast gewählt: {chosen_name}")
            show_recipe_details(selected)


        if selected is None: 
            print("Hm… die Küchenelfen haben in ihren Kesseln gerührt, aber kein Rezept ist erschienen. Versuche eine andere Zauberformel (äh… Auswahl).")
    
    elif choice == 2:
        print("Welchen Schwierigkeitsgrad soll dein Rezeptzauber haben?")
        print("1) leicht")
        print("2) mittel")
        print("3) anspruchsvoll")
        sub_choice = read_int("Wähle eine Option aus: ")

        complexity_map = {1: "leicht", 2: "mittel", 3: "anspruchsvoll"}
        complexity = complexity_map.get(sub_choice)

        if complexity is None:
            print("Die Küchenelfen verstehen diese Wahl der Schwierigkeit nicht.")
            return

        filtered = filter_by_complexity(recipes, complexity)
        selected = select_recipe_from_list(filtered)

        if selected is not None:
            chosen_name = selected.get("recipe_name") or selected.get("title") or "Unbekanntes Rezept"
            print(f"\nDu hast gewählt: {chosen_name}")
            show_recipe_details(selected)
        else:
            print("Hm… die Küchenelfen haben in ihren Kesseln gerührt, aber kein Rezept mit dieser Komplexität ist erschienen.")

    elif choice == 3:
        print("Welche Ernährungsform suchst du?")
        print("1) vegan")
        print("2) vegetarisch")
        print("3) pescetarisch")
        print("4) standard")
        sub_choice = read_int("Wähle eine Option aus: ")

        diet_map = {1: "vegan", 2: "vegetarisch", 3: "pescetarisch", 4: "standard"}
        diet = diet_map.get(sub_choice)

        if diet is None:
            print("Die Küchenelfen verstehen diese Ernährungsform nicht.")
            return

        filtered = filter_by_diet(recipes, diet)
        selected = select_recipe_from_list(filtered)

        if selected is not None:
            chosen_name = selected.get("recipe_name") or selected.get("title") or "Unbekanntes Rezept"
            print(f"\nDu hast gewählt: {chosen_name}")
            show_recipe_details(selected)
        else:
            print("Hm… die Küchenelfen haben in ihren Kesseln gerührt, aber kein Rezept mit dieser Ernährungsform ist erschienen.")

    elif choice == 4:
        print("Nach welcher Art von Zaubergericht suchst du??")
        print("1) Vorspeise")
        print("2) Hauptgericht")
        print("3) Nachtisch")
        print("4) Zurück")
        sub_choice = read_int("Wähle eine Option aus: ")

        course_map = {1: "vorspeise", 2: "hauptgericht", 3: "nachtisch"}
        course = course_map.get(sub_choice)

        if course is None: 
            print("Die Küchenelfen verstehen diese Zaubergerichtart nicht.")
            return
        
        filtered = filter_by_course(recipes, course)
        selected = select_recipe_from_list(filtered)
        
        if selected is not None: 
            chosen_name = selected.get("recipe_name") or selected.get("title") or "Unbekanntes Rezept"
            print(f"\nDu hast gewählt: {chosen_name}")
            show_recipe_details(selected)

        if selected is None: 
            print("Hm… die Küchenelfen haben in ihren Kesseln gerührt, aber kein Rezept ist erschienen. Versuche eine andere Zauberformel (äh… Auswahl).")


    elif choice == 5:
        if not recipes:
            print("Leider kein Rezept gefunden (keine Rezepte geladen).")
            return

        while True:
            random_recipe = get_random_recipe(recipes)
            if not random_recipe:
                print("Leider kein Rezept gefunden (keine Rezepte geladen).")
                break

            chosen_name = random_recipe.get("recipe_name") or random_recipe.get("title") or "Unbekanntes Rezept"
            print(f"\nHeutiger Vorschlag: {chosen_name}")
            show_recipe_details(random_recipe)

            again = input("\nGefällt dir dieses Rezept nicht? Neues Zufallsrezept anzeigen? (j/n): ").strip().lower()
            if again not in ("j", "ja", "y", "yes"):
                break
    elif choice == 0:
        print("Hauptmenü wird geladen...")
        time.sleep(2)
        return                   # Zurück ins Hauptmenü - show_main_menu Ebene
    else:
        print("Die Küchenelfen schauen ratlos – diese Wahl kennen sie nicht. Probier eine andere.")


## Auswahl 2: Rezepte verwalten #######


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
            new_recipe = create_new_recipe()
            if new_recipe:
                recipes.append(new_recipe)
                print("Rezept wurde hinzugefügt!")
        elif choice == 2:
            selected = select_recipe_from_list(recipes)
            if selected:
                show_recipe_details(selected)
        elif choice == 3:
            recipe_name = input("Rezeptname eingeben: ").strip()
            found = next((r for r in recipes if r.get('recipe_name', '').lower() == recipe_name.lower()), None)
            if found:
                show_recipe_details(found)
            else:
                print("Rezept nicht gefunden.")
        elif choice == 4:            
            ingredient = input("Zutat eingeben: ").strip()
            filtered = search_by_ingredient(recipes, ingredient)
            if filtered:
                selected = select_recipe_from_list(filtered)
                if selected:
                    show_recipe_details(selected)
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


## Auswahl 3: Rezepte nach Charakter wählen #####################

    
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

    # Alle gefundenen Charaktere auflisten
    print("\nVerfügbare Charaktere:")
    for i, char in enumerate(all_characters, 1):
        print(f"{i}) {char}")
    print("0) Zurück")

    # Nutzer wählt dass er zurück möchte
    choice = read_int("\nWähle einen Charakter: ")
    if choice == 0:
        return
    
    # Nutzer wählt einen Charakter und erhält das Rezept
    if 1 <= choice <= len(all_characters):
        selected_character = all_characters[choice - 1]
        filtered = filter_by_character(recipes, selected_character)
        if filtered:
            print(f"\nRezepte für {selected_character}:")
            selected_recipe = select_recipe_from_list(filtered)
            if selected_recipe:
                show_recipe_details(selected_recipe)
        else:
            print(f"Keine Rezepte für {selected_character} gefunden.")
    else:
        print("Ungültige Auswahl.")
 

## Übergreifend genutzt


# `select_recipe_from_list` and `show_recipe_details` are provided by `functionsstorage`

