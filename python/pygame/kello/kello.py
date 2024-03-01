# analoginen kello
import datetime
import math
import pygame

pygame.init()
pygame.display.set_caption("kello")
naytto = pygame.display.set_mode((640, 640))

# valitse värit RGB
sininen = (0, 0, 255)
punainen = (255, 0, 0)


def muuta_koordinaatisto(säde, kulma):
    """_summary_

    Args:
        säde (integer): ympyrän säde
        kulma (integer): kulma asteina

    Returns:
        x, y:  y = math.cos(2 * math.pi * kulma/360) * säde, x = math.sin(2 * math.pi * kulma/360) * säde
    """
    
    y = math.cos(2 * math.pi * kulma/360) * säde
    x = math.sin(2 * math.pi * kulma/360) * säde
    return x+320, -(y-320)


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))

    aika_nyt = datetime.datetime.now()
    tunnit = aika_nyt.hour
    minuutit = aika_nyt.minute
    sekunnit = aika_nyt.second

    # kellontaulu ja keskipiste
    pygame.draw.circle(naytto, punainen, (320, 320), 320, 4)
    pygame.draw.circle(naytto, punainen, (320, 320), 6)

    # sekuntti viisari
    säde = 310
    kulma = sekunnit * (360/60)
    paksuus = 3
    pygame.draw.line(naytto, sininen, (320, 320),
                     muuta_koordinaatisto(säde, kulma), paksuus)
    # minuuttitti viisari
    säde = 300
    kulma = (minuutit+sekunnit/60) * (360/60)
    paksuus = 8
    pygame.draw.line(naytto, sininen, (320, 320),
                     muuta_koordinaatisto(säde, kulma), paksuus)
    # sekuntti viisari
    säde = 280
    kulma = (tunnit + minuutit/60 + sekunnit/3600) * (360/12)
    paksuus = 12
    pygame.draw.line(naytto, sininen, (320, 320),
                     muuta_koordinaatisto(säde, kulma), paksuus)

    pygame.display.flip()
