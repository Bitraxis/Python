from random import randrange
import pygame
import sys


pygame.init()
display = pygame.display.set_mode((10, 10))


velkost = 10
priestor = [" "] * velkost
hrac = "X"
okraj = "#"
posLO = velkost // 4
sirka = velkost // 2
posH = velkost // 2
priestor[posLO] = okraj
priestor[posLO + sirka] = okraj
priestor[posH] = hrac
hrame = True
skore = 0

def posunZnaku(pos, posun, znak, delta=0):
    global priestor
    if 0 <= pos + posun < velkost and 0 <= pos + posun + delta < velkost:
        priestor[pos] = " "
        priestor[pos + posun] = znak
        return posun
    return 0


while hrame:
    skore += 1
    hodiny = pygame.time.Clock()
    print("|" + "".join(priestor) + "| " + str(skore))
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_a:
                posH += posunZnaku(posH, -1, hrac)
            if udalost.key == pygame.K_d:
                posH += posunZnaku(posH, 1, hrac)
    zmena = randrange(-1, 2)
    posunZnaku(posLO, zmena, okraj, sirka)
    # priestor[posLO] = " "
    # priestor[posLO + zmena] = okraj
    posLO += posunZnaku(posLO + sirka, zmena, okraj, -sirka)
    # priestor[posLO + sirka] = " "
    # priestor[posLO + sirka + zmena] = okraj
    # posLO += zmena
    if hrac not in priestor:
        print("havaria " + str(skore))
        hrame = False
    hodiny.tick(2)
    
pygame.quit()
