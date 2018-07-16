# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

import urllib.request
sivu = urllib.request.urlopen("http://www.it.lut.fi/")
sisalto = sivu.read() # luetaan sivun sisältö
sivu.close()
tekstina = sisalto.decode("utf-8") # parsitaan merkistö oikeanlaiseksi
print(tekstina)