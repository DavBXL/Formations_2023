# demandez à l'user de rentrer une année (en chiffrees)
# et dire si celle-ci est bissextile ou non

year = int(input("Enter a year : "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is leap")
else:
    print("year is not leap")

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"{year} is leap")
else:
    print("year is not leap")