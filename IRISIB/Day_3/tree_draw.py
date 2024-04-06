height = int(input("Size of the tree: "))

for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

print(" " * (height -1) + "|")
