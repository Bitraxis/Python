import random as rd

pocetNul = 20
ukoncenie = 100
nuly = ["0"] * pocetNul
ideme = True
while ideme:
    print(", ".join(nuly))
    pos = rd.randrange(pocetNul)
    nuly[pos] = str(int(nuly[pos]) + 1)
    if int(nuly[pos]) == ukoncenie:
        print("vyhrala pozicia " + str(pos))
        ideme = False
