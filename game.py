import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre du jeu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI Gaming Buddy")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Paramètres du joueur
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 5
jumping = False
velocity_y = 0

# Paramètres du sol du jeu
ground_height = 50
ground_y = SCREEN_HEIGHT - ground_height

# Paramètres de la boucle du jeu on va utiliser pour limiter les FPS surtout
clock = pygame.time.Clock()

def handle_player_movement():
    global player_x, player_y, jumping, velocity_y
    
    keys = pygame.key.get_pressed()
    
    # Déplacement horizontal
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    # Sauter
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            velocity_y = -15
    
    if jumping:
        player_y += velocity_y
        velocity_y += 1  # l'effet de gravité que je veux
        if player_y >= SCREEN_HEIGHT - player_height - ground_height:
            player_y = SCREEN_HEIGHT - player_height - ground_height
            jumping = False

def draw_player():
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

def main():
    global player_x, player_y, jumping, velocity_y
    run_game = True
    while run_game:
        screen.fill(WHITE)

        # Événements du jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        
        handle_player_movement()
        draw_player()
        
        # Dessiner le sol
        pygame.draw.rect(screen, BLACK, (0, ground_y, SCREEN_WIDTH, ground_height))

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
