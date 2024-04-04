print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play :)")

score = 0

answer = input("What does cpu STAND FOR? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    print("Your score: ", str(score))
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Atributed Memory":
    print("Correct!")
    score += 1
    print("Your score: ", str(score))
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "Graphic Processing Unit":
    print("Correct!")
    score += 1
    print("Your score: ", str(score))
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")