# Hier kann man mit Dateien arbeiten: Rezepte speichern, aus Datei einlesen; Einkaufszettel?
import json

json_file = "hp_recipes.json"

def load_recipes() -> list[dict]:
    try:
        with open(json_file, "r", encoding="utf-8") as f:           # Fehlerbehandlung: Die Datei wird nach der Ausführunf im with-Block automatisch geschlossen
            recipes = json.load(f)
        if not isinstance(recipes, list):
            print("Die Rezeptrolle ist beschädigt — starte mit einem leeren Pergament.")
            return []
        return recipes  # type: ignore[return-value]
    except FileNotFoundError:
        print("Die Rezeptrollen fehlen im Regal — also beginnen wir mit einem leeren Pergament.")
        return []
    except json.JSONDecodeError:
        print("Die Rezeptrolle ist unleserlich — starte mit einem leeren Pergament.")
        return []


def save_recipes(recipes: list[dict], filename: str = json_file) -> bool:
    """Speichert Rezepte als JSON-Datei; gibt True bei Erfolg zurück."""

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(recipes, f, ensure_ascii=False, indent=2)
        print(f"Rezepte gespeichert in: {filename}")
        return True
    except (OSError, TypeError) as e:
        print(f"Fehler beim Speichern der Rezepte: {e}")
        return False

def create_shopping_list():
    pass
