import pygame
import random

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

#Load sound
catch_sound = pygame.mixer.Sound("bubble-pop.wav")

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
#BLUE = (0, 0, 255)
#RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

# Load images
player_img = pygame.image.load("DancerRedDress.png")
object_img = pygame.image.load("Rose.png")

# Resize images (optional)
player_img = pygame.transform.scale(player_img, (100, 100))
object_img = pygame.transform.scale(object_img, (30, 30))

# Player setup
#player_width = 100
#player_height = 20
player_x = WIDTH // 2 - 50
player_y = HEIGHT - 100
player_speed = 5

#Falling object setup
#object_width = 30
#object_height = 30
object_x = random.randint(0, WIDTH - 30)
object_y = 0
object_speed = 5

#Score
score = 0
last_checkpoint = 0  # to control difficulty increase

# Clock
clock = pygame.time.Clock()
time_limit = 60  # 60 segundos de jogo
start_ticks = pygame.time.get_ticks()  # marca o tempo de início

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

    #Rects for collision detection
    player_rect = player_img.get_rect(topleft=(player_x, player_y))
    object_rect = object_img.get_rect(topleft=(object_x, object_y))

    #Collision check
    if player_rect.colliderect(object_rect):
        #print("Collision detected")
        # Reset object
        score += 1
        catch_sound.play()  # play the sound

        if score % 5 == 0 and score != last_checkpoint:
            object_speed += 1
            last_checkpoint = score

        object_y = 0
        object_x = random.randint(0, WIDTH - 30)

    #Reset object when it goes off-screen
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH - 30)

    # Draw the player
    screen.blit(player_img, (player_x, player_y))
    screen.blit(object_img, (object_x, object_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Calculate remaining time
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = time_limit - seconds

    # Game ends if time runs out
    if remaining_time <= 0:
        running = False

    # Draw remaining time
    time_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(time_text, (WIDTH - 120, 40))

    # Refresh the screen
    pygame.display.flip()

pygame.quit()
