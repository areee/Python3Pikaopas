from tkinter import *
import sys


def avaa():
    teksti_ikkuna['text'] = "Valitsit avaa"


def sulje():
    teksti_ikkuna['text'] = "Valitsit sulje"


def lopeta():
    ikkuna.destroy()
    sys.exit(0)


ikkuna = Tk()
valikko = Menu(ikkuna)
ikkuna.title("Valikko-ohjelma")
ikkuna.geometry("250x100")
ikkuna.config(menu=valikko)

valinnat = Menu(valikko)
valikko.add_cascade(label="Tiedosto", menu=valinnat)
valinnat.add_command(label="Avaa", command=avaa)
valinnat.add_command(label="Sulje", command=sulje)
valinnat.add_separator()
valinnat.add_command(label="Lopeta", command=lopeta)

ruutu1 = Frame(ikkuna, borderwidth=3)
ruutu1.pack()

teksti_ikkuna = Label(ruutu1, text="Valitse jotain")
teksti_ikkuna.pack()

ikkuna.mainloop()
