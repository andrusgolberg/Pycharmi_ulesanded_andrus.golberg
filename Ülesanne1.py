# vajalik selleks, et üldse seda teha
import pygame

# korrektseks lõpetuseks vajalik
import pygame

pygame.init()

width = 300

height = 300

screen = pygame.display.set_mode((width, height))

# määrame akna pealkirja (programmi nimi ja sinu nimi)
pygame.display.set_caption("Lumemees - Andrus")

# defineerime värvid
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# muutuja mis hoiab programmi töös
running = True

# peamine programmitsükkel
while running:

    # vaatame läbi kõik pygame sündmused
    for event in pygame.event.get():

        # kontrollime kas kasutaja vajutas akna sulgemise nuppu
        if event.type == pygame.QUIT:

            # kui vajutati X, lõpetame programmi
            running = False

    # värvime kogu akna mustaks (taust)
    screen.fill(black)

    # joonistame lumepallid alt üles
    pygame.draw.circle(screen, white, (150, 225), 50)
    pygame.draw.circle(screen, white, (150, 140), 40)
    pygame.draw.circle(screen, white, (150, 75), 30)

    # joonistame silmad vasakult paremale
    pygame.draw.circle(screen, black, (140, 70), 5)
    pygame.draw.circle(screen, black, (160, 70), 5)

    # joonistame nina
    pygame.draw.polygon(screen, red, [(145,80), (155,80), (150,95)])

    # uuendame ekraani, et joonistatud asjad oleks nähtavad
    pygame.display.update()

# sulgeme pygame süsteemi
pygame.quit()
