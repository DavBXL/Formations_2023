scores = [12, 5, 8, 16]
marks = scores
student_scores = scores.copy()
student_scores.append(20)
marks.append(17)
print(scores)
print(student_scores)
print(id(student_scores))
print(id(scores))
print(id(marks))
if type(marks) == list:
    print("marks est une liste")