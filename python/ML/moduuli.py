
def testaa(testattava):
    """Testaa soveltuuko salasanaksi"""
    if len(testattava) < 5 or testattava.isalpha() or testattava.isdigit():
        return False
    else:
        return True


while True:
    testattava = input("Anna testattava sana: ")
    tulos = testaa(testattava)
    if tulos == True:
        print("Antamasi sana kelpaa salasanaksi!")
        break
    else:
        print("Sana ei kelpaa.")

