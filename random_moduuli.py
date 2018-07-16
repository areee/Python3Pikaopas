# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

import random

# Satunnainen valinta
hedelma1 = random.choice(['apple', 'pear', 'banana'])
print(hedelma1)

# Satunnainen joukko
joukko = random.sample(range(100), 10)
print(joukko)

# Satunnainen liukuluku väleiltä 0 <= x < 1
liukuluku = random.random()
print(liukuluku)

# Satunnainen kokonaisluku väliltä a <= x <= b
kokonaisluku = random.randint(0, 12)
print(kokonaisluku)
