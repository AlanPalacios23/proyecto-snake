import pygame
import random

# -------------------------
# Configuración inicial
# -------------------------
pygame.init()  # Inicializa todos los módulos de pygame

# Dimensiones de la ventana
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20  # Tamaño de cada celda (segmento de la serpiente y comida)

# Colores en formato RGB
WHITE = (255, 255, 255)  
GREEN = (0, 255, 0)      # Serpiente
RED = (255, 0, 0)        # Comida
BLACK = (0, 0, 0)        # Fondo

# Crear ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")  # Título de la ventana

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()


# -------------------------
# Funciones auxiliares
# -------------------------

# Generar una nueva posición aleatoria para la comida
# Siempre múltiplos de GRID_SIZE para que coincida con la cuadrícula
def new_food():
    return [random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]


# -------------------------
# Inicialización de objetos
# -------------------------

# Serpiente: lista de segmentos, cada uno con [x, y]
snake = [[WIDTH // 2, HEIGHT // 2]]  # Empieza en el centro de la pantalla

# Dirección inicial: movimiento hacia la derecha
direction = (GRID_SIZE, 0)

# Colocar la primera comida
food = new_food()


# -------------------------
# Bucle principal del juego
# -------------------------
running = True
while running:
    screen.fill(BLACK)  # Pinta el fondo en negro
    
    # -------------------------
    # Manejo de eventos
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Cerrar ventana
            running = False
        elif event.type == pygame.KEYDOWN:  # Control con teclado
            # Evitar moverse en la dirección opuesta inmediata
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)   # Mover arriba
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)   # Mover abajo
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)  # Mover izquierda
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)   # Mover derecha
    
    # -------------------------
    # Movimiento de la serpiente
    # -------------------------

    # Nueva cabeza (suma la dirección a la cabeza actual)
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    
    # Verificar colisiones
    if (
        new_head in snake                       # Choque consigo misma
        or new_head[0] < 0 or new_head[0] >= WIDTH   # Choque contra pared lateral
        or new_head[1] < 0 or new_head[1] >= HEIGHT  # Choque contra pared superior/inferior
    ):
        running = False  # Termina el juego si hay colisión
    else:
        snake.insert(0, new_head)  # Añade la nueva cabeza
        if new_head == food:       # Si come la comida
            food = new_food()      # Genera nueva comida
        else:
            snake.pop()            # Si no come, elimina la cola (para mantener tamaño)
    
    # -------------------------
    # Dibujar en pantalla
    # -------------------------

    # Dibujar la comida
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))
    
    # Dibujar la serpiente
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Controlar la velocidad del juego (10 FPS)
    clock.tick(10)


# -------------------------
# Salir del juego
# -------------------------
pygame.quit()
