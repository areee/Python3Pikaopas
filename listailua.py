# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

lista = []

while True:
    luku = int(input("Anna positiivinen kokonaisluku (negatiivinen lopettaa): "))
    if luku < 0:
        break
    lista.append(luku)

print("Listassa on seuraavat luvut: ", lista)
lista.sort()
print("Järjestettynä lista on: ", lista)
lista.pop(0)
lista.pop()
print("Ensimmäinen ja viimeinen luku poistettuna: ", lista)
