#Start des Programms: Einstieg, Hauptschleife

from ui import greet_user, show_main_menu, find_recipe_flow, handle_character_flow, handle_manage_recipes_flow
from storage import load_recipes
import time  # Modul für Zeitfunktionen importieren (Zeitverzögerung zwischen den Ausgaben)


# ----------------------------------------------------

def main():
    recipes = load_recipes()
    name = greet_user()

    while True:
        choice = show_main_menu()
        
        if choice == 1:
            find_recipe_flow()
        elif choice == 2:
            handle_character_flow(recipes)
        elif choice == 3:
            recipes = handle_manage_recipes_flow(recipes)
        elif choice == 4:
            print("Die Magie ruht nicht. Komm zurück, wann immer dir danach ist.")
            break
        else:
            print("Die Küchenelfen kennen diese Zahl leider nicht. Probier es mit einer anderen.")

main()