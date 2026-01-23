# Hier kann man Pseudocode schreiben 
# für die main-Datei:
Function main():
    recipes -> load_recipes_from_file()
    user_name -> greet_user()

    REPEAT
        show_main_menu() -> choice:

        IF choice == 1 THEN
            find_recipe_flow(...)
        ELSE IF choice == 2 THEN
            character_flow(...)
        ELSE IF choice == 3 THEN
            manage_recipes_flow(...)
        ELSE IF choice == 4 THEN
            exit_logic_with_save(...)
            EXIT LOOP
        ELSE
            print("Ungültige Eingabe. Bitte erneut versuchen.")
        END IF

    UNTIL FALSE
END FUNCTION

# Begrüßung + Hauptmenü 
Function greet_user() -> STRING:
    print("=== Harry Potter Kochbuch ===")
    print("Willkommen, Reisender. Du hast das Harry-Potter-Kochbuch betreten.")
    print("Wie ist dein Name, Hexe oder Zauberer?")
    User_name input()

    print(Schön, dich kennenzulernen, [name]! Heute begleite ich dich durch die magische Küche.)
    print("Ich begleite dich heute durch die magische Küche.")
    RETURN name
END FUNCTION
