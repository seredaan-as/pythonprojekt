#Start des Programms: Einstieg, Hauptschleife

from functionsstorage import read_int
from ui import greet_user, show_main_menu, find_recipe_flow, filter_by_complexity, filter_by_diet
from storage import load_recipes, save_recipes
import time  # Modul für Zeitfunktionen importieren (Zeitverzögerung zwischen den Ausgaben)


# ----------------------------------------------------

def main():
    recipes = load_recipes
    name = greet_user()

    while True:
        choice = show_main_menu()
        
        if choice == 1:
            find_recipe_flow()
        elif choice == 2:
            filter_by_complexity()
        elif choice == 3:
            filter_by_diet()
        elif choice == 4:
            print("Die Magie ruht nicht. Komm zurück, wann immer dir danach ist.")
            break
        else:
            print("Die Küchenelfen kennen diese Zahl leider nicht. Probier es mit einer anderen.")

main()