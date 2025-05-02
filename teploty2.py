pocet_dni = 0
suma_rano = 0
suma_obed = 0
suma_vecer = 0
with open("teploty2.txt", "r") as vstup:
    for den in vstup:
        hodnoty = den.split()
        pocet_dni += 1
        suma_rano += int(hodnoty[0])
        suma_obed += int(hodnoty[1])
        suma_vecer += int(hodnoty[2])
print("Priemerné teploty za " + str(pocet_dni) + " dní")
print("Ráno: " + str(suma_rano / pocet_dni) + "°C")
print("Obed: " + str(suma_obed / pocet_dni) + "°C")
print("Večer: " + str(suma_vecer / pocet_dni) + "°C")
