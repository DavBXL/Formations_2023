temperature =int(input("entrez la température : "))
if temperature <= 0:
    print("Il gèle")
elif temperature < 4:
    print("Conditions glissantes")
elif temperature > 5 and temperature <= 30: #if 5< temperature < 30:
    print("pas de souci")
else:
    print("chaleur intense")