import csv

consommations = []

with open("energy.csv", "r", encoding="utf-8-sig") as fichier:
    lecteur = csv.DictReader(fichier, delimiter = ";")

    for ligne in lecteur:
        