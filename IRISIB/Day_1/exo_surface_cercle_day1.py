import math

"""
Réalisez un programme qui à partir diamètre d’un cercle
en cm calcule sa surface en m²
Input prend le diamètre en cm
Le programme calcule l’aire en m² et l’affiche
"""



print("Calcul de  la surface d'un cercle a partir de son diametre")
print()
print("Veuillez introduire le diametre du cercle")
print()

diam = int(input("Diametre (cm) : "))

ray = diam / 2

surf = ((ray ** 2) * math.pi) / 10000

print("Surface (m2) = ", str(surf), "m2")

