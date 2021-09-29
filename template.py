


# Application Template for automation tasks
# Nigele McCoy

import tkinter
from tkinter import *
import tkinter.messagebox

class template:
    def __init__(self):

        # Application Structure
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        self.Main_label = tkinter.Label(self.top_frame, \
                                            text=' Template ')
        
        self.Input_label = tkinter.Label(self.top_frame, \
                                            text=' Input File :  ')
        self.Output_label = tkinter.Label(self.mid_frame, \
                                            text=' Output File :  ')
        self.inputFilename = tkinter.Entry(self.top_frame, \
                                          width=16)
        self.outputFilename = tkinter.Entry(self.mid_frame, \
                                          width=16)

        self.Main_label.pack(side='top')
        self.Input_label.pack(side='left')
        self.inputFilename.pack(side='left')
        self.Output_label.pack(side='left')
        self.outputFilename.pack(side='left')
        self.run_button = tkinter.Button(self.bottom_frame, \
                                               text='run', \
                                               command = self.run)
        self.run_button.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        # Menu Bar
        menubar = Menu(self.main_window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Info",command=self.getInfo)
        menubar.add_cascade(label='Info',menu=filemenu)
        self.main_window.config(menu=menubar)
        
        

        tkinter.mainloop()

    def run(self):
        tkinter.messagebox.showinfo("Run Function","executed")

    def getInfo(self):
        tkinter.messagebox.showinfo("Run Function","executed")
        

template()
