import pygame
from sys import exit as sysexit
from auticko import Auticko
pygame.init()

rozmery = (800, 600)
okno = pygame.display.set_mode(rozmery)
FPS = 60
Hra = True

x, y, pohyb = 200,200,5
auto = Auticko("auto.png", x, y, pohyb, rozmery)
auto1 = Auticko("auto.png", x+5, y+5, pohyb+5, rozmery)

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
    if klavesy[pygame.K_w] :
        auto1.hore()
    if klavesy[pygame.K_a] :
        auto1.dolava()
    if klavesy[pygame.K_s] :
        auto1.dole()
    if klavesy[pygame.K_d] :
        auto1.doprava()
    okno.fill((0, 0, 0))
    okno.blit(auto.sprite,auto.pozicia)
    okno.blit(auto1.sprite,auto1.pozicia)
    pygame.display.update()
    hodiny.tick(FPS)
pygame.quit()
