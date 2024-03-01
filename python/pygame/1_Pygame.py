####################### PYGAME #######################

# Pygame on peliohjelmointiin tarkoitettu Python-kirjasto.
# Pygamen avulla pystyy piirtämään grafiikkaa, käsittelemään näppäimistön ja hiiren tapahtumia ja tekemään muuta peleissä tarvittavaa.

# Pygame-kirjaston asennusohjeet löytyvät Learn-alustalta.
# Asenna Pygame-kirjasto ennen materiaalissa etenemistä

# Ohjelman ongelmattoman ajamisen varmistamiseksi kopioi kukin koodin osa Testikoodi.py -tiedostoon ja aja se siellä.


###### ENSIMMÄINEN OHJELMA ######

# Tässä on yksinkertainen Pygamea käyttävä testiohjelma:

import pygame
"""
pygame.init()
naytto = pygame.display.set_mode((640, 480))

naytto.fill((0,0,0))
pygame.display.flip()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

"""

# Kun ohjelma käynnistetään, se näyttää käyttäjälle tyhjän ikkunan
# Ohjelman suoritus jatkuu niin kauan, kunnes käyttäjä sulkee ikkunan.


# Ohjelman alussa rivi import pygame ottaa mukaan Pygame-kirjaston.
# Kirjaston käyttäminen alkaa kutsumalla funktiota pygame.init, minkä jälkeen ohjelma luo ikkunan funktiolla pygame.display.set_mode.

# Muuttujan naytto kautta ikkunaan voidaan viitata myöhemmin esimerkiksi grafiikan piirtämistä varten.
# Parametri (640, 480) tarkoittaa, että tässä ohjelmassa ikkunan leveys on 640 pikseliä ja korkeus on 480 pikseliä.

# Metodi fill täyttää näytön annetulla värillä. Tässä tapauksessa värinä on (0, 0, 0), mikä tarkoittaa mustaa.
# Sitten metodi pygame.display.flip päivittää näytön sisällön.

# Pääsilmukka käsittelee tapahtumat, jotka käyttöjärjestelmä välittää ohjelmalle.
# Joka kierroksella funktio pygame.event.get antaa listan tapahtumista, jotka ovat syntyneet funktion edellisen kutsukerran jälkeen.

# Tässä tapauksessa ohjelma käsittelee vain tyyppiä pygame.QUIT olevat tapahtumat.
# ällainen tapahtuma syntyy, kun käyttäjä sulkee ohjelman esimerkiksi painamalla ikkunan ylänurkassa olevaa raksia.
# Tämän tapahtuman seurauksena ohjelma sulkee itsensä kutsumalla exit-funktiota.

# Voit kokeilla, mitä tapahtuu, jos ohjelma ei käsittele tapahtumaa pygame.QUIT. Tällöin raksin painamisen ei pitäisi vaikuttaa ohjelman toimintaan, mikä on hämmentävää käyttäjälle.
# Ohjelman voi kuitenkin tässäkin tapauksessa sulkea väkisin komentoriviltä painamalla Control+C.


###### KUVA IKKUNAAN ######


# Laajennetaan seuraavaksi ohjelmaa niin, että se näyttää ikkunassa kuvan.
# Ohjelman ajamiseksi kommentoi ylempänä oleva koodi ennen testaamista tai kopioi alla oleva koodi Testikoodi.py-tiedostoon ja aja se.
"""
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

naytto.fill((0, 0, 0))
naytto.blit(dog, (100, 50))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
"""

# Tiedoston dog.png tulee olla samassa hakemistossa ohjelman lähdekoodin kanssa, jotta ohjelma löytää kuvan.

# Tässä funktio pygame.image.load lataa muuttujaan tiedostossa dog.png olevan kuvan.
# Tämän jälkeen metodi blit piirtää kuvan ikkunaan kohtaan (100, 50) ja sitten funktio pygame.display.flip päivittää ikkunan sisällön.
# Kohta (100, 50) tarkoittaa, että kuvan vasen yläkulma on kyseisessä kohdassa.

# Huomaa, että Pygamessa ja yleensä muutenkin ohjelmoinnissa koordinaatisto on rakennettu niin,
# että piirtoalueen vasen yläkulma on kohdassa (0, 0) ja koordinaatit kasvavat x-suunnassa oikealle ja y-suunnassa alaspäin.
# Tässä tapauksessa ikkunan oikean alakulman koordinaatit ovat (640, 480).

# Kuvan voi piirtää moneenkin kohtaan ikkunassa. Esimerkiksi seuraava koodi piirtää kuvan kolmeen eri kohtaan:


pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

naytto.fill((0, 0, 0))
naytto.blit(dog, (0, 0))
naytto.blit(dog, (300, 0))
naytto.blit(dog, (100, 200))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()


# Seuraava koodi puolestaan piirtää kuvan ikkunan keskelle:


pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

naytto.fill((0, 0, 0))
leveys = dog.get_width()
korkeus = dog.get_height()
naytto.blit(dog, (320-leveys/2, 240-korkeus/2))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

# Tässä metodi get_width antaa kuvan leveyden ja vastaavasti metodi get_height antaa kuvan korkeuden. Ikkunan keskikohta on (320, 240),
# joten tämän avulla saadaan laskettua sopiva kohta kuvan vasemmalle yläkulmalle niin, että kuva sijoittuu ikkunan keskelle.


####### TEHTÄVÄT ######


# TEHTÄVÄ 1

# Tee ohjelma, joka piirtää koiran jokaiseen ikkunan neljään nurkkaan.

# Vastaus:


# TEHTÄVÄ 2

# Tee ohjelma, joka piirtää kymmenen koiraa riviin.

# Vastaus:


# TEHTÄVÄ 3

# Tee ohjelma, joka piirtää tuhat koiraa satunnaisiin paikkoihin.

# Vastaus:
