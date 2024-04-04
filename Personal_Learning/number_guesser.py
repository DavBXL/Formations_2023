import random

while True:
    r = random.randrange(-1, 10)
    user_guess = input("Guess a number between 1 and 9 included: ")
    if user_guess == str(r):
        print()
        print("YOU WON!")
        print("Mine: " + str(r) + " Yours: " + (user_guess))
        print()

    else:
        print()
        print("Not this time!... Try again!")
        print("Mine: " + str(r) + " Yours: " + (user_guess))
        print()