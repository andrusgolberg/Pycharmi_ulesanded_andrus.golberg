import pygame  #impordime pygame

pygame.init()

#Loome 300x300 akna
aken = pygame.display.set_mode((300, 300))

#Pealkiri aknale
pygame.display.set_caption("Foor - Andrus")

working = True

while working:

    #Akna sulgemise kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

    #Taust mustaks
    aken.fill((0, 0, 0))

    #Raam
    pygame.draw.rect(aken, (150, 150, 150), (100, 20, 100, 260), 2)

    #Tuled
    pygame.draw.circle(aken, (255, 0, 0), (150, 65), 38)    # punane
    pygame.draw.circle(aken, (255, 255, 0), (150, 150), 38) # kollane
    pygame.draw.circle(aken, (0, 255, 0), (150, 235), 38)   # roheline

    #Värskendab pildi
    pygame.display.flip()

pygame.quit()