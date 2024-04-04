"""
L'IBN-10 sans clé comporte 9 chiffres :
Pour calculer la clé, opérer comme suit :
multiplier chacun des chiffres de l'ISBN-10 pris de gauche à droite par les poids 10, 9, …, 3, 2 ;
faire la somme de ces neuf produits ;
calculer le reste de cette somme dans la division par 11 ;
si le reste est nul, la clé est aussi zéro, sinon retrancher ce reste de 11 : c'est la valeur de la clé. Si elle vaut
10, on la note "X".
Exemple pour l'ISBN 2-1234-5680-2 :
ISBN	2	1	2	3	4	5	6	8	0
Poids	10	9	8	7	6	5	4	3	2
Somme
pondéré	20	9	16	21	24	25	24	24	0	163
reste de 163 divisé par 11 = 9
11 – 9 = 2.
"""


isbn = input("ISBN number = ")

liste = []
for numbers in isbn:
    print(numbers)
    liste.append(numbers)
if liste[-1] == "X":
    liste.remove("X") and liste.append("10")

print(f"liste avec 10 si X: {liste}")

liste.remove("-")
liste.remove("-")
liste.remove("-")

print(f"liste sans les tirets: {liste}")

last_nb = liste.pop(-1)

print(f"dernier chiffre de la liste: {last_nb}")

weight = [10, 9, 8, 7, 6, 5, 4, 3, 2]
somme = 0

for indice in range(9):
    somme += int(liste[indice]) * weight[indice]
    print(somme)

reste = somme % 11
print(reste)

if reste == 0:
    key = 0

else:
    key = 11 - reste
print("Valid key : " + str(key))
print("Given key : " + last_nb)

if str(key) == last_nb:
    print("Valid ISBN number!")
if str(key) != last_nb:
    print("Not valid ISBN number. Key is not valid.")
