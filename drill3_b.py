#!/usr/bin/python
# -*- coding: utf-8 -*-

##Serena Pan
##3/19/2020
##Python Version 3.8.1
##Drill: Check Files

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #config for master frame
        self.master=master
        self.master.minsize(500, 250)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        #buttons
            #lambda = anonymous function, used for inline function or pointing to functions with arguments
        self.browse1 = tk.Button(self.master, text='Browse...',bg="#F0F0F0", width=12, height=2, \
                                 command= self.choose_file1)
        self.browse1.grid(row=0, column=0, padx=(20,0), pady=(40,0))
        self.browse2 = tk.Button(self.master, text='Browse...', bg="#F0F0F0", width=12, height=2, \
                                 command= self.choose_file2)
        self.browse2.grid(row=1, column=0, padx=(20,0), pady=(15,0))
        self.btn_check = tk.Button(self.master, width=12, height=3, text='Check for files...', \
                                   command = lambda: messagebox.showinfo('Dear User...',"Button does not have a function yet"))
        self.btn_check.grid(row=2,column=0,padx=(20,0),pady=(15,0))
        self.btn_close = tk.Button(self.master, width=12, height=3, text='Close Program', command= self.close)
        self.btn_close.grid(row=2,column=1,padx=(20,0),pady=(15,0), sticky=E)


        #text fields
        self.txt_browse1 = tk.Entry(self.master, text = '',width=30)
        self.txt_browse1.grid(row=0, column = 1, padx=(20,0),pady=(40,0))
        self.txt_browse2 = tk.Entry(self.master, text = '',width=30)
        self.txt_browse2.grid(row=1, column = 1, padx=(20,0),pady=(20,0))


    #use askdirectory() to set function to browse buttons
    def choose_file1(self):
        self.filename = filedialog.askdirectory()
        self.txt_browse1.delete(0,END)
        self.txt_browse1.insert(0, self.filename)

    def choose_file2(self):
        self.filename2 = filedialog.askdirectory()
        self.txt_browse2.delete(0,END)
        self.txt_browse2.insert(0, self.filename2)

    #close program button function
    def close(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
            self.master.destroy()


    

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
