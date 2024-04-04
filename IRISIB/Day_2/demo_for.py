sentence = "hello world!"
letters = []
for variable in sentence:
    print(variable)
    letters.append(variable)
print(letters)

scores = [12, 20, 8, 4, 16]
scores_in_percent = []
for score in scores:
    scores_in_percent.append(score*5)
print(scores_in_percent)
print()
for value in (10, 100, 20, 200):
    print(value)
print()
values = (10, 100, 20, 200)
for value in values:
    print(value)
print()
for value in range(3, 22, 3):
    print(value)