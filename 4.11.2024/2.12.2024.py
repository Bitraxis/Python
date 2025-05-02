print("auto vo for")
for auto in range(5, 50, 4):
    print(auto)
print("kvety vo for")
for kvety in range(15):
    print(kvety)
print("kvety vo while")
kvety = 0
while kvety < 15 :
    print(kvety)
    kvety += 1
print("teplota for")
for teplota in range(36, 4, -1):
    print(teplota)
print("teplota while")
teplota = 36
while teplota > 4:
    print(teplota)
    teplota -= 1
print("Ascii")
for cisloZnaku in range(22,106):
    print(str(cisloZnaku) + " " + chr(cisloZnaku))
print("vypisanie malych pismen")
for cisloZnaku in range(65,123):
    print(str(cisloZnaku) + " " + chr(cisloZnaku))
print("premenna zo string")
text = input("zadaj text: ")
for premenna in text:
    print(ord(premenna), end=" ")
