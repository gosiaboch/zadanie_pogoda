import tkinter as tk
from tkinter import messagebox
import json
from urllib.request import urlopen
import os.path

api_key = "b24e1e1b327c926df045fa69d5aa5d98"

window = tk.Tk()
window.title("Pogoda")

miastoLabel = tk.Label(window, text="Wpisz nazwę miasta")
miastoLabel.pack()

miasto = tk.Entry(window)
miasto.pack()

sciezkaLabel = tk.Label(window, text="Podaj ścieżkę do pliku")
sciezkaLabel.pack()

sciezka = tk.Entry(window)
sciezka.pack()

def sprawdz_pogode():
    response = urlopen("http://api.openweathermap.org/data/2.5/weather?q="+miasto.get()+"&APPID=b24e1e1b327c926df045fa69d5aa5d98")
    dane = json.load(response)
    messagebox.showinfo("Temperatura", dane["main"]["temp_max"])

def sprawdz_dla_pliku():
    if os.path.exists(sciezka.get()):
        with open(sciezka.get(), "r") as plikMiastaDoOdczytu:
            kolekcjaMiast = plikMiastaDoOdczytu.readlines()
        for miast in kolekcjaMiast:
            miast = miast.replace("\n", "")
            response = urlopen("http://api.openweathermap.org/data/2.5/weather?q="+miast+"&APPID=b24e1e1b327c926df045fa69d5aa5d98")
            dane = json.load(response)
            messagebox.showinfo(miast, dane["main"]["temp_max"])


submit = tk.Button(window, text="Sprawdź dla miasta", command = sprawdz_pogode)
submit.pack()

submitZPliku = tk.Button(window, text="Sprawdz pogode dla pliku", command = sprawdz_dla_pliku)
submitZPliku.pack()

window.mainloop()