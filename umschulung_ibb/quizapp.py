import tkinter as tk
from tkinter import ttk
import random
from time import sleep
import json


FragList = open("umschulung_ibb/standard_fragen.json", "r")
FragList = json.load(FragList)


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
            self, textvar=self.Antwort0text, variable=self.Auswahl, value=0)
        self.Antwort[0].pack()

        self.Antwort[1] = ttk.Radiobutton(
            self, textvar=self.Antwort1text, variable=self.Auswahl, value=1)
        self.Antwort[1].pack()

        self.Antwort[2] = ttk.Radiobutton(
            self, textvar=self.Antwort2text, variable=self.Auswahl, value=2)
        self.Antwort[2].pack()

        self.Antwort[3] = ttk.Radiobutton(
            self, textvar=self.Antwort3text, variable=self.Auswahl, value=3)
        self.Antwort[3].pack()
        self.Enter = ttk.Button(self, text="Abschicken",
                                command=self.ErgebnisPrüfen,
                                style="Abschicken.TButton")
        self.Enter.pack(pady=20)

        self.Fragenpool = set()
        self.Highscore = set()
        i = 0
        while i < len(FragList):
            self.Fragenpool.add(i)
            i += 1
        self.Beantwortetpool = set()

        self.FragenAufrufen()

    def FragenAufrufen(self):

        self.Antwort[0].config(style="Antwort.TButton")
        self.Antwort[1].config(style="Antwort.TButton")
        self.Antwort[2].config(style="Antwort.TButton")
        self.Antwort[3].config(style="Antwort.TButton")
        self.update_idletasks()

        self.index = random.choice(
            list(self.Fragenpool - self.Beantwortetpool))
        self.Beantwortetpool.add(self.index)

        self.Fragenfeld.tag_configure("fragentext", justify='center')

        self.Fragenfeld.delete(1.0, tk.END)

        self.Fragenfeld.insert(tk.END, FragList[self.index]["Frage"])

        self.Fragenfeld.tag_add("fragentext", "1.0", "end")

        self.Antwliste = []
        self.Antwliste = [FragList[self.index]["RichtigeAntwort"],
                          FragList[self.index]["FalscheAntwort1"],
                          FragList[self.index]["FalscheAntwort2"],
                          FragList[self.index]["FalscheAntwort3"]]
        random.shuffle(self.Antwliste)
        self.Antwort0text.set(self.Antwliste[0])
        self.Antwort1text.set(self.Antwliste[1])
        self.Antwort2text.set(self.Antwliste[2])
        self.Antwort3text.set(self.Antwliste[3])
        self.update_idletasks()

    def ErgebnisPrüfen(self):

        Ergebnis = self.Auswahl.get()

        if self.Antwliste[Ergebnis] == FragList[self.index]["RichtigeAntwort"]:

            self.Antwort[Ergebnis].config(style="RichtigeAntwort.TButton")
            self.Highscore.add(True)
        else:

            self.Antwort[Ergebnis].config(style="FalscheAntwort.TButton")
            self.Highscore.add(False)

        self.update_idletasks()
        sleep(2)
        self.FragenAufrufen()


Fenster = QuizApp()
Fenster.mainloop()
