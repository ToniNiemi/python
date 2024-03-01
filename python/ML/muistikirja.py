import time
import pickle
t = (time.strftime("%X %x"))



def tallenna(list):
    tiedosto = open('muistio.txt', 'wb')
    pickle.dump(list, tiedosto)
    tiedosto.close()

def lue():
    try:
        tiedosto = open('muistio.txt', 'rb')
        list = pickle.load(tiedosto)
        tiedosto.close()
    except (IOError, FileNotFoundError):
        print('Virhe tiedostossa, luodaan uusi muistio.dat.')
        list = []
        tiedosto = open('muistio.txt', 'wb')
        pickle.dump(list, tiedosto)
        tiedosto.close()
    else:
        return list


def main():
    valinta = 0
    list = []
    lue()
    while True:
        try:
            valinta = int(input('(1) Lue muistikirjaa \n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta\n\n Mitä haluat tehdä: '))
        except ValueError:
            print('anna valinta lukuna! ')

        if valinta == 1:
            for i in list:
                print(i)

        elif valinta == 2:
            # lisää
            item = input('Kirjoita uusi merkintä: ')
            item = (item + ' ::: ' + t)
            list.append(item)

        elif valinta == 3:
            #muokkaa
            print('Listalla on ', len(list), 'merkintää.')
            try:
                kohta = int(input('Mitä niistä muutetaan?: ')) - 1
            except IndexError:
                print('luku pitää kuulua listaan')
            print(list[kohta])
            muutettu = input('Anna uusi teksti:')
            list[kohta] = (muutettu + ' ::: ' + t)

        elif valinta == 4:
            # poista
            print('Listalla on ', len(list), 'merkintää.')
            try:
                kohta = int(input('Mitä niistä poistetaan?: ')) - 1
            except IndexError:
                print('luku pitää kuulua listaan')
            print('Poistettiin merkintä ', list[kohta])
            list.pop(kohta)

        elif valinta == 5:
            # tallenna lopeta
            tallenna(list)
            break

        else:
            print('virheellinen valinta')

if __name__ == "__main__":  # kutsutaan main funktio
    main()