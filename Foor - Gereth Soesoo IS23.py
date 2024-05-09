import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Gereth Soesoo")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKROUND = (153, 255, 153)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BACKROUND)

    # Create a pygame.Rect object
    rect = pygame.Rect(130, 15, 60, 150)
    
    pygame.draw.rect(screen, BLUE, (145, 250, 30, 20))
    pygame.draw.rect(screen, BLACK, (145, 270, 30, 20))
    pygame.draw.rect(screen, WHITE, (145, 290, 30, 20))

    pygame.draw.rect(screen, GRAY, rect, 2)
    pygame.draw.circle(screen, RED, (160, 50), 20)
    pygame.draw.circle(screen, YELLOW, (160, 90), 20)
    pygame.draw.circle(screen, GREEN, (160, 130), 20)
    pygame.draw.line(screen, GRAY, (160, 165), (160, 250), 2)
    pygame.draw.line(screen, GRAY, (160, 250), (180, 290), 2)
    pygame.draw.line(screen, GRAY, (160, 250), (140, 290), 2)
    pygame.draw.line(screen, GRAY, (140, 290), (180, 290), 2)

    
    # Update the display
    pygame.display.flip()

pygame.quit()