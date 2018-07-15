# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

ohje = input("Mikä ohje tämä on? ")
x = input("Kuinka monta desiä vettä? ")
vesi = int(x)
x = input("Kuinka monta grammaa hiivaa? ")
hiiva = int(x)
# Huomaa, että seuraavassa input() on laitettu suoraan int():n sisään.
jauho = int(input("Kuinka monta desiä jauhoja? "))

print(ohje)
print("=========")
print("Vettä:       ", vesi, "dl")
print("Hiivaa:      ", hiiva, "g")
print("Vehnäjauhoja:", jauho, "dl")