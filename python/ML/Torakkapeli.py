###############################################################################
#                                TORAKKA PELI                                 #
###############################################################################
from random import randint


def tietokone():
    """Arpoo kokonaisluvun 1-3 väliltä ja muuttaa sen vastaamaan merkkijonoja"""
    kone = randint(1, 3)
    if kone == 1:
        return 'Jalka'
    elif kone == 2:
        return 'Ydinase'
    else:
        return 'Torakka'


def pelimoottori(pelaaja, kone):
    """vertaillaan merkkijonoja keskenään voittajan selvittämiseksi"""

    if pelaaja == kone:
        return 0  # arvo pakko palauttaa, ettei tule none arvoa

    elif (pelaaja == 'Jalka' and kone == 'Torakka') or (pelaaja == 'Ydinase' and kone == 'Jalka') or (pelaaja == 'Torakka' and kone == 'Ydinase'):
        print('Voitit!')      # voitto argumentit kerätty ehtoihin
        return 1

    elif (pelaaja == 'Jalka' and kone == 'Ydinase') or (pelaaja == 'Torakka' and kone == 'Jalka') or (pelaaja == 'Ydinase' and kone == 'Torakka'):
        print('Hävisit!')     # häviö argumentit kerätty ehtoihin
        return 0


def main():
    i = 0  # kierros laskuri
    tasa = 0  # tasapeli laskuri
    voitto = 0  # voitto laskuri
    jatka = True  # toisto ehto
    while jatka:  # peli looppi
        kone = tietokone()  # kutsutaan tietokone()
        pelaaja = input('Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ')  # kysytään syöte pelaajalta
        if pelaaja == 'Lopeta':
            break  # jos lopetetaan peli

        i = i + 1  # lisätään kierros laskuriin
        print('Sinä valitsit:', pelaaja)  # tulostetaan pelaajan valinta
        print('tietokone valitsi:', kone)  # tulostetaan tietokoneen valinta
        if pelaaja == kone:  # tasapeli tilanne
            print('Tasapeli!')  # tulostus

            tasa += 1  # lisätään tasapeli laskuriin 1 piste

        elif pelimoottori(pelaaja, kone) == 1:  # kysytään pelimoottorilta kumpi voitti
            voitto += 1  # lisätään voitto laskuriin piste

    print('pelasit', i, 'kierrosta, joista voitit', voitto, 'ja pelasit tasan', tasa, 'peliä.')  # loppu tulostus


if __name__ == "__main__":  # kutsutaan main funktio
    main()
