#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
###############################################################################
#
#
#               hotel app
#
#               by Jens Zorn
#
#               -
#
#
#
# <°))))><
###############################################################################
import tkinter as tk
from tkinter import NSEW, StringVar, E, Scrollbar, Listbox, DISABLED, END
# from tkinter import ttk
import os
# import json, sys


class AutoScrollbar(tk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.
    # only works with grid
    def set(self, low, high):
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        tk.Scrollbar.set(self, low, high)


class root(tk.Tk):

    current_page = ""
    login = False
    pages = {}

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # root window settings
        self.title("Test Window")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # root frame, holds every content
        self.root_window = tk.Frame(self)
        self.root_window.grid(row=0, column=0, sticky=NSEW)
        self.root_window.rowconfigure(1, weight=1)
        self.root_window.columnconfigure(0, weight=1)

        # main window content (between menubar and statusbar)
        self.root_canvas = tk.Canvas(self.root_window, background="black")
        self.root_canvas.grid(row=1, column=0, sticky=NSEW)
        self.root_content = tk.Frame(self.root_canvas, background="cyan")
        # self.root_content.rowconfigure(0, weight=1)
        # self.root_content.columnconfigure(0, weight=1)

        # scrollbars for root window
        self.vertical_scrollbar = AutoScrollbar(
            self.root_window, orient="vertical",
            command=self.root_canvas.yview)
        self.vertical_scrollbar.grid(row=1, column=1, rowspan=1, sticky="ns")
        self.horizontal_scrollbar = AutoScrollbar(
            self.root_window, orient="horizontal",
            command=self.root_canvas.xview)
        self.horizontal_scrollbar.grid(row=2, column=0, sticky="ew")
        # make scrollbars react to windowsize changes
        self.root_content.bind("<Configure>",
                               lambda e: self.root_canvas.configure(
                                   scrollregion=self.root_canvas.bbox("all")))
        self.root_content_id = self.root_canvas.create_window(
            (0, 0), window=self.root_content, anchor="nw")
        self.root_canvas.configure(yscrollcommand=self.vertical_scrollbar.set)
        self.root_canvas.configure(
            xscrollcommand=self.horizontal_scrollbar.set)
        # adjust positioning of root_content_id inside the canvas on resizing
        # the window
        self.root_canvas.bind("<Configure>", self.on_resize_window)

        # initialize menu bar and statusbar
        self.menu_bar()
        self.statusbar()

        # initialize Welcome_Page for login, tbd. gets destroyed on finish,
        # then load Main_Page
        self.change_page("Welcome_Page")
        self.update_idletasks()

    def change_page(self, wanted_page):
        if not root.login:
            self.page = Welcome_Page(parent=self.root_content)
            self.page.grid(row=0, column=0, sticky=NSEW)
            #
            print(root.login)
            # root.login = True
        elif root.pages == {}:
            for P in (Main_Page, Second_Page, Error_Page):
                page_name = P.__name__
                page = P(parent=self.root_content)
                page.grid(row=0, column=0, sticky="nwes")
                root.pages[page_name] = page
            self.page = root.pages["Error_Page"]
            self.page.tkraise()
            print(root.login)
        elif wanted_page == "Welcome_Page" and root.login and root.pages != {}:
            self.page = root.pages["Error_Page"]
            self.page.tkraise()
            print(root.login)
        else:
            self.page = self.pages[wanted_page]
            self.page.tkraise()
            print(root.login)
        root.current_page = self.page
        self.update_idletasks()

    def on_resize_window(self, newwindow):
        self.update_idletasks()
        x = (newwindow.width / 2) - (root.current_page.winfo_width() / 2)
        self.statb_upd = ("Fenstergröße: " + str(newwindow.width)
                          + ", Canvasgröße: "
                          + str(self.root_canvas.winfo_width())
                          + " : Position: " + str(x) + " = "
                          + str(newwindow.width / 2) + " - "
                          + str(self.current_page.winfo_width() / 2)
                          + ", Position: "
                          + str(self.root_canvas.coords(self.root_content_id)))
        self.text.set(self.statb_upd)
        self.root_canvas.coords(self.root_content_id, x, 0)
        self.update_idletasks()

    def menu_bar(self):
        self.menu_bar_frame = tk.Frame(self.root_window)
        self.menu_bar_frame.grid(row=0, column=0, sticky="nwe")
        self.menubar = tk.Menu(self.menu_bar_frame)
        # self.file_menu = tk.Menu(self.menubar)
        # self.file_menu.add_command(label="second",
        # command= lambda: self.change_page("Second_Page"))
        # self.file_menu.add_command(label="Exit", command=quit)
        # self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_command(
            label="welcome", command=lambda: self.change_page("Welcome_Page"))
        self.menubar.add_command(
            label="main", command=lambda: self.change_page("Main_Page"))
        self.menubar.add_command(
            label="second", command=lambda: self.change_page("Second_Page"))
        self.menubar.add_command(label="Exit", command=quit)
        self.config(menu=self.menubar)

    def statusbar(self):
        self.login1 = "Nö"
        self.text = StringVar()
        self.text.set(self.login1)
        self.statusbar_frame = tk.Frame(self.root_window)
        self.statusbar_frame.grid(row=3, column=0, sticky="nwe")
        label = tk.Label(self.statusbar_frame, textvariable=self.text)
        label.grid(row=0, column=0)


class Welcome_Page(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        subfolders = [f.name for f in os.scandir(
            "umschulung_ibb/hotel_app") if f.is_dir()]
        header = tk.Label(
            self, text="""Willkommen im Hotelmanager.\n
            Wähle dein Hotel aus, oder lege ein neues an.""")
        header.grid(row=0, column=0)

        hotel_list_scrollbar = Scrollbar(self)
        hotel_list_scrollbar.grid(row=1, column=1, sticky="nsw")
        hotel_list = Listbox(
            self, width=40, yscrollcommand=hotel_list_scrollbar.set)
        hotel_list.grid(row=1, column=0, sticky=E)
        hotel_list_scrollbar.config(command=hotel_list.yview)

        button = tk.Button(self, text="Select")
        button.grid(row=2, column=0, sticky=E)
        button1 = tk.Button(self, text="Create New")
        button1.grid(row=2, column=1, sticky=E)
        if subfolders == []:
            button.config(state=DISABLED)
        else:
            for folder in subfolders:
                n = int(20 - len(folder)/2)
                print(n)
                print(len(folder))
                folder = "  "*(n-1) + folder
                hotel_list.insert(END, str(folder))

    def login(self):
        root.login = True
        print(root.login)


class Main_Page(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.grid_propagate(True)
        self.config(borderwidth=0, bg="red")
        self.button = tk.Button(self, text="Test")
        self.button.grid(row=1, column=0, sticky=E)
        self.button1 = tk.Button(self, text="Test")
        self.button1.grid(row=1, column=1, sticky=E)
        self.button2 = tk.Button(self, text="Test")
        self.button2.grid(row=1, column=2, sticky=E)
        self.button3 = tk.Button(self, text="Test")
        self.button3.grid(row=1, column=3, sticky=E)
        self.button4 = tk.Button(self, text="Test")
        self.button4.grid(row=1, column=4, sticky=E)


class Second_Page(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.grid_propagate(True)
        self.config(borderwidth=0, bg="red")
        self.button = tk.Button(self, text="Test2")
        self.button.grid(row=1, column=0, sticky=E)
        self.button1 = tk.Button(self, text="Test2")
        self.button1.grid(row=1, column=1, sticky=E)
        self.button2 = tk.Button(self, text="Test2")
        self.button2.grid(row=1, column=2, sticky=E)
        self.button3 = tk.Button(self, text="Test2")
        self.button3.grid(row=1, column=3, sticky=E)
        self.button4 = tk.Button(self, text="Test2")
        self.button4.grid(row=1, column=4, sticky=E)


class Error_Page(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.grid_propagate(True)
        self.config(borderwidth=0, bg="red")
        self.button = tk.Button(self, text="Error, tried to call Welcome Page")
        self.button.grid(row=1, column=0, sticky=E)
        self.button1 = tk.Button(self, text="Test2")
        self.button1.grid(row=1, column=1, sticky=E)
        self.button2 = tk.Button(self, text="Test2")
        self.button2.grid(row=1, column=2, sticky=E)
        self.button3 = tk.Button(self, text="Test2")
        self.button3.grid(row=1, column=3, sticky=E)
        self.button4 = tk.Button(self, text="Test2")
        self.button4.grid(row=1, column=4, sticky=E)


if __name__ == "__main__":
    rootw = root()
    rootw.resizable(True, True)
    rootw.geometry("800x600+500+100")
    rootw.mainloop()
