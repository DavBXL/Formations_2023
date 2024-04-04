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
import calendar

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

joursJanvier = (calendar.monthrange(cur_year, 1)[1])
joursFevrier = (calendar.monthrange(cur_year, 2)[1])
joursMars = (calendar.monthrange(cur_year, 3)[1])
joursAvril = (calendar.monthrange(cur_year, 4)[1])
joursMai = (calendar.monthrange(cur_year, 5)[1])
joursJuin = (calendar.monthrange(cur_year, 6)[1])
joursJuillet = (calendar.monthrange(cur_year, 7)[1])
joursAout = (calendar.monthrange(cur_year, 8)[1])
joursSeptembre = (calendar.monthrange(cur_year, 9)[1])
joursOctobre = (calendar.monthrange(cur_year, 10)[1])
joursNovembre = (calendar.monthrange(cur_year, 11)[1])
joursDecembre = (calendar.monthrange(cur_year, 12)[1])

# Convert birthdate to a datetime object
birthdate_dt = datetime.datetime.strptime(birthdate, "%d/%m/%Y").date()

# Calculate next birthday
next_birthday = datetime.date(cur_year, int(birth_month), int(birth_day))
if next_birthday < mydate:
    next_birthday = datetime.date(cur_year + 1, int(birth_month), int(birth_day))

# Calculate remaining days
days_remaining = (next_birthday - mydate).days
print("Days remaining until your next birthday:", days_remaining)
print()
print("Dear ", name, ",in ", days_remaining, " days, you will turn ", age)
