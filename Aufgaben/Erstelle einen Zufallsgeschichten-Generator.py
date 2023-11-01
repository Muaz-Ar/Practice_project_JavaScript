import random

# Listen von Wörtern und Phrasen in verschiedenen Kategorien
subekte = [
    "Ein grüner Dinosaurier",
    "Ein frecher Pinguin",
    "Ein furchtloser Astronaut",
    "Eine flauschige Katze",
    "Ein tanzender Roboter"
]

verben = [
    "tanzt",
    "fliegt",
    "lacht über",
    "sucht nach",
    "träumt von"
]

objekte = [
    "eine Banane",
    "einen Regenbogen",
    "eine Tasse Kaffee",
    "einen Schatz",
    "einen Alien"
]

orte = [
    "auf dem Mond",
    "im Dschungel",
    "in der Wüste",
    "auf dem Mars",
    "in einem geheimen Labor"
]

# Begrüßung
print("Willkommen zum Zufallsgeschichten-Generator!")

# Hauptschleife
while True:
    try:
        anzahl_sätze = int(input("Geben Sie die Anzahl der Sätze in der Geschichte ein: "))

        # Generiere die Geschichte
        geschichte = ""
        for _ in range(anzahl_sätze):
            satz = f"{random.choice(subekte)} {random.choice(verben)} {random.choice(objekte)} {random.choice(orte)}."
            geschichte += satz + " "

        # Ausgabe der generierten Geschichte
        print("\nHier ist deine zufällige Geschichte:")
        print(geschichte)
        
        # Grußformel und Option zur Generierung weiterer Geschichten
        weitere_generierung = input("\nMöchten Sie eine weitere Geschichte generieren? (Ja/Nein): ").lower()
        if weitere_generierung != "ja":
            print("Vielen Dank und auf Wiedersehen!")
            break

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
