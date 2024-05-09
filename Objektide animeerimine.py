import pygame, sys, random

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3

# koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(10):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords.append([posX, posY])

gameover = False
while not gameover:
    # fps
    clock.tick(120)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # loendist koordinaadid
    for i in range(len(coords)):
        pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += 1
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0, screenX)
    # koordinaatide loomine ja lisamine massiivi
    coords = []
    for i in range(10):
        posX = random.randint(1, screenX)
        posY = random.randint(1, screenY)
        speed = random.randint(1, 5)
        coords.append([posX, posY, speed])


    # loendist koordinaadid
    for i in range(len(coords)):
        pygame.draw.rect(screen, red, [coords[i][0], coords[i][1], 20, 20])
        coords[i][1] += coords[i][2]
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0, screenX)

    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit()