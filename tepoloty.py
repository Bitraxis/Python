dni = 0
najvyssia_teplota = -274
with open("teploty.txt", "r") as teploty:
    for riadok in teploty:
        riadok = riadok.strip()
        print(riadok + "°C")
        riadok = int(riadok)
        dni += 1
        if riadok >= najvyssia_teplota:
            najvyssia_teplota = riadok
            den = dni
        else:
            continue
print("Meralo sa " + str(dni) + " dní")
print(
    "Najvyššia teplota bola "
    + str(den)
    + " deň a bola "
    + str(najvyssia_teplota)
    + "°C"
)

""" "Michálikovo" (ChatGPT) riešenie
with open("teploty.txt", "r") as subor:
    teploty = [float(riadok.strip()) for riadok in subor]
pocetDni = len(teploty)
print("Počet dní s meraním teploty: " + str(pocetDni))
 
najvyssiaTeplota = max(teploty)
najvyssiDen = teploty.index(najvyssiaTeplota) + 1
print("Najvyššia teplota bola " + str(najvyssiaTeplota) + "na den cislo " + str(najvyssiDen))
"""
