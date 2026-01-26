# Hier kann man mit Dateien arbeiten: Rezepte speichern, aus Datei einlesen; Einkaufszettel?
import json
from typing import List, Dict                      # Für Typing, muss ggf vervollständigt werden, wenn du noch was anderes brauchst

json_file = "hp_recipes.json"

def load_recipes() -> list[dict]:
    try:
        with open(json_file, "r", encoding="utf-8") as f:           # Fehlerbehandlung: Die Datei wird nach der Ausführung im with-Block automatisch geschlossen
            recipes = json.load(f)
        return recipes
    except FileNotFoundError:
        print("Die Rezeptrollen fehlen im Regal — also beginnen wir mit einem leeren Pergament.")
        return []


def save_recipes(recipes: list[dict]) -> None:
    """Speichert die Rezepte in die JSON-Datei."""
    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(recipes, f, ensure_ascii=False, indent=2)
        print("Die Rezeptrollen wurden sicher im Regal verstaut.")
    except Exception as e:
        print(f"Beim Speichern der Rezeptrollen ist etwas schiefgelaufen: {e}")


def create_shopping_list(recipe: dict) -> None:
    """Erstellt eine Einkaufsliste für ein Rezept als Textdatei."""
    if not recipe:
        print("Kein Rezept vorhanden für die Einkaufsliste.")
        return
    
    filename = f"einkaufsliste_{recipe.get('recipe_name', 'unbekannt').replace(' ', '_')}.txt"
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== Einkaufsliste: {recipe.get('recipe_name', 'Unbekanntes Rezept')} ===\n")
            f.write(f"Portionen: {recipe.get('servings', '?')}\n\n")
            f.write("Zutaten:\n")
            f.write("-" * 50 + "\n")
            
            for ingredient in recipe.get('ingredients', []):
                ing_name = ingredient.get('ingredient', '?')
                amount = ingredient.get('amount')
                unit = ingredient.get('unit', '')
                note = ingredient.get('note')
                
                line = f"- {ing_name}"
                if amount is not None:
                    line += f": {amount}"
                    if unit:
                        line += f" {unit}"
                if note:
                    line += f" ({note})"
                f.write(line + "\n")
        
        print(f"Einkaufsliste wurde erstellt: {filename}")
    except Exception as e:
        print(f"Beim Erstellen der Einkaufsliste ist etwas schiefgelaufen: {e}")
