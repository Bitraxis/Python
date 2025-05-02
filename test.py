import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 100, 255)  # Walls
GREEN = (0, 255, 0)  # Floors
YELLOW = (255, 255, 0)  # Stairs
RED = (255, 0, 0)  # Test mode
CYAN = (0, 255, 255)  # Start
MAGENTA = (255, 0, 255)  # End

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Map Creator")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Create a 2D grid
rows = HEIGHT // GRID_SIZE
cols = WIDTH // GRID_SIZE
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Brushes and Tools
current_tool = "brush"  # Options: "brush", "eraser"
current_brush = "wall"  # Options: "wall", "floor", "stairs", "start", "end"

# Map brush types to their respective grid values and colors
BRUSH_TYPES = {
    "wall": {"value": 1, "color": BLUE},
    "floor": {"value": 2, "color": GREEN},
    "stairs": {"value": 3, "color": YELLOW},
    "start": {"value": 4, "color": CYAN},
    "end": {"value": 5, "color": MAGENTA},
}

# Player position
player_x, player_y = None, None  # To be set when "start" tile is placed


# Draw grid
def draw_grid():
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if grid[y][x] == 1:  # Wall
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[y][x] == 2:  # Floor
                pygame.draw.rect(screen, GREEN, rect)
            elif grid[y][x] == 3:  # Stairs
                pygame.draw.rect(screen, YELLOW, rect)
            elif grid[y][x] == 4:  # Start
                pygame.draw.rect(screen, CYAN, rect)
            elif grid[y][x] == 5:  # End
                pygame.draw.rect(screen, MAGENTA, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Draw UI buttons
def draw_ui():
    # Tool buttons
    pygame.draw.rect(screen, WHITE, (10, HEIGHT - 50, 100, 40))  # Brush button
    pygame.draw.rect(screen, WHITE, (120, HEIGHT - 50, 100, 40))  # Eraser button
    pygame.draw.rect(screen, WHITE, (WIDTH - 110, HEIGHT - 50, 100, 40))  # Test button

    # Submenu for brush types
    pygame.draw.rect(screen, WHITE, (10, HEIGHT - 100, 100, 40))  # Wall brush
    pygame.draw.rect(screen, WHITE, (120, HEIGHT - 100, 100, 40))  # Floor brush
    pygame.draw.rect(screen, WHITE, (230, HEIGHT - 100, 100, 40))  # Stairs brush
    pygame.draw.rect(screen, WHITE, (340, HEIGHT - 100, 100, 40))  # Start brush
    pygame.draw.rect(screen, WHITE, (450, HEIGHT - 100, 100, 40))  # End brush

    # Render text
    font = pygame.font.SysFont(None, 24)
    brush_text = font.render("Brush", True, BLACK)
    eraser_text = font.render("Eraser", True, BLACK)
    test_text = font.render("Test", True, BLACK)
    wall_text = font.render("Wall", True, BLACK)
    floor_text = font.render("Floor", True, BLACK)
    stairs_text = font.render("Stairs", True, BLACK)
    start_text = font.render("Start", True, BLACK)
    end_text = font.render("End", True, BLACK)

    # Blit text
    screen.blit(brush_text, (30, HEIGHT - 40))
    screen.blit(eraser_text, (140, HEIGHT - 40))
    screen.blit(test_text, (WIDTH - 90, HEIGHT - 40))
    screen.blit(wall_text, (30, HEIGHT - 90))
    screen.blit(floor_text, (140, HEIGHT - 90))
    screen.blit(stairs_text, (250, HEIGHT - 90))
    screen.blit(start_text, (360, HEIGHT - 90))
    screen.blit(end_text, (470, HEIGHT - 90))

# Test mode: Simulates the map in "Doom-like" style with movement
def play_test_mode():
    global player_x, player_y

    # Ensure there is a start point
    if player_x is None or player_y is None:
        print("Error: Please place a Start tile before testing the map!")
        return

    # Create a test screen
    test_screen = pygame.Surface((cols, rows))
    for y in range(rows):
        for x in range(cols):
            color = BLACK
            if grid[y][x] == 1:  # Wall
                color = BLUE
            elif grid[y][x] == 2:  # Floor
                color = GREEN
            elif grid[y][x] == 3:  # Stairs
                color = YELLOW
            elif grid[y][x] == 5:  # End
                color = MAGENTA
            pygame.draw.rect(test_screen, color, (x, y, 1, 1))

    # Scale up the grid to fullscreen
    stretched_map = pygame.transform.scale(test_screen, (WIDTH, HEIGHT))
    running_test = True
    player_rect = pygame.Rect(player_x * GRID_SIZE, player_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

    while running_test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle player movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w]:  # Move up
            dy = -1
        if keys[pygame.K_s]:  # Move down
            dy = 1
        if keys[pygame.K_a]:  # Move left
            dx = -1
        if keys[pygame.K_d]:  # Move right
            dx = 1

        # Update player position if it's a valid move
        new_x = player_x + dx
        new_y = player_y + dy
        if 0 <= new_x < cols and 0 <= new_y < rows and grid[new_y][new_x] != 1:
            player_x, player_y = new_x, new_y
            player_rect.x, player_rect.y = player_x * GRID_SIZE, player_y * GRID_SIZE

        # Check if the player reached the end
        if grid[player_y][player_x] == 5:
            print("Congratulations! You reached the end!")
            running_test = False

        # Draw the map and player
        screen.blit(stretched_map, (0, 0))
        pygame.draw.rect(screen, CYAN, player_rect)  # Draw player
        pygame.display.flip()
        clock.tick(FPS)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse input
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x // GRID_SIZE
            grid_y = mouse_y // GRID_SIZE
            if grid_x < cols and grid_y < rows:
                if current_tool == "brush":
                    grid[grid_y][grid_x] = BRUSH_TYPES[current_brush]["value"]
                    if current_brush == "start":
                        player_x, player_y = grid_x, grid_y  # Set player starting position
                elif current_tool == "eraser":
                    grid[grid_y][grid_x] = 0  # Erase

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Tool buttons
            if 10 <= mouse_x <= 110 and HEIGHT - 50 <= mouse_y <= HEIGHT:  # Brush button
                current_tool = "brush"
            elif 120 <= mouse_x <= 220 and HEIGHT - 50 <= mouse_y <= HEIGHT:  # Eraser button
                current_tool = "eraser"
            elif WIDTH - 110 <= mouse_x <= WIDTH - 10 and HEIGHT - 50 <= mouse_y <= HEIGHT:  # Test button
                play_test_mode()

            # Brush submenu
            if 10 <= mouse_x <= 110 and HEIGHT - 100 <= mouse_y <= HEIGHT - 60:  # Wall brush
                current_brush = "wall"
            elif 120 <= mouse_x <= 220 and HEIGHT - 100 <= mouse_y <= HEIGHT - 60:  # Floor brush
                current_brush = "floor"
            elif 230 <= mouse_x <= 330 and HEIGHT - 100 <= mouse_y <= HEIGHT - 60:  # Stairs brush
                current_brush = "stairs"
            elif 340 <= mouse_x <= 440 and HEIGHT - 100 <= mouse_y <= HEIGHT - 60:  # Start brush
                current_brush = "start"
            elif 450 <= mouse_x <= 550 and HEIGHT - 100 <= mouse_y <= HEIGHT - 60:  # End brush
                current_brush = "end"

    # Draw the grid and UI
    draw_grid()
    draw_ui()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()