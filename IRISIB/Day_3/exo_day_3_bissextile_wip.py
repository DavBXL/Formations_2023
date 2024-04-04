"""Les années sont bissextiles si elles sont multiples de quatre, mais pas si elles sont multiples de cent,
à l'exception des années multiples de quatre cents qui, elles, sont également bissextiles. Ainsi, les années 2020,
2024 et 2028 sont bissextiles, de même que 2000 ou 2400, mais pas 1900, 2100, 2200 et 2300."""


year = int(input("Enter a year: )")

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
           print(f"{year} is leap")
else:
    print("Year is not leap.")