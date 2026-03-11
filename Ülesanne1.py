import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees - Andrus")

# Värvid
BLACK, WHITE, RED = (0,0,0), (255,255,255), (255,0,0)

def draw_snowman(surf):
    # Lumepallid
    pygame.draw.circle(surf, WHITE, (150,225), 50)
    pygame.draw.circle(surf, WHITE, (150,140), 40)
    pygame.draw.circle(surf, WHITE, (150,75), 30)
    # Silmad
    for x in (140, 160):
        pygame.draw.circle(surf, BLACK, (x,70), 5)
    # Nina
    pygame.draw.polygon(surf, RED, [(145,80),(155,80),(150,95)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_snowman(screen)
    pygame.display.update()

pygame.quit()
