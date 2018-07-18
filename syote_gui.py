from tkinter import *
import sys


def lue():
    teksti = str(Entry.get(kentta))
    tulos = "Kirjoitit: " + teksti
    teksti_ikkuna['text'] = tulos


def lopeta():
    ikkuna.destroy()
    sys.exit(0)


ikkuna = Tk()
ikkuna.title("Lukukone")
ikkuna.geometry("250x100")

ruutu1 = Frame(ikkuna, borderwidth=3)
ruutu1.pack()
ruutu2 = Frame(ruutu1, borderwidth=3)
ruutu2.pack(side=RIGHT)

kentta = Entry(ruutu1)
kentta.pack()

teksti_ikkuna = Label(ruutu1, text="")
teksti_ikkuna.pack()

lue_nappi = Button(ruutu2, text="Lue teksti", width=12, command=lue)
lue_nappi.pack()

lopeta_nappi = Button(ruutu2, text="Lopeta", width=12, command=lopeta)
lopeta_nappi.pack(side=BOTTOM)

ikkuna.mainloop()
