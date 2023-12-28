# Wenn Dann Abfragen / Vergleichsabfrage (True False)
# True --> ==

variable_1 = 8
variable_2 = 9
variable_3 = 10


if (variable_1 < variable_2) and (variable_1 < variable_3):
    print('Var1 kleiner als Var2 und Var3')

# logisches oder = or
    
# if else: wenn Kondition NICHT true ist, wird der else-Block ausgeführt 
# if else if: im Else eine zusätzliche if (elif!) abfrage 
# (nur wenn die erste Kondition false ist und die 2. Kondition true ist, wird der Code ausgeführt. 
    #Sonst wird der Code im Else-Block ausgeführt)

variable_4 = 8
variable_5 = 9
variable_6 = 10

if (variable_4 < variable_5):
    print('Var4 ist kleiner Var5')
else: 
    print('Var4 ist NICHT kleiner als Var5')

variable_6 = 11
variable_7 = 9
variable_8 = 10

if (variable_6 < variable_7):
    print('Var6 ist kleiner als Var7')
elif (variable_2 < variable_8):
    print('Var6 ist NICHT kleiner als Var7 UND')
    print('Var7 ist kleiner als Var8')
else: 
    print('Else Pfad')

# Loops for-Schleifen 
meine_zahlen = [0,10,50]

for i in meine_zahlen:
    print('Die aktuelle Zahl ist', i)

for j in range(3):
    print('Die aktuelle Zahl ist', meine_zahlen[j])

# While: solange ausführen bis Bedingung nicht mehr erfüllt ist (man weiß nicht wann das ist)

meine_var = 2
while(meine_var < 20): 
    print('Variable =', meine_var)
    meine_var = meine_var*2
# Wird nur bis 16 ausgeführt, da danach 32 kommt und 32 nicht kleiner 20. 

# Challenge1: Array mit 5 Werten anlegen; jedem Wert den 3-fachen Wert des Index zuweisen; Anzahl der Werte ausgeben, die größer gleich 6 sind.
mein_array = [1, 2, 3, 4, 5]
print('Listenwert an Index 2', mein_array[2])

for i in range(5):
    mein_array[i] = mein_array[i] * 3
    print('Variable mein_array', mein_array[i])

for j in mein_array:
    if j > 6:
        print('Wert groesser 6 =', j)


# Challenge2
erstevar = 10
zweitevar = 2

while(zweitevar <= erstevar):
    erstevar = erstevar+1
    zweitevar = zweitevar+2

print('Zweitevar größer als Erstevar, Wert Var1', erstevar)
print('Zweitevar größer als Erstevar, Wert Var2', zweitevar)