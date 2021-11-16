#!/usr/bin/env python3
# -*- coding: UTF-8 -*- 
#######################################################################################
#
#
#               A small programm to work with classes and GUI
#
#               by Jens Zorn
#
#               -
#
#
#
#<°))))><
#######################################################################################
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys

#from Hotel_Gaeste import *
#from Hotel import *


class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(hotel.hotelname + " Zimmerbelegung und Buchung")

        mainwindow = tk.Frame(self)
        mainwindow.grid(row=0, column=0, sticky=N+S+E+W)
        self.frames = {}
        for F in (rootwindow, guestpage):
            frame_name = F.__name__
            frame = F(parent=mainwindow)
            self.frames[frame_name] = frame
            frame.grid(sticky=N+S+E+W)

        self.upper_menu_bar()
        self.show_frame("rootwindow")
        self.update_idletasks() 
        self.window_width= frame.winfo_width()
        self.statusbar()
        
    def upper_menu_bar(self):
        self.menubar = tk.Menu(self, bd=1, relief=tk.RAISED)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Exit", command=quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.config(menu=self.menubar)

    def statusbar(self):
        self.img = tk.PhotoImage() # zero size image
        self.statusbar = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.statusbar.grid(row = 1, column = 0, sticky="ws")
        self.statusbar_label = tk.Label(self.statusbar, width=self.window_width, height=15, text="Statusbar", image=self.img, compound=tk.CENTER, anchor=tk.W)
        self.statusbar_label.grid(row=0, column=0)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def quit(self):
        self.shutdown()
        sys.exit()

class rootwindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)

        #Versuch einer Scrollbar
        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=1, column=1, rowspan=5, padx=5, pady=5)

        #Zimmerliste links
        self.zimmerliste = Listbox(self, width=30, height=20, selectmode=SINGLE, yscrollcommand=self.scrollbar.set)
        self.zimmerliste.grid(row=1, column=0, rowspan=5, padx=5, pady=5)
        i=1
        for zimmer in hotel.zimmerauflistung:
            self.zimmerliste.insert(i, "Zimmernr. " + str(zimmer.zimmernummer) + ", Status: " + zimmer.status)
            i+=1
        self.zimmerliste.bind('<<ListboxSelect>>', self.show_detail)

        #Zimmerdetails
        ttk.Label(self, text = "Zimmernr: ").grid(row = 1, column = 2)
        self.zimmernr_entry = ttk.Entry(self, width=20)
        self.zimmernr_entry.grid(row = 1, column = 3)
        ttk.Label(self, text = "Status: ").grid(row = 2, column = 2)
        self.status_entry = ttk.Entry(self, width=20)
        self.status_entry.grid(row = 2, column = 3)
        ttk.Label(self, text = "Gast: ").grid(row = 3, column = 2)
        self.gast_entry = ttk.Entry(self, width=20)
        self.gast_entry.grid(row = 3, column = 3)

        #Gastdetails
        self.checkin_gastname_entry = ttk.Entry(self, width=20)
        self.checkin_gastname_entry.grid(row = 6, column = 0)
        self.checkin_geburtsdatum_entry = ttk.Entry(self, width=20)
        self.checkin_geburtsdatum_entry.grid(row = 6, column = 3)
        self.checkin_anreise_entry = ttk.Entry(self, width=20)
        self.checkin_anreise_entry.grid(row = 7, column = 0)
        self.checkin_abreise_entry = ttk.Entry(self, width=20)
        self.checkin_abreise_entry.grid(row = 7, column = 3)
        self.checkin_zimmernr_entry = ttk.Entry(self, width=20)
        self.checkin_zimmernr_entry.grid(row = 8, column = 0)
        self.button_send = ttk.Button(self, text="CHECKIN",command=lambda: self.checkin()).grid(row = 8, column = 1)
        self.button_send = ttk.Button(self, text="CHECKOUT",command=lambda: self.checkout()).grid(row = 8, column = 3)
        self.button_quit = ttk.Button(self, text="QUIT", command=quit).grid(row = 8, column = 4)

    def show_detail(self, selection):
        try:
            self.selection = selection.widget
            self.selectindex = self.selection.curselection()[0]
            self.selection = self.selection.get(self.selectindex)
        except:
            pass
        try:
            self.selectindex = int(selection)
        except:
            pass
        print (str(self.selection) + str(self.selectindex))
        self.zimmernr_entry.delete(0, "end")
        self.status_entry.delete(0, "end")
        self.gast_entry.delete(0, "end")
        self.checkin_gastname_entry.delete(0, "end")
        self.checkin_geburtsdatum_entry.delete(0, "end")
        self.checkin_anreise_entry.delete(0, "end")
        self.checkin_abreise_entry.delete(0, "end")
        self.checkin_zimmernr_entry.delete(0, "end")
        self.zimmernr_entry.insert(0, hotel.zimmerauflistung[self.selectindex].zimmernummer)
        self.status_entry.insert(0, hotel.zimmerauflistung[self.selectindex].status)
        self.gast_entry.insert(0, hotel.zimmerauflistung[self.selectindex].gast)
        self.checkin_gastname_entry.insert(0, hotel.zimmerauflistung[self.selectindex].gast)
        #self.checkin_geburtsdatum_entry.insert(1, hotel.zimmerauflistung[self.selectindex].geburtsdatum)
        self.checkin_anreise_entry.insert(0, hotel.zimmerauflistung[self.selectindex].anreise)
        self.checkin_abreise_entry.insert(0, hotel.zimmerauflistung[self.selectindex].abreise)
        self.checkin_zimmernr_entry.insert(0, hotel.zimmerauflistung[self.selectindex].zimmernummer)

    def checkin(self):
        self.geburtsdatuminsert = self.checkin_geburtsdatum_entry.get()
        self.zimmernrinsert = int(self.checkin_zimmernr_entry.get())
        hotel.zimmerauflistung[self.zimmernrinsert].zimmernummer = self.zimmernrinsert
        hotel.zimmerauflistung[self.zimmernrinsert].status = "Besetzt"
        hotel.zimmerauflistung[self.zimmernrinsert].gast = self.checkin_gastname_entry.get()
        hotel.zimmerauflistung[self.zimmernrinsert].anreise = self.checkin_anreise_entry.get()
        hotel.zimmerauflistung[self.zimmernrinsert].abreise = self.checkin_abreise_entry.get()
        self.zimmerliste.delete(self.zimmernrinsert)
        self.zimmerliste.insert(self.zimmernrinsert, "Zimmernr. " + str(self.zimmernrinsert) + ", Status: " + hotel.zimmerauflistung[self.zimmernrinsert].status)
        self.show_detail(self.zimmernrinsert)

    def checkout(self):
        self.geburtsdatuminsert = self.checkin_geburtsdatum_entry.get()
        self.zimmernrinsert = int(self.checkin_zimmernr_entry.get())
        hotel.zimmerauflistung[self.zimmernrinsert].zimmernummer = self.zimmernrinsert
        hotel.zimmerauflistung[self.zimmernrinsert].status = "Frei"
        hotel.zimmerauflistung[self.zimmernrinsert].gast = ""
        hotel.zimmerauflistung[self.zimmernrinsert].anreise = ""
        hotel.zimmerauflistung[self.zimmernrinsert].abreise = ""
        self.zimmerliste.delete(self.zimmernrinsert)
        self.zimmerliste.insert(self.zimmernrinsert, "Zimmernr. " + str(self.zimmernrinsert) + ", Status: " + hotel.zimmerauflistung[self.zimmernrinsert].status)
        self.show_detail(self.zimmernrinsert)



class guestpage(tk.Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        pass

class Hotel:
    def __init__(self, hotelname, anzahlzimmer):
        self.hotelname = hotelname
        self.anzahlzimmer = anzahlzimmer
        self.zimmerauflistung = []
        i = 0
        while i < anzahlzimmer:
            self.zimmerauflistung.append(Zimmer(i+1, "Frei", "", "", ""))
            i += 1

class Zimmer(Hotel):
    def __init__(self, nr, status, gast, anreise, abreise):
        self.zimmernummer = nr
        self.status = status
        self.gast = gast
        self.anreise = anreise
        self.abreise = abreise

class Gast:
    def __init__(self, name, gebdatum, anreise, abreise):
        self.name = name
        self.geburtsdatum = gebdatum
        self.anreise = anreise
        self.abreise = abreise


hotel = Hotel("Asklepios", 30)
rootw = root()
rootw.geometry("1200x800+50+50")
rootw.mainloop()