# Funktionen: def Funktionsname(parameter, parameter)
def variablen_ausgabe(parameter):
  print('Die Fkt hat den Parameter', parameter, 'bekommen')

# Funktion erstellen, die eine Summe aus 2 Werten bildet
def summe(summand_a, summand_b):
  summe = summand_a + summand_b
  return summe

def summenausgabe(parameter):
  print('Die Summe lautet:', parameter, '!!!')

mein_parameter = 5
variablen_ausgabe(mein_parameter)

mein_parameter2 = 6


meine_summe = summe(mein_parameter, mein_parameter2)
summenausgabe(meine_summe)

# Challenge1: Funktion mit Namen ausgabe_meine_liste, die eine Liste als Parameter übernimmt

def ausgabe_meine_liste(liste):
  for element in liste:
    print('Das sind die Listenelemente:', element)

testliste = [1,2,3,4,5]
ausgabe_meine_liste(testliste)

# Challenge2: 
def multipli(gleitkommazahl1, gleitkommazahl2):
  produkt = gleitkommazahl1 * (gleitkommazahl2 + 2)
  return produkt

gkz1 = 2.2
gkz2 = 3.3
testprodukt = multipli(gkz1, gkz2)
print('Das Produkt ist:', testprodukt)

# Challenge3
def boolfkt(zahl1, zahl2, zahl3):
  if(zahl1 < zahl2) and (zahl2 < zahl3):
    return True
  else:
    return False

testzahl1 = 1
testzahl2 = 2
testzahl3 = 3

testbool = boolfkt(testzahl1, testzahl2, testzahl3)
print('Das Testergebnis lautet:', testbool)