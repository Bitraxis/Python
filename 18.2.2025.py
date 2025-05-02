cisla = [8, 6, 7, 5, 9, 4]
a = 0
for priemer in cisla:
    a += priemer
priemer = a // len(cisla)
for vacsie in range(len(cisla)):
    if priemer < cisla[vacsie]:
        print("Vacsie su: " + str(cisla[vacsie]))
