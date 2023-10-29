# Gegebene Schülerdaten
mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

# Durchschnittsnote berechnen
durchschnitt_mathematik = sum(mathematik) / len(mathematik)
durchschnitt_physik = sum(physik) / len(physik)
durchschnitt_chemie = sum(chemie) / len(chemie)
durchschnitt_noten = [durchschnitt_mathematik, durchschnitt_physik, durchschnitt_chemie]

# Beste und schlechteste Note finden
beste_noten = [max(mathematik), max(physik), max(chemie)]
schlechteste_noten = [min(mathematik), min(physik), min(chemie)]

# Gesamtdurchschnittsnote berechnen
gesamtdurchschnitt = (durchschnitt_mathematik + durchschnitt_physik + durchschnitt_chemie) / 3

# Notenstatistik
mindestens_90 = [len([note for note in mathematik if note >= 90]),
                len([note for note in physik if note >= 90]),
                len([note for note in chemie if note >= 90])]

# Notenverteilung anzeigen
def notenverteilung(fach):
    noten_dict = {}
    for note in fach:
        if note in noten_dict:
            noten_dict[note] += 1
        else:
            noten_dict[note] = 1
    return noten_dict

verteilung_mathematik = notenverteilung(mathematik)
verteilung_physik = notenverteilung(physik)
verteilung_chemie = notenverteilung(chemie)

print("Durchschnittsnote in Mathe, Physik, Chemie:", durchschnitt_noten)
print("Beste Noten in Mathe, Physik, Chemie:", beste_noten)
print("Schlechteste Noten in Mathe, Physik, Chemie:", schlechteste_noten)
print("Gesamtdurchschnittsnote aller Schüler:", gesamtdurchschnitt)
print("Anzahl der Schüler mit mindestens 90 in Mathe, Physik, Chemie:", mindestens_90)

print("Notenverteilung in Mathe:", verteilung_mathematik)
print("Notenverteilung in Physik:", verteilung_physik)
print("Notenverteilung in Chemie:", verteilung_chemie)
