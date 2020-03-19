#!/usr/bin/python
# -*- coding: utf-8 -*-

##Serena Pan
##3/18/2020
##Python Version 3.8.1
##Phonebook Demo using SQLite3 and Tkinter

import tkinter as tk
from tkinter import *

import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master= master
        self.master.minsize(500, 300) #(Height, weight)
##        self.master.maxsize(500,300)
##        phonebook_func.center_window(self, 500,300)
        self.master.title("The Tkinter phonebook demo")
        self.master.configure(bg="#F0F0F0")

        #load widgets from ext module
        phonebook_gui.load_gui(self)


if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
