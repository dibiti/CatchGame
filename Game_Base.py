import pygame

# Inicializar pygame
pygame.init()

# Definir o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Base")

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Jogador
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 5

# Clock
clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Desenhar jogador
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Atualizar o ecrã
    pygame.display.flip()

pygame.quit()
