# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

sana = input("Anna sana: ")
x = input("Monennenko merkin kohdalta haluat katkaista sanan? ")
luku = int(x)  # muutetaan numeroksi

print("Sana:", sana, "on katkaistuna", sana[0:luku])  # leikataan loppu

print("Sinulla on 10 litraa vettä ja kilo hiivaa ja toinen kilo sokeria.")
x = input("Anna hiivan tarkkuuskerroin: ")
kerroin = float(x)
tulos = 10 * 1 * 1 + kerroin / 1.3
tulos = round(tulos,2)
#tehdään lasku ja tulostetaan tulos kahden desimaalin tarkkuudella
print("Kertoimella",kerroin,"valmistuu",tulos,"litraa simaa.")