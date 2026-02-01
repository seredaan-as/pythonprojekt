#Start des Programms: Einstieg, Hauptschleife

from ui import greet_user, show_main_menu, find_recipe_flow, handle_manage_recipes_flow, handle_character_flow
from functionsstorage import filter_by_complexity, filter_by_diet
from storage import load_recipes, save_recipes
import time  # Modul für Zeitfunktionen importieren (Zeitverzögerung zwischen den Ausgaben)


# ----------------------------------------------------

def main():
    """Startet die Hauptschleife des Programms.

    Lädt gespeicherte Rezepte, begrüßt den User und steuert die Navigation über das
    Hauptmenü in die jeweiligen Flows.

    Returns:
        None: Kein Rückgabewert; die Funktion führt das Programm aus.
    """
    recipes = load_recipes()
    name = greet_user()

    while True:
        choice = show_main_menu()
        
        if choice == 1:
            find_recipe_flow(recipes)                       # Auswahl 1: Rezepte zum Kochbuch finden
        elif choice == 2:            
            recipes = handle_manage_recipes_flow(recipes)   # Auswahl 2: Rezepte verwalten
        elif choice == 3:
            handle_character_flow(recipes)                  # Auswahl 3: Rezepte nach Charakter wählen
        elif choice == 4:
            print("Die Magie ruht nicht. Komm zurück, wann immer dir danach ist.")                      # Programm beenden
            break
        else:
            print("Die Küchenelfen kennen diese Zahl leider nicht. Probier es mit einer anderen.")      # Fehlerhafte Eingabe


if __name__ == "__main__":
    main()


