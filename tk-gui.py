# Alkuperäinen koodi: Erno Vanhala ja Uolevi Nikula: Python 3 – ohjelmointiopas, versio 1.1
# Creative Commons Nimi mainittava-Ei kaupalliseen käyttöön-Sama lisenssi 2.5 -lisenssi

from tkinter import *


class Laskin():
    luku1 = ""
    luku2 = ""
    vastaus = ""

    def __init__(self):
        pohja = Tk()
        pohja.title('Laskin')
        Label(pohja, text='1. luku').pack()
        self.luku1 = Entry(pohja)
        self.luku1.pack()
        Label(pohja, text='2. luku').pack()
        self.luku2 = Entry(pohja)
        self.luku2.pack()
        Label(pohja, text='Vastaus').pack()
        self.vastaus = Entry(pohja)
        self.vastaus.pack()
        Button(pohja, text='Summaa', command=self.summaa).pack()

    def summaa(self):
        eka = float(self.luku1.get())
        toka = float(self.luku2.get())
        summa = eka + toka
        self.vastaus.delete(0, END)
        self.vastaus.insert(0, str(summa))


kalkulaattori = Laskin()
