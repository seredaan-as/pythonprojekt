# Hier kann man mit Dateien arbeiten: Rezepte speichern, aus Datei einlesen; Einkaufszettel?
import json
from typing import List, Dict                      # Für Typing, muss ggf vervollständigt werden, wenn du noch was anderes brauchst

json_file = "hp_recipes.json"

def load_recipes() -> list[dict]:
    try:
        with open(json_file, "r") as f:           # Fehlerbehandlung: Die Datei wird nach der Ausführunf im with-Block automatisch geschlossen
            recipes = json.load(f)
        return recipes
    except FileNotFoundError:
        print("Die Rezeptrollen fehlen im Regal — also beginnen wir mit einem leeren Pergament.")


def save_recipes():
    pass

def create_shopping_list():
    pass