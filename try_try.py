# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

import sys

try:
    tiedosto_kahva = open("tiedosto.txt", "r", encoding="utf-8")
    try:
        rivi = tiedosto_kahva.readline()
        if len(rivi) == 0:
            print("Tiedosto on tyhjä!")
        else:
            rivi_muuttuja = rivi[:-1]  # Määritetään asetus_vipu
    except IOError:
        print("Tiedostosta lukeminen epäonnistui.")
        sys.exit(-2)
    finally:
        tiedosto_kahva.close()  # Suljetaan onnistuneesti avattu tiedosto
except IOError:
    print("Tiedoston avaaminen epäonnistui.")
    sys.exit(-1)

print("Tiedosto-operaatiot suoritettu onnistuneesti.")
print("Kiitos ohjelman käytöstä.")
