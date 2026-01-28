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