nosnost = int(input("Akú nosnosť má výťah? "))
zvysok = 0
while nosnost > 0:
    clovek = int(input("Akú váhu má človek? "))
    nosnost = nosnost - clovek
    zvysok += 1
print("Do výťahu sa zmestilo " + str(zvysok) + " ľudí")