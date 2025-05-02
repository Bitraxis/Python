a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a < b:
    if b > c:
        print(b)
    else:
        print(c)
elif a < c:
    print(c)
elif a > c > b:
    print(a)
else:
    print("Sú rovnaké ")