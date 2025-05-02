# Učiteľ na telesnej si zapisuje skoky do diaľky a zisťuje kto skočil najďalej
skok = float(input("Ako rýchlo dokončil 100m beh: "))
naj = skok
poradieZiaka = 1
vitaz = 1
while skok > 0 :
    if skok < naj :
        naj = skok
        vitaz = poradieZiaka
    poradieZiaka += 1
    skok = float(input("Ako rýchlo dokončil 100m beh: "))
print("Žiak číslo " + str(vitaz) + " je vitaz" + " zo rýchlosťou " + str(naj) + "s")