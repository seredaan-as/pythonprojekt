# pythonprojekt
## *Harry Potter Kochbuch*
## Ein interaktives Konsolenprogramm in Python zur Verwaltung und Anzeige magisch inspirierter Rezepte.
## Beschreibung
Dieses Projekt implementiert ein interaktives Harry-Potter-Kochbuch als Konsolenanwendung.
Das Programm ermöglicht es, Rezepte:
- nach Zeit
- nach Schwierigkeitsgrad
- nach Ernährungsform
- nach Gerichtstyp
- nach Harry Potter Charakteren oder
- per Zufallsprinzip
zu filtern und anzuzeigen.

Zusätzlich können:
- Portionen dynamisch angepasst 
- Einkaufszettel als Textdatei generiert 
- Neue Rezepte hinzugefügt 
- Rezepte gespeichert und geladen werden

## Projektstruktur
pythonprojekt/
- main.py              # Startpunkt des Programms
- ui.py                # Menüführung und Benutzerinteraktion
- functionsstorage.py  # Logik-Datei mit Hilfsfunktionen
- storage.py           # Laden & Speichern von JSON
- hp_recipes.json      # Rezeptdaten
- grocery_lists/       # Erstellte Einkaufszettel
- exported_recipes/    # Gespeicherte Rezepte
- (+) README.md


## Installation und  Bedienung
Voraussetzung: Python 3.10 oder höher
Programm starten: 
  -> Im Projektordner ausführen: python main.py

*Ablaufidee*
1. Hauptmenü
2. Rezept auswählen oder filtern
3. Rezeptdetails anzeigen
4. Mini-Menü:
  - Portionen anpassen
  - Einkaufszettel erstellen
  - Rezept speichern
  - Zurück ins Hauptmenü

Die Navigation erfolgt bewusst über return, um Endlosschleifen zu vermeiden.

## Datenspeicherung
Die Daten werden in einer JSON-Datei verwaltet. 
Die Speicherung der Rezepte und Einkaufszettel erfolg im TXT-Format.
Falls der entsprechende Ordner nicht existiert, wird er automatisch erstellt.

## Mögliche Erweiterungen
- Zutaten mehrerer Rezepte zusammenfassen
- Verbesserte Suchfunktionen
- Benutzerprofile

## Team
Sternberg, Leif
Sereda, Anastasiia

## Anforderungen
Ein Programm zur Verwaltung von Rezepten inklusive Zutaten und Zubereitungsschritten.

*Anforderungen:*
	• Anlegen neuer Rezepte (+)
	• Anzeige aller Rezepte (+)
	• Anzeigen einzelner Rezepte (+)
	• Speichern in und laden der Rezepte aus einer Datei (+)
	• Hauptmenü mit mehreren Auswahlmöglichkeiten (+)
	• Saubere Benutzerführung (Fehlermeldung bei falscher Eingabe) (+)
*Erweiterungen:*
	• suche nach Zutaten (+)
	• Portionsanpassung (nach Anzahl Personen) (+)
	• Kategorien (z.B. vegetarisch) (+)
	• Einkaufslisten-Generator (→ Einkaufsliste ist separate, formatierte Textdatei) (+)
	• Zufällige Rezeptauswahl (+)

