################### ANIMAATIO PYGAME-KIRJASTON AVULLA ###################

# HUOMIO! Ohjelman ongelmattoman ajamisen varmistamiseksi kopioi kukin koodin osa Testikoodi.py -tiedostoon ja aja se siellä.


# Monissa peleissä on tarvetta saada aikaan liikkuvia hahmoja, joten seuraava luonteva askel on opetella animaation tekeminen. 
# Animaatio syntyy, kun kuva piirretään eri kohtiin näytöllä sopivasti ajastettuna.


# Seuraava koodi luo animaation, jossa koira kulkee vasemmalta oikealle ikkunassa:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

# Katsotaan taas tarkemmin, mitä ohjelmassa tapahtuu. Jotta kuva pystyy liikkumaan, ohjelmassa täytyy olla tieto sen paikasta. 
# Tämä onnistuu ottamalla käyttöön kaksi muuttujaa, jotka sisältävät kuvan vasemman yläkulman koordinaatit eli x ja y
x = 0
y = 0

# Tämän lisäksi määritellään kello, jonka avulla pystyy huolehtimaan siitä, että animaation nopeus on sopiva.
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(dog, (x, y))
    pygame.display.flip()

    x += 1
    kello.tick(60)



# Pääsilmukan sisällä on koodi, joka piirtää kuvan sen nykyiseen paikkaan.

# Ensin kutsutaan metodia fill, joka tyhjentää ikkunan mustalla värillä. 
# Väri määritellään RGB-muodossa parametrilla (0, 0, 0), mikä tarkoittaa, että värin punainen, vihreä ja sininen komponentti on 0 eli väri on musta. 
# Jokainen komponentti voi olla välillä 0–255. Esimerkiksi (255, 255, 255) on valkoinen ja (255, 0, 0) on punainen. 

# Tämän jälkeen kuva piirretään tuttuun tapaan metodilla blit ja lopuksi ikkunan sisältö päivitetään funktiolla pygame.display.flip.
# Silmukan päätteeksi muuttujan x arvo kasvaa, minkä ansiosta kuva liikkuu pikselin eteenpäin joka kierroksella.

# Lisäksi silmukan lopussa suoritetaan kellon metodi tick().
# Metodi tick huolehtii siitä, että animaation nopeus on sopiva: se tahdistaa silmukan niin, että silmukka pyritään suorittamaan 60 kertaa sekunnissa. 
# Toisin sanoen kuva liikkuu sekunnissa 60 pikseliä oikealle. 
# Tämä vastaa suunnilleen pelien yhteydessä käytettävää termiä FPS (frames per second).

# Metodi tick on hyödyllinen, koska sen avulla animaatio toimii periaatteessa yhtä nopeasti jokaisella koneella. 
# Jos silmukassa ei olisi tällaista ajastusta, pelin nopeus riippuisi siitä, kuinka nopeasti pelaajan kone toimii.

### TÖRMÄÄMINEN ###

# Äskeinen animaatio on muuten hieno, mutta kun koira etenee ikkunan ulkopuolelle, animaatio jatkuu ja koira katoaa näkyvistä. 
# Tehdään seuraavaksi ohjelmaan parannus, jonka avulla koiran suunta muuttuu, jos se törmää seinään:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

x = 0
y = 0
nopeus = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(dog, (x, y))
    pygame.display.flip()
    
    x += nopeus
    if nopeus > 0 and x+dog.get_width() >= 640:
        nopeus = -nopeus
    if nopeus < 0 and x <= 0:
        nopeus = -nopeus

    kello.tick(60)

# Nyt ohjelmassa on uusi muuttuja nopeus, joka määrittää koiran liikkumistavan. 
# Positiivinen nopeus tarkoittaa liikkumista oikealle ja negatiivinen nopeus tarkoittaa liikkumista vasemmalle. 
# Tässä tapauksessa kun nopeus on 1, koira liikkuu oikealle, ja kun nopeus on –1, koira liikkuu vasemmalle.

# Jos nopeus on positiivinen eli koira liikkuu oikealle ja sen oikea reuna menee ikkunan oikean reunan ulkopuolelle, koiran suunta muuttuu käänteiseksi eli se alkaa liikkua vasemmalle. 
# Vastaavasti jos nopeus on negatiivinen ja koiran vasen reuna menee ikkunan vasemman reunan ulkopuolelle, suunta muuttuu taas käänteiseksi eli koira alkaa liikkua oikealle.

# Tämän koodin ansiosta koira jatkaa loputtomasti rataa, jossa se liikkuu ensin koko ikkunan verran oikealle, sitten takaisin vasemmalle, sitten taas oikealle, jne.


# Tehdään vielä animaatio, jossa koira pyörii ikkunan keskipisteen ympärillä:

import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

dog = pygame.image.load("dog.png")

kulma = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    x = 320+math.cos(kulma)*100-dog.get_width()/2
    y = 240+math.sin(kulma)*100-dog.get_height()/2

    naytto.fill((0, 0, 0))
    naytto.blit(dog, (x, y))
    pygame.display.flip()

    kulma += 0.01
    kello.tick(60)


# Pyörimisanimaatio saadaan toteutettua trigonometrian avulla: muuttujassa kulma on radiaaneina koiran sijainnin kulma suhteessa ikkunan keskipisteeseen. 
# Tästä saadaan laskettua sini- ja kosinifunktioilla koiran sijainti

# Tämä tarkoittaa, että koiran sijainti on ympyrällä, jonka säde on 100. Kosini antaa x-suuntaisen sijainnin ja sini puolestaan y-suuntaisen sijainnin. 
# Jotta animaatio näyttää hyvältä, koira lisäksi keskitetään niin, että sen keskipiste on ympyrällä.

# Joka kierroksella muuttujan kulma arvo kasvaa 0.01:llä. 
# Koska radiaaneissa täysi ympyrä on 2π eli noin 6.28, koira pyörii suunnilleen kierroksen verran 10 sekunnissa.



####### TEHTÄVÄT ######


# TEHTÄVÄ 1

# Tee animaatio, jossa koira liikkuu vuorotellen ylös ja alas. Koira ei mene ikkunan ulkopuolelle

# Vastaus:











# TEHTÄVÄ 2

# Tee animaatio, jossa koira kiertää ympäri ikkunan reunaa.

# Vastaus:















# TEHTÄVÄ 3

# Tee animaatio, jossa kaksi koiraa kulkee näytöllä vuorotellen oikealle ja vasemmalle eri tasoissa. Alempi koira kulkee tuplavauhtia.

# Vastaus:














