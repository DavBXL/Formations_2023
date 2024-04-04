"""
Créer un script qui
• demande notre prénom et notre date de naissance (jour, mois et
année) dans l’interface (fonction input
• calcule notre âge
• Calcule le nombre de jours restants avant notre anniversaire
• affiche (fonction print() ) un texte avec notre prénom, notre âge
et le nombre de jours restants avant notre anniversaire
"""

import datetime

print("Hello...")

name = input("What's your name? ")

print("Nice to meet you ", name, "! I'm Python...")

print("What's your birthdate? ")
birthdate = input("Enter a date in dd/mm/yyyy format : ")

birth_day = birthdate[0:2]
birth_month = birthdate[3:5]
birth_year = birthdate[-4:]
print("birthdate : ", birth_day, birth_month, birth_year)

mydate = datetime.date.today()
cur_day = mydate.day
cur_month = mydate.month
cur_year = mydate.year
print("Current day : ", cur_day, cur_month, cur_year)

age = int(cur_year) - int(birth_year)

if (int(cur_month) - int(birth_month)) >= 0:
    print("You're ", age, " years old.")

if (int(cur_month) - int(birth_month)) < 0:
    print("You're ", age - 1, " years old.")
