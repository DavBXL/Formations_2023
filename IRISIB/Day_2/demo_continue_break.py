for number in range(0, 101, 5):
    if number % 10 == 0:  # Signifie que number est multiple de 10
        continue
    print(number)
    print("ok")
    print("c'est bien")
print()
for number in range(10):
    print(number)
    if number == 5:
        break

scores = [10, 20, 8, None]
remarks = []
for score in scores:
    if score == 20:
        remarks.append("Perfect")
        continue
    print(f"The student got {score}")
    remark = input("Enter a remark for the student : ")
    remarks.append(remark)
print(remarks)
print("end of script.")
