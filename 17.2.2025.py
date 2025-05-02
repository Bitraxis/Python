subor = open("cisla.txt", "w")

pocet = subor.write("Ahoj svet" + "\n")
pocet += subor.write(str(42))
print("zapis:" + str(pocet))
subor.close()

with open("cisla.txt", "w") as f:
    for cislo in range(11):
        zapisanych = f.write(str(cislo) + "\n")
        print("zapisanych:", str(zapisanych))
vstup = open("cisla.txt", "r")
for riadok in vstup:
    riadok = riadok.strip()
    print(riadok)
