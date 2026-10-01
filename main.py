import csv

consommations = []
somme = 0
nombre = 0

with open("energy.csv", "r", encoding="utf-8-sig") as fichier:
    lecteur = csv.DictReader(fichier, delimiter = ";")

    for ligne in lecteur:
        consommation = float((ligne["consommation"]))
        somme += consommation
        nombre += 1

moyenne = somme / nombre 
print(moyenne)
print(somme)
