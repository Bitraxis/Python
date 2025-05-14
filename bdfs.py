import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
HALF_HEIGHT = HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Map settings
MAP = [
    "##########",
    "#        #",
    "#  ##    #",
    "#  ##    #",
    "#        #",
    "#    ##  #",
    "#    ##  #",
    "#        #",
    "##########"
]
TILE_SIZE = 64
MAP_WIDTH = len(MAP[0]) * TILE_SIZE
MAP_HEIGHT = len(MAP) * TILE_SIZE

# Player settings
player_x, player_y = TILE_SIZE * 2, TILE_SIZE * 2
player_angle = math.pi / 4
FOV = math.pi / 3
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

def cast_rays():
    """ Raycasting function to detect walls and render them """
    start_angle = player_angle - (FOV / 2)
    for ray in range(NUM_RAYS):
        angle = start_angle + ray * DELTA_ANGLE
        sin_a, cos_a = math.sin(angle), math.cos(angle)

        # Ray distance calculation
        for depth in range(MAX_DEPTH):
            target_x = int(player_x + depth * cos_a)
            target_y = int(player_y + depth * sin_a)

            # Check for wall collision
            if MAP[target_y // TILE_SIZE][target_x // TILE_SIZE] == "#":
                depth *= math.cos(player_angle - angle)  # Fix fisheye effect
                wall_height = min(HEIGHT, TILE_SIZE * 800 / (depth + 0.0001))
                pygame.draw.rect(screen, GRAY, (ray * (WIDTH // NUM_RAYS), HALF_HEIGHT - wall_height // 2, WIDTH // NUM_RAYS, wall_height))
                break

def move_player():
    """ Handle player movement """
    global player_x, player_y, player_angle
    keys = pygame.key.get_pressed()
    speed = 3
    if keys[pygame.K_w]:
        player_x += speed * math.cos(player_angle)
        player_y += speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player_x -= speed * math.cos(player_angle)
        player_y -= speed * math.sin(player_angle)
    if keys[pygame.K_a]:
        player_angle -= 0.05
    if keys[pygame.K_d]:
        player_angle += 0.05

# Game loop
running = True
while running:
    screen.fill(BLACK)
    move_player()
    cast_rays()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
