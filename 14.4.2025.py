from sys import exit
from random import randrange as rr
import pygame

pygame.init()

res = xres, yres = 500, 500
display = pygame.display.set_mode(res)


class Player:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def draw(self, surface):
        pygame.draw.rect(
            surface, (rr(256), rr(256), rr(256)), (self.x, self.y, self.a, self.b)
        )

    def move_right(self):
        self.x += 5

    def move_left(self):
        self.x -= 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def inc(self):
        self.a += 10
        self.b += 10

    def dec(self):
        self.a -= 10
        self.b -= 10


player_one = Player(150, 150, 200, 200)

player_two = Player(100, 100, 100, 100)

player_three
## x, y = 150, 150
## a, b = 200, 200

hrame = True
while hrame:
    hodiny = pygame.time.Clock()
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            exit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.unicode == "+":
                player_one.inc()
                player_two.dec()
                # pygame.draw.rect(display, (0, 0, 0), (x, y, a, b))
                ## a += 10
                ## b += 10

            if udalost.unicode == "-":
                player_one.dec()
                player_two.inc()
                # pygame.draw.rect(display, (0, 0, 0), (x, y, a, b))
                ## a -= 10
                ## b -= 10

    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.K_a]:
        player_one.move_left()
        player_two.move_right()
        # pygame.draw.rect(display, (0, 0, 0), (x, y, a, b))
        ## x -= 5

    if klavesy[pygame.K_d]:
        player_one.move_right()
        player_two.move_left()
        # pygame.draw.rect(display, (0, 0, 0), (x, y, a, b))
        ## x += 5

    if klavesy[pygame.K_w]:
        player_one.move_up()
        player_two.move_down()
        
        # pygame.draw.rect(display, (0, 0, 0), (x, y, a, b))
        ## y -= 5

    if klavesy[pygame.K_s]:
        player_one.move_down()
        player_two.move_up()

        # pygame.draw.rect(display, (0, 0, 0), (x, y, a, b))
        ## y += 5

    display.fill((0, 0, 0))
    player_one.draw(display)
    player_two.draw(display)
    ## pygame.draw.rect(display, (rr(256), rr(256), rr(256)), (x, y, a, b))

    pygame.display.update()
    hodiny.tick(60)
pygame.quit()
