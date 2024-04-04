secondes = int(input("Enter number of seconds : "))

heures = secondes // 3600
secondes_restantes = secondes % 3600
minutes = secondes_restantes // 60
secondes_restantes = secondes_restantes % 60
print(secondes, "secondes représent ", heures, "h", minutes, secondes_restantes)
print(str(secondes) + " secondes représent " + str(heures) + " " + str(minutes) + " " + str(secondes_restantes))
print(f"{secondes} secondes représentent {heures}:{minutes}:{secondes_restantes}")

