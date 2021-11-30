#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#######################################################################################
#
#
#               Just a file to test some things outside of other files
#
#               by Jens Zorn
#
#               
#
#
#
#<°))))><
#######################################################################################

import tkinter as tk
root = tk.Tk()


str1 = tk.StringVar()
str2 = tk.StringVar()
str3 = tk.StringVar()
str1.set("Test1")
str2.set("Test2")
str3.set("Test3")
list = (str1.get(), str2.get(), str3.get())
print(list[1])
str1.set("Test1")
str2.set("Test4")
str3.set("Test3")
list = (str1.get(), str2.get(), str3.get())
print(list[1])
root.mainloop()
