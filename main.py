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
        consommations.append(float(ligne["consommation"]))


moyenne = somme / nombre 
minimum = min(consommations)
maximum = max(consommations)

print("Moyenne :" + str(moyenne))
print("Somme :" + str(somme))
print(" Minimum  :" + str(minimum))
print(" Maximum  :" + str(maximum))

