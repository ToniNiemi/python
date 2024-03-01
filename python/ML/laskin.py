from math import sin
from math import cos

def testeri():
    x = (input('Anna luku: '))  # pyytää lukua käyttäjältä
    while True:
        try:
            int(x)
        except (TypeError, ValueError):
            print('Virheellinen syöte!')
            x = (input('Anna luku: '))  # pyytää lukua käyttäjältä
        else:
            return int(x)


ekaluku = testeri()
tokaluku = testeri()

while True:  # loopataan laskutoimitukset ja valinnat
    print('(1)+ \n(2)- \n(3)* \n(4)/ \n(5)sin(luku1/luku2) \n(6)cos(luku1/luku2) \n(7)Vaihda luvut \n(8)Lopeta \n Valitut luvut ', ekaluku, tokaluku)  # valinta ohjeet
    valinta = input('Tee valinta (1-8): ')
    if valinta == '1':
        vastaus = (ekaluku + tokaluku)  # yhteenlasku
        print('tulos on: ', vastaus)  # vastauksen tulostus

    elif valinta == '2':
        vastaus = (ekaluku - tokaluku)  # vähennyslasku
        print('tulos on: ', vastaus)  # vastauksen tulostus

    elif valinta == '3':
        vastaus = (ekaluku * tokaluku)  # kertolasku
        print('tulos on: ', vastaus)  # vastauksen tulostus

    elif valinta == '4':
        vastaus = (ekaluku / tokaluku)  # jakolasku
        print('tulos on: ', vastaus)  # vastauksen tulostus

    elif valinta == '5':
        vastaus = sin(ekaluku / tokaluku)  # sin
        print('tulos on: ', vastaus)    # vastauksen tulostus

    elif valinta == '6':
        vastaus = cos(ekaluku / tokaluku)  # cos
        print('tulos on: ', vastaus)    # vastauksen tulostus

    elif valinta == '7':
        ekaluku = testeri()     #pyytää uutta lukua käyttäjältä
        tokaluku = testeri()    #pyytää uutta toista lukua käyttäjältä

    elif valinta == '8':
        break

    else:

        print('Valintaa ei tunnistettu.')

