"""
Tento program si vypyta rodne cislo
potom zobere cisla na parnych poziciach
spocita ich
potom zobere cisla na neparnych poziciach
spocita ich a vymoduluje ich o 11
a potom skontroluje podla standardu ci je este
vtedy platne
"""

rc = input("Rodne cislo: ")
rok = rc[0:2]
mesiac = rc[2:4]
den = rc[4:6]
neparne = rc[::2]
neparne = neparne.replace("/", "")
neparne = list(neparne)
parne = rc[1::2]
parne = parne.replace("/", "")
parne = list(parne)
b = 0
b1 = 0
c = 0
c1 = 0
for parnecislo in range(len(parne)):
    a = parne[b]
    c += int(a)
    b += 1
for neparnecislo in range(len(neparne)):
    a1 = parne[b1]
    c1 += int(a1)
    b1 += 1
if c % 11 == 0:
    if c1 % 11 == 0:
        print("Existuje")
        skutocne = True
    else:
        skutocne = False
        print("Neexistuje")
else:
    print("Neexistuje")
    skutocne = False
pocty_dni = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if skutocne == True:
    if int(rok) >= 54:
        rc = rc.split("/")
        rc = "".join(rc)
        if len(rc) != 10:
            print("Neexistuje")
        else:
            skutocne = True
            if int(mesiac) > 12:
                mesiac_cislo = int(mesiac) - 50
            else:
                mesiac_cislo = int(mesiac)
            if mesiac_cislo > 12:
                skutocne = False
            elif mesiac_cislo < 1:
                skutocne_cislo = False
            elif pocty_dni[int(mesiac) - 1] < int(den):
                skutocne = False
            if skutocne == True:
                if int(mesiac) > 50:
                    print("zena")
                else:
                    print("muz")
                if int(rok) <= 7:
                    print("Nad 18")
                elif int(rok) >= 26:
                    print("Nad 18")
                else:
                    print("Pod 18")
            else:
                print("Neplatne cislo")
    elif int(rok) <= 26:
        rc = rc.split("/")
        rc = "".join(rc)
        if len(rc) != 10:
            print("Neexistuje")
        else:
            skutocne = True
            if int(mesiac) > 12:
                mesiac_cislo = int(mesiac) - 50
            else:
                mesiac_cislo = int(mesiac)
            if mesiac_cislo > 12:
                skutocne = False
            elif mesiac_cislo < 1:
                skutocne_cislo = False
            elif pocty_dni[int(mesiac) - 1] < int(den):
                skutocne = False
            if skutocne == True:
                if int(mesiac) > 50:
                    print("zena")
                else:
                    print("muz")
                if int(rok) <= 7:
                    print("Nad 18")
                elif int(rok) >= 26:
                    print("Nad 18")
                else:
                    print("Pod 18")
            else:
                print("Neplatne cislo")
    else:
        rc = rc.split("/")
        rc = "".join(rc)
        if len(rc) != 9:
            print("Neexistuje")
        else:
            skutocne = True
            if int(mesiac) > 12:
                mesiac_cislo = int(mesiac) - 50
            else:
                mesiac_cislo = int(mesiac)
            if mesiac_cislo > 12:
                skutocne = False
            elif mesiac_cislo < 1:
                skutocne_cislo = False
            elif pocty_dni[int(mesiac) - 1] < int(den):
                skutocne = False
            if skutocne == True:
                if int(mesiac) > 50:
                    print("zena")
                else:
                    print("muz")
                if int(rok) <= 7:
                    print("Nad 18")
                elif int(rok) >= 26:
                    print("Nad 18")
                else:
                    print("Pod 18")
            else:
                print("Neplatne cislo")
else:
    print("Rodne cislo neni platne")
