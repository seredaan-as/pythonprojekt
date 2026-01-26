
        

# weitere Hilfsfunktionen

def filter_by_time():  
    pass
def filter_by_complexity():  
    pass
def filter_by_diet():  
    pass
def filter_by_course():  
    pass
def get_random_recipe():  
    pass
def create_new_recipe():  
    pass
def search_by_ingredient():  
    pass
def adjust_portions():  
    pass

# + Fehlerbehandlung für Files (wenn der Name nicht gefunden wird, Script Seite 15, 17, 1ß)






# ______________ ab hier fertige Funktionen ____________________________________

# Hilfsfunktion, damit die Zahlen eingelesehen und Fehler abgedeckt werden (Fehlerbehandlung)

def read_int(promt: str) -> int:
    while True:
        value = input(promt)
        try:
            return int(value)
        except ValueError:
            print("Bitte eine Zahl eingeben – die Magie erledigt den Rest.")



