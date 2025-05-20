import pygame
from random import randrange


class Auticko:
    def __init__(self, obrazok, x, y, pohyb, rozmery):
        self.pozicia = [x, y]
        self.pohyb = pohyb
        self.spriteOrig = pygame.image.load(obrazok)
        self.sprite = pygame.image.load(obrazok)
        self.rozmery = rozmery
        self.rect = self.sprite.get_rect(topleft=self.pozicia)

    def dolava(self):
        if self.pozicia[0] > 0:
            self.pozicia[0] -= self.pohyb
            self.sprite = pygame.transform.rotate(self.spriteOrig, 90)

    def doprava(self):
        if self.pozicia[0] < self.rozmery[0] - 100:
            self.pozicia[0] += self.pohyb
            self.sprite = pygame.transform.rotate(self.spriteOrig, -90)

    def hore(self):
        if self.pozicia[1] > 0:
            self.pozicia[1] -= self.pohyb
            self.sprite = pygame.transform.rotate(self.spriteOrig, 0)

    def dole(self):
        if self.pozicia[1] < self.rozmery[1] - 100:
            self.pozicia[1] += self.pohyb
            self.sprite = pygame.transform.rotate(self.spriteOrig, 180)
            
    def update(self):
        self.rect = self.sprite.get_rect(topleft=self.pozicia)


class Protivnik(pygame.sprite.Sprite, Auticko):
    def __init__(self, obrazok, x, y, pohyb, rozmery):
        Auticko.__init__(self, obrazok, x, y, pohyb, rozmery)
        pygame.sprite.Sprite.__init__(self)
        self.smeruje = 0

    def update(self):
        Auticko.update(self)
        if randrange(10) == randrange(10):
            self.smeruje = randrange(5)
        if self.smeruje == 1:
            self.hore()
        elif self.smeruje == 2:
            self.doprava()
        elif self.smeruje == 3:
            self.dole()
        elif self.smeruje == 4:
            self.dolava()
