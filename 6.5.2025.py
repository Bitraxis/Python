import pygame
from sys import exit as sysexit
from auticko import Auticko,Protivnik

pygame.init()

rozmery = (800, 600)
okno = pygame.display.set_mode(rozmery)
FPS = 60
Hra = True

x, y, rychlost,zmena = 200,200,5,2
auto = Auticko("auto.png", x, y, rychlost, rozmery)
auta = pygame.sprite.Group()
for i in range(5):
    auta.add(Protivnik("auto.png", x*zmena, y*zmena, rychlost+zmena, rozmery))
    zmena += 1
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
    auta.update()
    okno.fill((0, 0, 0))
    okno.blit(auto.sprite,auto.pozicia)
    for auto2 in auta:
        okno.blit(auto2.sprite,auto2.pozicia)
    pygame.display.update()
    hodiny.tick(FPS)
pygame.quit()