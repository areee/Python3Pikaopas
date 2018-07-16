# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

import datetime

# luodaan päiväys

# Tämä päivä kokonaisuudessaan, eli aika sekunteja myöten
nyt = datetime.datetime.now()
print(nyt)

# Tulostetaan päivämäärä ja aika havainnollisemmassa muodossa
nyt2 = nyt.strftime("Tänään pm %d.%m.%Y ja kello näyttää olevan %H:%M.")
print(nyt2)

# Päiviä voi vähentää toisistaan kuten lukuja
syntymapaiva = datetime.date(1989, 5, 30)
print(syntymapaiva)

# Nyt otamme vain päivän käyttöön ilman kellonaikaa
tama_paiva = datetime.date.today()
ika = tama_paiva - syntymapaiva
paivia = ika.days
print(paivia)
