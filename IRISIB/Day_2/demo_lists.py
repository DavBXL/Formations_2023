values = [1, 12, 24, 48, 15, 30, 50, 100]
scores = [10, 12, 8]
third_value = values[2]   # Lecture dans une liste
print(third_value)
values[5] = 71  # Modifie l'élément d'indice 5 dans la liste
print(values)
values[:2] = [10, 100]  # Remplace les éléments d'indice 0 et 1 de la liste
print(values)
values.append(0)    # Ajoute 0 à la fin de la liste (ce 0 devient le dernier élément)
print(values)
values.remove(100)  # Retrait par valeur : retire UNIQUEMENT la 1ere occurrence de 100 ici
print(values)
print(values.count(100))
popped_value = values.pop(0)    # Retrait par indice : retire l'élément d'indice 0 (ici 10)
print(values)
print(values.index(0))
values.sort()
print(values)
values.reverse()
print(values)
values.insert(3, 12)
print(values)
values.extend((800, 900, 1000))
print(values)


