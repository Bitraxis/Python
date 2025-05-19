import pygame
from random import randrange
class Auticko():
    def __init__(ja, obrazok, x, y, pohyb, rozmery):
        ja.pozicia = [x,y]
        ja.pohyb = pohyb
        ja.spriteOrig = pygame.image.load(obrazok)
        ja.sprite = pygame.image.load(obrazok)
        ja.rozmery = rozmery
        
    def dolava(ja):
        if ja.pozicia[0] > 0:
            ja.pozicia[0] -= ja.pohyb
            ja.sprite = pygame.transform.rotate(ja.spriteOrig, 90)
    def doprava(ja):
        if ja.pozicia[0] < ja.rozmery[0] - 100:
            ja.pozicia[0] += ja.pohyb
            ja.sprite = pygame.transform.rotate(ja.spriteOrig, -90)
    def hore(ja):
        if ja.pozicia[1] > 0:
            ja.pozicia[1] -= ja.pohyb
            ja.sprite = pygame.transform.rotate(ja.spriteOrig, 0)
    def dole(ja):
        if ja.pozicia[1] < ja.rozmery[1] - 100:
            ja.pozicia[1] += ja.pohyb
            ja.sprite = pygame.transform.rotate(ja.spriteOrig, 180)
            
class Protivnik(Auticko):
    def __init__(ja, obrazok, x, y, pohyb, rozmery):
        super().__init__(obrazok, x, y, pohyb, rozmery)
        ja.smeruje = 0
    def update(ja):
        if randrange(10) == randrange(10):
            ja.smeruje = randrange(5)
        if ja.smeruje == 1:
            ja.hore()
        elif ja.smeruje == 2:
            ja.doprava()
        elif ja.smeruje == 3:
            ja.dole()
        elif ja.smeruje == 4:
            ja.dolava()
            