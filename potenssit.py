# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

tiedosto_luku = open("numeroita.txt", "r", encoding="utf-8")
tiedosto_kirjoitus = open("potensseja.txt", "w", encoding="utf-8")
while True:
    rivi = tiedosto_luku.readline()
    if len(rivi) == 0:
        break
    luku = int(rivi[:-1])
    potenssi = luku ** 2
    tiedosto_kirjoitus.write(str(potenssi) + "\n")

tiedosto_luku.close()
tiedosto_kirjoitus.close()
