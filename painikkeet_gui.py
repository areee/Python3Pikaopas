# Alkuperäinen koodi: Jussi Pekka Kasurinen: Python 3 -ohjelmointi

from tkinter import *
import sys


def lopeta():
    ikkuna.destroy()
    sys.exit(0)


def tervehdi():
    teksti_ikkuna['text'] = "No hei vaan sinullekin!"


ikkuna = Tk()
ikkuna.title("Tervehtimiskone")
ikkuna.geometry("225x100")

teksti_ikkuna = Label(ikkuna, text="Tervehtimiskone versio 1")
teksti_ikkuna.pack()

terve_nappi = Button(ikkuna, text="Terve!", command=tervehdi)
terve_nappi.pack()

lopeta_nappi = Button(ikkuna, text="Lopeta", command=lopeta)
lopeta_nappi.pack(side=BOTTOM)

ikkuna.mainloop()
