##################### TAPAHTUMIEN KÄSITTELY #####################

# HUOMIO! Ohjelman ongelmattoman ajamisen varmistamiseksi kopioi kukin koodin osa Testikoodi.py -tiedostoon ja aja se siellä.


# Tähän asti olemme toteuttaneet Pygame-ohjelman pääsilmukan niin, että se käy läpi tapahtumat ja tunnistaa tapahtuman pygame.QUIT, mutta ei käsittele muita tapahtumia. 
# Nyt on aika tutustua tarkemmin tapahtumien käsittelyyn.

# Seuraava koodi näyttää terminaalissa, mitä tapahtumia syntyy ohjelman suorituksen aikana: AJA OHJELMA TESTIKOODI.PY -TIEDOSTOSSA

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

while True:
    for tapahtuma in pygame.event.get():
        print(tapahtuma)
        if tapahtuma.type == pygame.QUIT:
            exit()

# Tapahtumia voi etsiä Pygamen dokumentaatiosta mutta usein tehokas tapa löytää sopiva tapahtuma on käyttää yllä olevaa koodia ja tutkia, 
# millainen tapahtuma syntyy, kun ohjelmassa tapahtuu haluttu asia.


###### NÄPPÄINTAPAHTUMAT ######



# Seuraava ohjelma tunnistaa tapahtumat, joissa käyttäjä painaa oikealle tai vasemmalle nuolinäppäintä. 
# Ohjelma tulostaa testiksi tiedon näppäimen painamisesta:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                print("vasemmalle")
            if tapahtuma.key == pygame.K_RIGHT:
                print("oikealle")

        if tapahtuma.type == pygame.QUIT:
            exit()


# Tässä vakiot pygame.K_LEFT ja pygame.K_RIGHT tarkoittavat nuolinäppäimiä vasemmalle ja oikealle. 
# Näppäimistön eri näppäimiä vastaavat vakiot on listattu Pygamen dokumentaatiossa: https://www.pygame.org/docs/ref/key.html#key-constants-label

# Voimme nyt tehdä ohjelman, jossa käyttäjä pystyy liikuttamaan hahmoa oikealle ja vasemmalle nuolinäppäimillä. Tämä onnistuu seuraavasti:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")
x = 0
y = 480-dog.get_height()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                x -= 10
            if tapahtuma.key == pygame.K_RIGHT:
                x += 10

        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(dog, (x, y))
    pygame.display.flip()


# Tässä muuttujat x ja y sisältävät hahmon sijainnin. 
# Käyttäjä pystyy muuttamaan muuttujaa x, ja muuttuja y on asetettu niin, että hahmo on ikkunan alalaidassa. 
# Kun käyttäjä painaa vasemmalle tai oikealle nuolinäppäintä, hahmo liikkuu vastaavasti 10 pikseliä oikealle tai vasemmalle.

# Yllä oleva ohjelma toimii muuten hyvin, mutta pelikokemuksessa on puutteena, että näppäintä pitää painaa uudestaan aina, kun haluaa liikkua askeleen oikealle tai vasemmalle. 
# Olisi parempi, että voi pitää näppäintä pohjassa ja hahmo liikkuu niin kauan, kuin näppäin on pohjassa. 
# Seuraava koodi mahdollistaa tämän:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")
x = 0
y = 480-dog.get_height()

oikealle = False
vasemmalle = False

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False

        if tapahtuma.type == pygame.QUIT:
            exit()

    if oikealle:
        x += 2
    if vasemmalle:
        x -= 2

    naytto.fill((0, 0, 0))
    naytto.blit(dog, (x, y))
    pygame.display.flip()

    kello.tick(60)


# Koodissa on nyt muuttujat oikealle ja vasemmalle, joissa pidetään tietoa siitä, kuuluuko hahmon liikkua tällä hetkellä oikealle tai vasemmalle. 
# Kun käyttäjä painaa alas nuolinäppäimen, vastaava muuttuja saa arvon True, 
# ja kun käyttäjä nostaa alas nuolinäppäimen, vastaava muuttuja saa arvon False.

# Hahmon liike on tahdistettu kellon avulla niin, että liikkumista tapahtuu 60 kertaa sekunnissa. Jos nuolinäppäin on alhaalla, hahmo liikkuu 2 pikseliä oikealle tai vasemmalle. 
# Tämän seurauksena hahmo liikkuu 120 pikseliä sekunnissa, jos nuolinäppäin on painettuna.


###### HIIRITAPAHTUMAT ######

# Seuraava koodi tunnistaa tapahtumat, jossa käyttäjä painaa hiiren nappia ikkunan alueella:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            print("painoit nappia", tapahtuma.button, "kohdassa", tapahtuma.pos)

        if tapahtuma.type == pygame.QUIT:
            exit()

# Voit kokeilla painella eri painikkeita ja rullata hiiren rullaa nähdäksesi terminaalissa eri tulosteita.
# Tässä nappi 1 tarkoittaa hiiren vasenta nappia ja nappi 3 tarkoittaa hiiren oikeaa nappia.


# Seuraava ohjelma yhdistää hiiren käsittelyn ja kuvan piirtämisen. 
# Kun käyttäjä painaa hiirellä ikkunan alueella, koira piirretään kursorin sijaintiin.

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x = tapahtuma.pos[0]-dog.get_width()/2
            y = tapahtuma.pos[1]-dog.get_height()/2

            naytto.fill((0, 0, 0))
            naytto.blit(dog, (x, y))
            pygame.display.flip()

        if tapahtuma.type == pygame.QUIT:
            exit()


# Seuraava ohjelma puolestaan toteuttaa animaation, jossa koira seuraa kursoria. 
# Koiran sijainti on muuttujissa dog_x ja dog_y, ja kun kursori liikkuu, sen sijainti merkitään muuttujiin kohde_x ja kohde_y. 
# Jos koira ei ole kursorin kohdalla, se liikkuu sopivaan suuntaan.

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

dog_x = 0
dog_y = 0
kohde_x = 0
kohde_y = 0

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            kohde_x = tapahtuma.pos[0]-dog.get_width()/2
            kohde_y = tapahtuma.pos[1]-dog.get_height()/2

        if tapahtuma.type == pygame.QUIT:
            exit(0)

    if dog_x > kohde_x:
        dog_x -= 1
    if dog_x < kohde_x:
        dog_x += 1
    if dog_y > kohde_y:
        dog_y -= 1
    if dog_y < kohde_y:
        dog_y += 1

    naytto.fill((0, 0, 0))
    naytto.blit(dog, (dog_x, dog_y))
    pygame.display.flip()

    kello.tick(60)



####### TEHTÄVÄT ######


# TEHTÄVÄ 1

# Tee ohjelma, jossa pelaaja pystyy ohjaamaan koiraa neljään suuntaan nuolinäppäimillä.
# Tee ohjelma niin, että koira ei pysty menemään ikkunan ulkopuolelle mistään reunasta.

# Vastaus:















# TEHTÄVÄ 2

# Tee ohjelma, jossa kaksi pelaajaa voi ohjata omia koiriaan. Toinen pelaaja käyttää nuolinäppäimiä ja toinen esimerkiksi w-a-s-d.

# Vastaus:















# TEHTÄVÄ 3

# Tee ohjelma, jossa koira seuraa kursoria niin, että koiran keskikohta on aina hiiren kohdalla.

# Vastaus:













# TEHTÄVÄ 4

# Tee ohjelma, jossa koira on satunnaisessa paikassa ikkunassa. 
# Kun pelaaja painaa hiirellä koirasta, se siirtyy aina uuteen satunnaiseen paikkaan.

# Vastaus:










