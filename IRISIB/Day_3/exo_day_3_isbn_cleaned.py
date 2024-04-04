isbn = input("ISBN number = ")

liste = []
for numbers in isbn:
    liste.append(numbers)

liste.remove("-")
liste.remove("-")
liste.remove("-")

last_nb = liste.pop(-1)

weight = [10, 9, 8, 7, 6, 5, 4, 3, 2]
somme = 0

for indice in range(9):
    somme += int(liste[indice]) * weight[indice]

reste = somme % 11

if reste == 0:
    key = 0
else:
    key = 11 - reste

if str(key) == "10" and last_nb == "X" or str(key) == last_nb:
    print("Valid ISBN number!")
elif str(key) != last_nb:
    print("Not valid ISBN number. Key is not valid.")
