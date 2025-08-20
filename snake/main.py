import pygame
import random

# Configuración inicial
pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Función para generar nueva posición de comida
def new_food():
    return [random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]

# Inicialización de la serpiente
snake = [[WIDTH // 2, HEIGHT // 2]]
direction = (GRID_SIZE, 0)
food = new_food()

running = True
while running:
    screen.fill(BLACK)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)
    
    # Mover la serpiente
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    
    # Verificar colisiones
    if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    else:
        snake.insert(0, new_head)
        if new_head == food:
            food = new_food()
        else:
            snake.pop()
    
    # Dibujar comida y serpiente
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
