# Suchen, Filtern, Portionen, Character-Sachen
from typing import List, Dict

def adjust_portions(recipe: dict, target_servings: int) -> dict:
    """Passt die Portionen eines Rezepts an und gibt ein neues Rezept-Dict zurück."""
    if not recipe or target_servings <= 0:
        return recipe
    
    original_servings = recipe.get('servings', 1)
    if original_servings <= 0:
        original_servings = 1
    
    factor = target_servings / original_servings
    
    # Neues Rezept-Dict erstellen (Kopie)
    adjusted_recipe = recipe.copy()
    adjusted_recipe['servings'] = target_servings
    
    # Zutaten anpassen
    adjusted_ingredients = []
    for ingredient in recipe.get('ingredients', []):
        adjusted_ing = ingredient.copy()
        if adjusted_ing.get('amount') is not None:
            adjusted_ing['amount'] = round(adjusted_ing['amount'] * factor, 2)
        adjusted_ingredients.append(adjusted_ing)
    
    adjusted_recipe['ingredients'] = adjusted_ingredients
    
    print(f"Rezept wurde von {original_servings} auf {target_servings} Portionen angepasst (Faktor: {factor:.2f}).")
    return adjusted_recipe


def filter_by_character(recipes: list[dict], character: str) -> list[dict]:
    """Filtert Rezepte nach einem Harry-Potter-Charakter."""
    if not recipes or not character:
        return []
    
    filtered = []
    character_lower = character.lower()
    
    for recipe in recipes:
        characters = recipe.get('character', [])
        # Prüfen, ob der gesuchte Charakter in der Liste vorkommt (case-insensitive)
        if any(char.lower() == character_lower for char in characters):
            filtered.append(recipe)
    
    return filtered
