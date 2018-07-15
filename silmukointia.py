# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

while True:
    kerroin = int(input("Anna toistojen lukumäärä (0=lopetus): "))
    if kerroin == 0:
        break
    sana = input("Anna toistettava sana: ")
    for i in range(0,kerroin):
        print(sana)

print("Ohjelman suoritus lopetettu.")