
#Program Type writer Gui for writing and reading files
#Created by Nigele mccoy


import tkinter
from tkinter import Text, Tk
import os
import sys
import tkinter.messagebox
from tkinter import *
import getpass

class Typewriter:
      def __init__(self):

            self.main_window = tkinter.Tk()

            self.top_frame = tkinter.Frame()
            self.mid_frame = tkinter.Frame()
            self.bottom_frame = tkinter.Frame()
            master = tkinter.Frame()

            self.Main_label = tkinter.Label(self.top_frame, \
                                            text=' Type Writer ')
            self.Filename = tkinter.Entry(self.top_frame, \
                                          width=50)

            self.Main_label.pack(side='top')
            self.Filename.pack(side='top')
      
            scrollbar = Scrollbar(self.main_window)
            scrollbar.pack(side=RIGHT,fill=Y)
            self.Writer_entry = Text(self.main_window,yscrollcommand=scrollbar.set)
            self.Writer_entry.config(font=("Menlo",14))
            self.Writer_entry.pack(side='bottom')
            

            self.write_button = tkinter.Button(self.bottom_frame, \
                                               text='Write', \
                                               command = self.write)
            self.delete_button = tkinter.Button(self.bottom_frame, \
                                                text='Delete', \
                                                command = self.delete)
            self.read_button = tkinter.Button(self.bottom_frame, \
                                              text='Open', \
                                              command = self.read)
            self.clear_button = tkinter.Button(self.bottom_frame, \
                                               text='Clear', \
                                               command = self.clear)
            self.quit_button = tkinter.Button(self.bottom_frame, \
                                              text='Exit', \
                                              command = self.main_window.destroy)

            options = StringVar(master)
            options.set("Desktop")
            menu = OptionMenu(master,options,'Desktop','Documents','Downloads')
            self.write_button.pack(side='left')
            self.read_button.pack(side='left')
            self.clear_button.pack(side='left')
            self.quit_button.pack(side='left')
            menu.pack(side='left')
            
            self.delete_button.pack(side='left')

            self.top_frame.pack()
            self.mid_frame.pack()

            
            def Save():
                  Filename = str(self.Filename.get())
                  directory = options.get()
                  platform = sys.platform
                             
                  if platform == 'win32':
                        user = getpass.getuser()
                        if directory == 'Downloads':
                              path = "C:\\Users\\" + user + "\\Downloads\\" + Filename

 
                              try:
                                    
                                    File = str(self.Writer_entry.get('1.0','end'))

                                    creator = open(path, 'w')
                                    creator.write('\n\n' + File + '\n')
                                    creator.close()
                              except (FileNotFoundError,IsADirectoryError) as error:
                                    tkinter.messagebox.showinfo('File Not Found')
                              
                              
                        elif directory == 'Desktop':
                              path = "C:\\Users\\" + user + "\\Desktop\\" + Filename
 
                              
                              try:
                                    
                                    File = str(self.Writer_entry.get('1.0','end'))

                                    creator = open(path, 'w')
                                    creator.write('\n\n' + File + '\n')
                                    creator.close()
                              except (FileNotFoundError,IsADirectoryError) as error:
                                    tkinter.messagebox.showinfo('File Not Found')
                              


                        else:
                              path = "C:\\Users\\" + user + "\\Documents\\" + Filename 
                              
                              try:
                                    File = str(self.Writer_entry.get('1.0','end'))

                                    creator = open(path, 'w')
                                    creator.write('\n\n' + File + '\n')
                                    creator.close()
                              except (FileNotFoundError,IsADirectoryError) as error:
                                    tkinter.messagebox.showinfo('File Not Found')
                              

                              
                        
                        
                        
                  elif platform == 'linux' or platform == 'darwin' or platform == 'cygwin':
                        user = getpass.getuser()
                        if directory == 'Downloads':
                              path = "/Users/"+user+"/Downloads/"+Filename
                              try:
                                    File = str(self.Writer_entry.get('1.0','end'))

                                    creator = open(path, 'w')
                                    creator.write('\n\n' + File + '\n')
                                    creator.close()
                              except (FileNotFoundError,IsADirectoryError) as error:
                                    tkinter.messagebox.showinfo('File Not Found')
                              

                        elif directory == 'Desktop':
                              path = "/Users/"+user+"/Desktop/"+Filename
                              try:
                                    File = str(self.Writer_entry.get('1.0','end'))

                                    creator = open(path, 'w')
                                    creator.write('\n\n' + File + '\n')
                                    creator.close()
                              except (FileNotFoundError,IsADirectoryError) as error:
                                    tkinter.messagebox.showinfo('File Not Found')

                        else:
                              path = "/Users/"+user+"/Documents/"+Filename
                              try:
                                    File = str(self.Writer_entry.get('1.0','end'))

                                    creator = open(path, 'w')
                                    creator.write('\n\n' + File + '\n')
                                    creator.close()
                              except (FileNotFoundError,IsADirectoryError) as error:
                                    tkinter.messagebox.showinfo('File Not Found')
                              
                              

                  else:
                        tkinter.messagebox.showinfo('Platform not recognized please type in file path')
                        
            
                  
                  
                  #master.quit()
            button = Button(master, text="Save ", command=Save)
            button.pack()
            self.bottom_frame.pack()
            master.pack()

            tkinter.mainloop()
            
           
      def write(self):
            try:
                  Filename = str(self.Filename.get())
                  File = str(self.Writer_entry.get('1.0','end'))

                  creator = open(Filename, 'w')
                  creator.write('\n\n' + File + '\n')
                  creator.close()
            except FileNotFoundError as error:
                  tkinter.messagebox.showinfo('File Not Found')
                  
            

            
            
            
      def read(self):
            try:
                  Filename = str(self.Filename.get())

                  Creator = open(Filename, 'r')

                  for line in Creator:
                        words = str(line)
                        self.Writer_entry.insert('end',words)
                  Creator.close()
            except FileNotFoundError as error:
                  tkinter.messagebox.showinfo('File Not Found')
                  
      def clear(self):
            self.Writer_entry.delete('1.0','end')
            
            
                  
      def delete(self):
            Filename = str(self.Filename.get())
            try:
                  os.remove(Filename)
            except FileNotFoundError as error:
                  tkinter.messagebox.showinfo('File Not Found')
                  


      try:
            str.tk()
      except AttributeError as error:
            pass
      
      
      
            
            
            
            
                  
      

Typewriter()

            
            
            
