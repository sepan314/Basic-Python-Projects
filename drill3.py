#!/usr/bin/python
# -*- coding: utf-8 -*-

##Serena Pan
##3/18/2020
##Python Version 3.8.1
##Drill: Check Files

import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master=master
        self.master.minsize(500, 250)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        #buttons
        self.browse1 = tk.Button(self.master, text='Browse...',bg="#F0F0F0", width=12, height=2)
        self.browse1.grid(row=0, column=0, padx=(20,0), pady=(40,0))
        self.browse2 = tk.Button(self.master, text='Browse...', bg="#F0F0F0", width=12, height=2)
        self.browse2.grid(row=1, column=0, padx=(20,0), pady=(15,0))
        self.btn_check = tk.Button(self.master, width=12, height=3, text='Check for files...')
        self.btn_check.grid(row=2,column=0,padx=(20,0),pady=(15,0))
        self.btn_close = tk.Button(self.master, width=12, height=3, text='Close Program')
        self.btn_close.grid(row=2,column=1,padx=(20,0),pady=(15,0), sticky=E)
        



        #text fields
        self.txt_browse1 = tk.Entry(self.master, text = '',width=30)
        self.txt_browse1.grid(row=0, column = 1, padx=(20,0),pady=(40,0))
        self.txt_browse2 = tk.Entry(self.master, text = '',width=30)
        self.txt_browse2.grid(row=1, column = 1, padx=(20,0),pady=(20,0))





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
