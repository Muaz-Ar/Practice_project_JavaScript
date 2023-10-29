def verschluessle_zeichen(zeichen, schluessel):
    if 'a' <= zeichen <= 'z':
        verschiebung = ord(zeichen) - ord('a')
        verschluesseltes_zeichen = chr(((verschiebung + schluessel) % 26) + ord('a'))
    elif 'A' <= zeichen <= 'Z':
        verschiebung = ord(zeichen) - ord('A')
        verschluesseltes_zeichen = chr(((verschiebung + schluessel) % 26) + ord('A'))
    else:
        verschluesseltes_zeichen = zeichen
    return verschluesseltes_zeichen

def caesar_verschluesseln(text, schluessel):
    verschluesselter_text = ""
    for zeichen in text:
        verschluesseltes_zeichen = verschluessle_zeichen(zeichen, schluessel)
        verschluesselter_text += verschluesseltes_zeichen
    return verschluesselter_text

def caesar_entschluesseln(verschluesselter_text, schluessel):
    return caesar_verschluesseln(verschluesselter_text, -schluessel)

def main():
    while True:
        print("Willkommen zum Caesar-Verschlüsselungsprogramm!")
        nachricht = input("Geben Sie die Textnachricht ein: ")
        
        # Sicherheitsmaßnahmen: Überprüfen, ob der Schlüssel eine ganze Zahl im gültigen Bereich ist
        while True:
            try:
                schluessel = int(input("Gib eine ganze Zahl die zwische -25 bis +25 liegen an: "))
                if -25 <= schluessel <= 25:
                    break
                else:
                    print("Die Zahl muss zwischen -25 bis +25 liegen.")
            except ValueError:
                print("Ungültige Eingabe. Der Schlüssel muss eine ganze Zahl sein.")
        
        modus = input("Möchten Sie die Nachricht verschlüsseln (v) oder entschlüsseln (e)? ").lower()
        
        if modus == 'v':
            verschluesselter_text = caesar_verschluesseln(nachricht, schluessel)
            print(f"Verschlüsselte Nachricht: {verschluesselter_text}")
        elif modus == 'e':
            entschluesselte_text = caesar_entschluesseln(nachricht, schluessel)
            print(f"Entschlüsselte Nachricht: {entschluesselte_text}")
        else:
            print("Ungültige Auswahl. Bitte 'v' für Verschlüsselung oder 'e' für Entschlüsselung eingeben.")
        
        weiter = input("Möchten Sie eine weitere Nachricht verschlüsseln oder entschlüsseln? (j/n): ").lower()
        if weiter != 'j':
            break

if __name__ == "__main__":
    main()
