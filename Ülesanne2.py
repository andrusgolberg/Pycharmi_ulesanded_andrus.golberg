import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 2")

#Pildid
background = pygame.image.load("bg_shop.png")
seller = pygame.transform.scale(pygame.image.load("seller.png"), (255, 310))
chat = pygame.transform.scale(pygame.image.load("chat.png"), (250, 200))

#Font ja tekst
font = pygame.font.SysFont("arial", 20)
text = font.render("Tere, olen Andrus Golberg", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(seller, (105, 154))
    screen.blit(chat, (245, 65))
    screen.blit(text, (280, 125))

    pygame.display.update()

pygame.quit()
sys.exit()