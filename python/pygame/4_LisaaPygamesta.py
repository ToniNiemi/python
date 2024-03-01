##################### LISÄÄ PYGAMESTA #####################

# HUOMIO! Ohjelman ongelmattoman ajamisen varmistamiseksi kopioi kukin koodin osa Testikoodi.py -tiedostoon ja aja se siellä.


###### IKKUNAN OTSIKKO ######

# Ohjelma näyttää ammattimaisemmalta, jos ikkunan otsikkopalkissa ei lue "pygame window" vaan ohjelman todellinen nimi. 
# Tämä onnistuu metodilla pygame.display.set_caption("Nimi tähän")


###### KUVIOIDEN PIIRTÄMINEN ######

# Seuraava ohjelma luo kuvan, jossa on suorakulmio, ympyrä ja viiva:

import pygame

pygame.init()
pygame.display.set_caption("Kuvioita")
naytto = pygame.display.set_mode((640, 480))
naytto.fill((0, 0, 0))

pygame.draw.rect(naytto, (0, 255, 0), (50, 100, 200, 250))
pygame.draw.circle(naytto, (255, 0, 0), (200, 150), 40)
pygame.draw.line(naytto, (0, 0, 255), (80, 120), (300, 160), 2)

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()


###### TEKSTIN PIIRTÄMINEN ######

# Tekstin piirtäminen tapahtuu Pygame-kirjastossa niin, että ensin luodaan tekstiä vastaava kuva ja sen jälkeen piirretään kuva näytölle. 
# Seuraava ohjelma esittelee asiaa:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
naytto.fill((0, 0, 0))

fontti = pygame.font.SysFont("Arial", 24)
teksti = fontti.render("Moikka!", True, (255, 0, 0))
naytto.blit(teksti, (100, 50))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

# Tässä metodi pygame.font.SysFont luo fonttiolion, joka käyttää järjestelmän fonttia Arial kokona 24. 
# Tämän jälkeen olion metodi render luo kuvan, jossa lukee teksti "Moikka!" punaisella värillä, ja tämä kuva piirretään ikkunaan.

# Huomaa, että eri järjestelmissä on saatavilla eri fontit. Jos järjestelmässä ei ole fonttia Arial (mikä tosin on yleinen fontti), yllä oleva koodi käyttää sen sijasta järjestelmän oletusfonttia. 
# Toinen mahdollisuus on käyttää metodia pygame.font.Font, jolle annetaan hakemistossa olevan fonttitiedoston nimi.


###### TEHTÄVÄ ######


# Tee ohjelma, joka näyttää graafisesti kellonajan. 
# Ohjelman suorituksen tulee näyttää tältä: https://ohjelmointi-21.mooc.fi/0e95a9664e02d0dd939be3ebfd4725d5/pygame_kello.gif


# Vastaus:


















