#1 Aufgabe eins Begrüßung
name = input("Geben Sie Ihren Namen ein: ")

print("Hallo, " + name + "! Schön, dich kennenzulernen.")

#2 Aufgabe Flächeninhalt Rechteck
länge = float(input("Gib die Länge des Rechtecks ein: "))
breite = float(input("Gib die Breite des Rechtecks ein: "))

flächeninhalt = länge * breite

print("Der Flächeninhalt des Rechtecks beträgt:", flächeninhalt)

import random

# 3Aufgabe Zahl erraten
zielzahl = random.randint(1, 20)

while True:
    versuch = int(input("Errate die Zahl (zwischen 1 und 20): "))
    if versuch < zielzahl:
        print("Die gesuchte Zahl ist größer.")
    elif versuch > zielzahl:
        print("Die gesuchte Zahl ist kleiner.")
    else:
        print("Booo bist du gut. Du hast die richtige Zahl erraten. Spiel Lotto")
        break

# 4 Aufgabe Übung zu Listen 

liste_org = [1, 2, 3, 4, 5]

liste_1 = liste_org[::-1]

liste_2 = list_1 * 2


print("Ursprüngliche Liste:", liste_org)
print("Umgekehrte Liste:", liste_1)
print("Duplizierte Liste:", liste_2)

# 5 Aufgabe Zusatz

studenten = [("Andreas", 92), ("Pablo", 88), ("Dennis", 95), ("Abi", 78), ("Evelyn", 97)]

beste_studenten = sorted(studenten, key=lambda x: x[1], reverse=True)

print("Die besten drei Studenten sind:")
for student in beste_studenten[:3]:
    print(student[0], "-", student[1])
