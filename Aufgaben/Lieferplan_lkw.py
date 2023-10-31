# Aufgabe lkv fahrt 

def fahrten_und_kisten(bestandt, kisten_pro_f):
    fahrten = bestandt // kisten_pro_f
    letzte_fahrt = bestandt % kisten_pro_f
    return fahrten, letzte_fahrt

# Beispielaufruf der Funktion
kisten_pro_f = 75
bestandt = 1000
fahrten, letzte_fahrt = fahrten_und_kisten(bestandt, kisten_pro_f )

print("Der Lkw muss", fahrten, "Fahrten machen.")
print("Bei der letzten Fahrt muss er", letzte_fahrt, "Kisten mitnehmen.")
