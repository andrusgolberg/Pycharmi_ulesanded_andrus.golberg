import pygame, sys

#Ekraani mõõtmed ja taustavärv
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BACKGROUND_COLOR = (144, 238, 144)  # heleroheline

#Funktsioon ruudustiku joonistamiseks
def draw_grid(screen, rows=24, cols=32, line_color=(255,0,0)):
    #Arvutame ühe ruudu laiuse ja kõrguse, et kõik ruudud ekraanile mahuks
    square_w, square_h = SCREEN_WIDTH // cols, SCREEN_HEIGHT // rows
    for r in range(rows):
        for c in range(cols):
            #Joonistame iga ruudu äärise
            pygame.draw.rect(screen, line_color, pygame.Rect(c*square_w, r*square_h, square_w, square_h), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Täidetud ruudustik - heleroheline taust")
    clock = pygame.time.Clock()

    #Parameetrid: read, veerud ja joone värv
    rows, cols = 24, 32
    line_color = (255,0,0)  #punased ruudud

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen, rows, cols, line_color)  #Ruudustiku joonistamine
        pygame.display.flip()

        #Kontrollime, kas kasutaja sulges akna
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)  #Kaadrisagedus piiratud 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()