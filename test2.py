import pygame
import math

# Initialize Pygame
pygame.init()

FPS = 60

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HALF_HEIGHT = SCREEN_HEIGHT // 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doom-like Raycasting")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Map (1 = wall, 0 = empty space)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)

# Player settings
player_x = 3.5  # X position in the map grid
player_y = 3.5  # Y position in the map grid
player_angle = 0  # Player's viewing angle
FOV = math.pi / 3  # Field of view (60 degrees)
MOVE_SPEED = 0.05  # Movement speed
ROT_SPEED = 0.03  # Rotation speed

# Raycasting settings
NUM_RAYS = 120  # Number of rays
MAX_DEPTH = 20  # Maximum ray distance
DELTA_ANGLE = FOV / NUM_RAYS  # Angle between each ray
DISTANCE_TO_PROJECTION_PLANE = SCREEN_WIDTH / (2 * math.tan(FOV / 2))
SCALE = SCREEN_WIDTH // NUM_RAYS  # Width of each ray slice


# Raycasting function
def cast_rays():
    rays = []
    for ray in range(NUM_RAYS):
        angle = player_angle - FOV / 2 + ray * DELTA_ANGLE
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        # Step forward in increments to find wall
        for depth in range(MAX_DEPTH * 10):
            depth *= 0.1
            target_x = player_x + cos_a * depth
            target_y = player_y + sin_a * depth

            # Check if the ray hits a wall
            if int(target_x) < MAP_WIDTH and int(target_y) < MAP_HEIGHT:
                if MAP[int(target_y)][int(target_x)] == 1:
                    rays.append((depth, angle))
                    break
    return rays


# Draw 3D walls
def render_3d(rays):
    for ray_index, (depth, angle) in enumerate(rays):
        # Correct the fish-eye effect
        depth *= math.cos(player_angle - angle)

        # Calculate the height of the wall slice
        wall_height = min(SCREEN_HEIGHT, int(DISTANCE_TO_PROJECTION_PLANE / depth))

        # Determine color based on distance
        color_intensity = max(50, 255 - int(255 * (depth / MAX_DEPTH)))
        color = (color_intensity, color_intensity, color_intensity)

        # Calculate the position of the wall slice
        x = ray_index * SCALE
        pygame.draw.rect(screen, color, (x, HALF_HEIGHT - wall_height // 2, SCALE, wall_height))


# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move forward
        player_x += MOVE_SPEED * math.cos(player_angle)
        player_y += MOVE_SPEED * math.sin(player_angle)
    if keys[pygame.K_s]:  # Move backward
        player_x -= MOVE_SPEED * math.cos(player_angle)
        player_y -= MOVE_SPEED * math.sin(player_angle)
    if keys[pygame.K_a]:  # Rotate left
        player_angle -= ROT_SPEED
    if keys[pygame.K_d]:  # Rotate right
        player_angle += ROT_SPEED

    # Prevent player from walking through walls
    if MAP[int(player_y)][int(player_x)] == 1:
        if keys[pygame.K_w]:  # Undo forward movement
            player_x -= MOVE_SPEED * math.cos(player_angle)
            player_y -= MOVE_SPEED * math.sin(player_angle)
        if keys[pygame.K_s]:  # Undo backward movement
            player_x += MOVE_SPEED * math.cos(player_angle)
            player_y += MOVE_SPEED * math.sin(player_angle)

    # Raycasting
    rays = cast_rays()

    # Render 3D walls
    render_3d(rays)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()