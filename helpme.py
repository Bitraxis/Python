import random as rd

dlzky = []
a = 0
pocet = 0
rozsah = int(input("Daj rozsah: "))
for opakovanie in range(100):
    body = []
    aktualne = rd.randrange(rozsah)
    while aktualne not in body:
        body.append(aktualne)
        aktualne = rd.randrange(rozsah)
    dlzky.append(len(body))
print("Priemerna dlzka je: " + str(sum(dlzky) / len(dlzky)))
