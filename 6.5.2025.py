import pygame
from sys import exit as sysexit
from auticko import Auticko,Protivnik
from random import randrange
pygame.init()

rozmery = (800, 600)
okno = pygame.display.set_mode(rozmery)
FPS = 60
Hra = True

x, y, rychlost = 200,200,5
auto = Auticko("auto.png", x, y, rychlost, rozmery)
auto2 = Protivnik("auto.png", x*2, y*2, rychlost+2, rozmery)
pohyb = 0
while Hra:
    hodiny = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sysexit()
    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.K_LEFT] :
        auto.dolava()
    if klavesy[pygame.K_RIGHT] :
        auto.doprava()
    if klavesy[pygame.K_DOWN] :
        auto.dole()
    if klavesy[pygame.K_UP] :
        auto.hore()
    auto2.update()
    okno.fill((0, 0, 0))
    okno.blit(auto.sprite,auto.pozicia)
    okno.blit(auto2.sprite,auto2.pozicia)
    pygame.display.update()
    hodiny.tick(FPS)
pygame.quit()
