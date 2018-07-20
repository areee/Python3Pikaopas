from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
from tkinter import *
import sys


def avaa():
    nimi = filedialog.askopenfilename()
    tiedosto = open(nimi, 'r')
    sisalto = tiedosto.read()
    tiedosto.close()
    teksti_ikkuna['text'] = sisalto


def sulje():
    if messagebox.askyesno("Sulje", "Suljetaanko?"):
        teksti_ikkuna['text'] = ""


def lopeta():
    messagebox.showinfo("Lopetetaan", "Lopetetaan ohjelma")
    ikkuna.destroy()
    sys.exit(0)


ikkuna = Tk()
valikko = Menu(ikkuna)
ikkuna.title("Lukuohjelma")
ikkuna.geometry("350x200")
ikkuna.config(menu=valikko)

valinnat = Menu(valikko)
valikko.add_cascade(label="Tiedosto", menu=valinnat)

valinnat.add_command(label="Avaa", command=avaa)
valinnat.add_command(label="Sulje", command=sulje)
valinnat.add_separator()
valinnat.add_command(label="Lopeta", command=lopeta)

ruutu1 = Frame(ikkuna, borderwidth=3)
ruutu1.pack()

teksti_ikkuna = Label(ruutu1, text="Valitse luettava tiedosto")
teksti_ikkuna.pack()

ikkuna.mainloop()
