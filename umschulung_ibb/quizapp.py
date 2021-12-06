import tkinter as tk
from tkinter import ttk
import random
from time import sleep
import json


FragenListe = open("umschulung_ibb/standard_fragen.json", "r")
FragenListe = json.load(FragenListe)


class QuizApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        theme = ttk.Style()
        theme.theme_use('default')

        theme.configure("Antwort.TButton", font='helvetica 20')
        theme.configure("FalscheAntwort.TButton",
                        font='helvetica 20', foreground='red')
        theme.configure("RichtigeAntwort.TButton",
                        font='helvetica 20', foreground='green')
        theme.configure("Abschicken.TButton", font='helvetica 16')

        self.title("QuizApp")
        self.Überschrift = ttk.Label(self, text="Willkommen in der QuizApp")
        self.Überschrift.pack()

        self.Fragenfeld = tk.Text(
            self, height=2, width=50, font='helvetica 20')
        self.Fragenfeld.pack()

        self.Auswahl = tk.IntVar()
        self.Antwort0text = tk.StringVar()
        self.Antwort1text = tk.StringVar()
        self.Antwort2text = tk.StringVar()
        self.Antwort3text = tk.StringVar()

        self.Antwort = ["", "", "", ""]
        self.Antwort[0] = ttk.Radiobutton(
            self, textvariable=self.Antwort0text, variable=self.Auswahl, value=0)
        self.Antwort[0].pack()

        self.Antwort[1] = ttk.Radiobutton(
            self, textvariable=self.Antwort1text, variable=self.Auswahl, value=1)
        self.Antwort[1].pack()

        self.Antwort[2] = ttk.Radiobutton(
            self, textvariable=self.Antwort2text, variable=self.Auswahl, value=2)
        self.Antwort[2].pack()

        self.Antwort[3] = ttk.Radiobutton(
            self, textvariable=self.Antwort3text, variable=self.Auswahl, value=3)
        self.Antwort[3].pack()
        self.Enter = ttk.Button(self, text="Abschicken",
                                command=self.ErgebnisPrüfen, style="Abschicken.TButton")
        self.Enter.pack(pady=20)

        self.FragenAufrufen()

    def FragenAufrufen(self):

        self.Antwort[0].config(style="Antwort.TButton")
        self.Antwort[1].config(style="Antwort.TButton")
        self.Antwort[2].config(style="Antwort.TButton")
        self.Antwort[3].config(style="Antwort.TButton")
        self.update_idletasks()
        self.index = random.randint(0, len(FragenListe) - 1)

        self.Fragenfeld.tag_configure("fragentext", justify='center')

        self.Fragenfeld.delete(1.0, tk.END)
        self.Fragenfeld.insert(tk.END, FragenListe[self.index]["Frage"])

        self.Fragenfeld.tag_add("fragentext", "1.0", "end")

        self.Antwortenliste = [FragenListe[self.index]["RichtigeAntwort"], FragenListe[self.index]["FalscheAntwort1"],
                               FragenListe[self.index]["FalscheAntwort2"], FragenListe[self.index]["FalscheAntwort3"]]
        random.shuffle(self.Antwortenliste)
        self.Antwort0text.set(self.Antwortenliste[0])
        self.Antwort1text.set(self.Antwortenliste[1])
        self.Antwort2text.set(self.Antwortenliste[2])
        self.Antwort3text.set(self.Antwortenliste[3])
        self.update_idletasks()

    def ErgebnisPrüfen(self):

        Ergebnis = self.Auswahl.get()

        if self.Antwortenliste[Ergebnis] == FragenListe[self.index]["RichtigeAntwort"]:

            self.Antwort[Ergebnis].config(style="RichtigeAntwort.TButton")

        else:

            self.Antwort[Ergebnis].config(style="FalscheAntwort.TButton")

        self.update_idletasks()
        sleep(2)
        self.FragenAufrufen()


Fenster = QuizApp()
Fenster.mainloop()
