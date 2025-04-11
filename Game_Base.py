import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player setup
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 5

#Falling object setup
object_width = 30
object_height = 30
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    #Move falling object
    object_y += object_speed

    #Reset object when it goes off-screen
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH - object_width)

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Refresh the screen
    pygame.display.flip()

pygame.quit()
