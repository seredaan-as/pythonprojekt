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
    

