# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

# Kysytään käyttäjältä kolme syötettä ja muutetaan ne kokonaisluvuiksi
luku1 = int(input("Anna 1. luku: "))
luku2 = int(input("Anna 2. luku: "))
luku3 = int(input("Anna 3. luku: "))

if luku1 == luku2:
    print("Luvut 1 ja 2 ovat samoja.")

if luku1 == luku2 and luku2 == luku3:
    print("Kaikki luvut ovat samoja.")

# Ratkotaan luvuista suurin, tasatilanteessakin tulostetaan jokin vaihtoehto
if luku1 < luku2:
    if luku2 < luku3:
        print("Luku 3 on suurin.")
    else:
        print("Luku 2 on suurin.")
else:
    if luku1 < luku3:
        print("Luku 3 on suurin,")
    else:
        print("Luku 1 on suurin.")