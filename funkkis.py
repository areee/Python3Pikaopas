# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

def funktio(teksti, kerroin):
    for i in range(0, kerroin):
        print(teksti)


merkkijono = input("Anna tekstiä: ")
numero = int(input("Anna numero: "))

funktio(merkkijono, numero)
funktio("LUT", 3)
