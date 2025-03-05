import pygame

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Circle properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill screen
    screen.fill((30, 30, 30))
    
    # Draw circle
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    
    pygame.display.flip()

pygame.quit()
