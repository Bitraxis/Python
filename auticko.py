import pygame
class Auticko():
    def __init__(ja, obrazok, x, y, pohyb, rozmery):
        ja.pozicia = [x,y]
        ja.pohyb = pohyb
        ja.sprite = pygame.image.load(obrazok)
        ja.rozmery = rozmery
        
    def dolava(ja):
        if ja.pozicia[0] > 0:
            ja.pozicia[0] -= ja.pohyb
    def doprava(ja):
        if ja.pozicia[0] < ja.rozmery[0] - 100:
            ja.pozicia[0] += ja.pohyb
    def hore(ja):
        if ja.pozicia[1] > 0:
            ja.pozicia[1] += ja.pohyb
    def dole(ja):
        if ja.pozicia[1] < ja.rozmery[1] - 100:
            ja.pozicia[1] -= ja.pohyb