import pygame

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Andrus")

colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0)]
positions = [65, 150, 235]

working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

    aken.fill((0, 0, 0))
    pygame.draw.rect(aken, (150, 150, 150), (100, 20, 100, 260), 2)

    for color, y in zip(colors, positions):
        pygame.draw.circle(aken, color, (150, y), 38)

    pygame.display.flip()

pygame.quit()