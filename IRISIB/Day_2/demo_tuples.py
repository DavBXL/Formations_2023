values = (1, 3, 6, 7, 10, 12, 15, 20, 30, 100, 1000)
first_value = values[0]
print(first_value)
last_value = values[-1]
print(values[1])
some_values = values[::-1]
print(some_values)

if 1 in values:
    print("1 est dans values")
if 2 in values:
    print("2 est dans values")

sentence = "Hello world. Today is the second day of April."
if "world" in sentence:
    print("le mot world est présent dans la phrase 'sentence'")