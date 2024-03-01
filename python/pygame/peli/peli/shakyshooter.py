# Music in the background from https: // www.FesliyanStudios.com
import pygame
from pygame import mixer
from random import randint


def arvopullo():

    arpa = randint(1, 6)
    if arpa == 1:
        pullo_x = 150
        pullo_y = 390

    if arpa == 2:
        pullo_x = 120
        pullo_y = 430

    if arpa == 3:
        pullo_x = 200
        pullo_y = 430

    if arpa == 4:
        pullo_x = 300
        pullo_y = 375

    if arpa == 5:
        pullo_x = 350
        pullo_y = 430

    if arpa == 6:
        pullo_x = 400
        pullo_y = 470


pullo_x = 400
pullo_y = 470


def shaky():
    shaky = randint(-8, 8)
    return shaky


def peli():
    pygame.init()
    pygame.display.set_caption("Shaky Shooter")
    naytto = pygame.display.set_mode((800, 600))

    fontti = pygame.font.SysFont("comicsans", 30)
    osumia_teksti_x = 10
    osumia_teksti_y = 20

    mixer.init()
    bang = mixer.Sound('shot.wav')
    mixer.music.load('taustamus.mp3')
    mixer.music.play()

    ase = pygame.image.load("gun1.png")
    ase_x = 400
    ase_y = 600
    tausta = pygame.image.load("tausta.png")
    tausta = pygame.transform.scale(tausta, (800, 600))
    aita = pygame.image.load("aita.png")
    aita = pygame.transform.scale(aita, (300, 100))
    pullo = arvopullo()
    pullo = pygame.image.load("pullo.png")
    pullo = pygame.transform.scale(pullo, (23, 37))
    hiiri_x = 400
    hiiri_y = 600
    kello = pygame.time.Clock()
    ammuksia = 6
    ammus = pygame.image.load("bullet.png")
    ammus = pygame.transform.scale(ammus, (10, 20))
    # leveys = ammus.get_width()
    time = 200
    while True:
        osuma = 0
        osumia_teksti_sis = fontti.render(
            "osumia: " + str(osuma), True, (0, 0, 0))
        ammuksia_teksti_sis = fontti.render(
            "Ammuksia: " + str(ammuksia), True, (0, 0, 0))
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEMOTION:
                hiiri_x = tapahtuma.pos[0]-ase.get_width()/2-25
                hiiri_y = tapahtuma.pos[1]-0
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                if ammuksia > 0:
                    laukausx = tapahtuma.pos[0]-ase.get_width()/2-25
                    laukausy = tapahtuma.pos[1] - \
                        ase.get_height() - ase.get_height()
                    bang.play()
                    ammuksia = ammuksia - 1
                    if (laukausx > pullo_x and laukausx < pullo_x + pullo.get_width()) and (laukausy > pullo_y and laukausy < pullo_y + pullo.get_height()):
                        osuma = osuma + 1
                        arvopullo()
                        naytto.blit(pullo, (pullo_x, pullo_y))
                    else:
                        pass
            if tapahtuma.type == pygame.QUIT:
                exit()

        if ase_x > hiiri_x:
            ase_x -= 1
        if ase_x < hiiri_x:
            ase_x += 1
        if ase_y > hiiri_y:
            ase_y -= 1
        if ase_y < hiiri_y:
            ase_y += 1

        naytto.blit(tausta, (0, 0))
        naytto.blit(pullo, (pullo_x, pullo_y))
        naytto.blit(aita, (100, 400))
        naytto.blit(ammus, (600, 550))
        naytto.blit(ase, (ase_x + shaky(), ase_y + shaky()))
        naytto.blit(ammuksia_teksti_sis, (600, 550))
        naytto.blit(osumia_teksti_sis, (osumia_teksti_x, osumia_teksti_y))
        pygame.display.flip()
        kello.tick(60)


peli()
