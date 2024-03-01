# def tulostaja(mjono):
#     if len(mjono) > 4:
#         return mjono
#     else:
#         return "Oletustulostus"
#
#
# def main():
#     mjono = ""
#     while mjono != "Lopeta":
#         mjono = input("Anna syöte (Lopeta lopettaa): ")
#         if mjono == "Lopeta":
#             break
#         print(tulostaja(mjono))
#
#
# if __name__ == "__main__":
#     main()


def pituusmitta(x):
    return len(x)


def main():
    mjono = ""
    while mjono != "Lopeta":
        mjono = input("Anna syöte (Lopeta lopettaa): ")
        if mjono == "Lopeta":
            break
        elif pituusmitta(mjono) < 1:
            print("Et antanut syötettä")

        else:
            print("Antamasi syöte oli", pituusmitta(mjono), "merkkiä pitkä.")

if __name__ == "__main__":
    main()