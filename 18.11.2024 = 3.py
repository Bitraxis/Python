a = float(input("a: "))
b = float(input("b: "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
