number = 0
while number < 10:
    print(f"number = {number}")
    number += 1
print("we exited the while loop")

score = float(input("Enter a student score between 0 and 20 : "))

while not (0 <= score <= 20):
    score = float(input("PLEASE enter a student score between 0 and 20 : "))

print(f"you entered {score}")