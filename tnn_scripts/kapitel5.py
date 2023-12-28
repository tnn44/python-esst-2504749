# Zufallszahl
import random

# zufallszahl = random.randint(0,3)

wahlmglkt_pc = ["Schere", "Stein", "Papier"]
zufallswahl_computer = random.choice(wahlmglkt_pc)


# Schere Stein Papier (Schere > Papier, Papier > Stein, Stein > Schere); Funktion input --> im Terminal kann dann eingegeben werden, was der User wählen möchte
user_eingabe = input('Schere, Stein oder Papier? ')
print('Deine Wahl ist:', user_eingabe)

print('Der Computer wählt:', zufallswahl_computer)

if (user_eingabe == "Stein" and zufallswahl_computer == "Papier"):
  print('DU HAST VERLOREN!')
elif (user_eingabe == "Stein" and zufallswahl_computer == "Schere"):
  print('DU HAST GEWONNEN!')
elif (user_eingabe == "Schere" and zufallswahl_computer == "Papier"):
  print('DU HAST GEWONNEN!')
elif (user_eingabe == "Schere" and zufallswahl_computer == "Stein"):
  print('DU HAST VERLOREN!')
elif (user_eingabe == "Papier" and zufallswahl_computer == "Schere"):
  print('DU HAST VERLOREN!')
elif (user_eingabe == "Papier" and zufallswahl_computer == "Stein"):
  print('DU HAST GEWONNEN!')
else:
  print('UNENTSCHIEDEN')


