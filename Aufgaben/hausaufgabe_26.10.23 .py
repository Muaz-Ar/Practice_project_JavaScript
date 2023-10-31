# Aufgabe 1 Loops in console from to

def from_to(start, end): 
    for i in range(start, end + 1): # Das end ist in range nicht mit einbegriffen 
        print(i) 

from_to(1, 15)

# Aufgabe 1 in liste wiedergeben mit return 

def from_to1(start, end):
    resultat = []
    for i in range(start, end + 1):
        resultat.append(i)
    return resultat

range_1 = from_to1(5, 15) 
print(range_1)

# Aufgabe 1 Zahlen 1 - 100 durchlaufen nur durch 6 teilbare ausgeben 
def div_by6(start, end, diff):
    resultat = []
    for i in range(start, end + 1, diff):
        resultat.append(i)
    return resultat

range_2 = div_by6(0, 100, 6) 
print(range_2)

# hab ich nicht wirklich verstanden ab modulu variante 
def div_by66():
    for num in range(1, 101):
        if num % 6 ==0:
            print(num)

print(div_by66())

# Aufgabe Fizzbuzz
def fizzbuzz(): 
    for num in range(1, 101): 
        if num % 3 == 0 and num % 5 == 0: 
            print("fizzbuzz")          
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else: 
            print(num)

print(fizzbuzz())

# Aufgabe 2 Summe einer Liste ohne sum 

def sum_1(numbers):
    total = 0
    for i in numbers: 
        total += i 
    return total
liste = [1, 2, 3, 4, 5]
ergebnis = sum_1(liste) 
print("Die gesammtsummer der liste lautet: " + str(ergebnis))

# Avarage 

def avarage(numbers):
    total = 0
    for i in numbers: 
        total += i 
    return total / len(numbers)
liste = [1, 2, 3, 4, 5]
ergebnis = avarage(liste) 
print("Der durchschnitt der liste lautet: " + str(ergebnis))
