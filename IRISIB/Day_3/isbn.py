# Demandez à l'user de rentrer un ISBN, puis vérifiez si celui-ci est valide ou non
# ISBN valide : 3-598-21507-X
# On présuppose que l'user entre un "bon" ISBN : comprendre un ISBN de 10 caractères
# qui sont tous des chiffres sauf le dernier qui peut être un chiffre ou un X majuscule

# isbn = input("Enter ISBN to verify : ")
isbn = "3598215078"

digits = []
for digit in isbn[:-1]:
    digits.append(int(digit))
if isbn[-1] == "X":
    digits.append(10)
else:
    digits.append(int(isbn[-1]))

# (d1x10 + d2x9 + ... + d9x2 + d10x1) % 11 == 0
# version 1
counter = 0
sum_ = 0
for digit in digits:
    # sum_ = sum_ + digit*counter
    sum_ += digit*counter
    counter -= 1

if sum_ % 11 == 0:
    print(f"{isbn} is a valid ISBN")
else:
    print(f"{isbn} is NOT a valid ISBN")

# Version 2
# weights = range(10, 0, -1)
# sum_ = 0
# for digit, weight in zip(digits, weights):
#     sum_ += digit * weight
# if sum_ % 11 == 0:
#     print(f"{isbn} is a valid ISBN")
# else:
#     print(f"{isbn} is NOT a valid ISBN")

# Version 3
# weights = range(10, 0, -1)
# products = []
# for digit, weight in zip(digits, weights):
#     products.append(digit * weight)
# if sum(products) % 11 == 0:
#     print(f"{isbn} is a valid ISBN")
# else:
#     print(f"{isbn} is NOT a valid ISBN")

# Version 4
# sum_ = 0
# for weight, digit in enumerate(reversed(digits), start=1):
#     sum_ += weight * digit
# if sum_ % 11 == 0:
#     print(f"{isbn} is a valid ISBN")
# else:
#     print(f"{isbn} is NOT a valid ISBN")

# Version 3+ : list comprehension
# products = []
# for digit, weight in zip(digits, weights):
#     products.append(digit * weight)
# if sum([digit * weight for digit, weight in zip(digits, range(10, 0, -1))]) % 11 == 0:
#     print(f"{isbn} is a valid ISBN")
# else:
#     print(f"{isbn} is NOT a valid ISBN")
