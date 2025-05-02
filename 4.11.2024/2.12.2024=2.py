#letisko
vahamax = float(input("Aká je maximálna váha batožiny (kg): "))
cenakg = float(input("Aká je cena za kg extra (€): "))
vahaa = 1
while vahaa >= 0 :
    vahaa = float(input("Váha batožiny (v kg): "))
    if vahaa > vahamax :
        print("Treba doplatit " + str((vahaa - vahamax)*cenakg) + "€")
    else:
        print("Môžte pokračovať")
    
    
