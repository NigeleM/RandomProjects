

import os
import sys
import re
import shutil
import getpass
import tkinter


#create a directory
# save files from a directory
# save directories from a directory
# save directories and files

# know when completed
# know how much data has been copied

#os.path.getsize()

def app():
      print(" ")
      print("Enter Option ")
      print("1. Files only ")
      print("2. Directories and files ")
      print("3. Exit")
 
      try:
            option = int(input())
            if option == 1:
                  files()
            elif option == 2:
                  directory()
            elif option == 3:
                  sys.exit()
            else:
                  print("Invalid Option")
                  app()
      except ValueError as error:
            print("Invalid Option")
            app()
 
def files():
      print("Create a folder")
      folder = input("Enter name : ")
      print("Enter name of the directory you want to copy from")
      dirs = input("Enter name : ")
      size = 0
      
      try:
            os.mkdir(folder)
            oslist = []
            oslist = os.listdir(dirs)
            var = 0
            totatl = 0
            total = len(os.listdir(dirs))

            while var != total:
                  line = ''
                  line = oslist[var]
                  osline = dirs + line
                  if os.path.isfile(osline) == True:
                        shutil.copy(osline,folder)
                        size += os.path.getsize(osline)
                        var = var + 1
                  else:
                        var = var + 1
                        
                  
            
      except FileExistsError as error:
            pass
            oslist = []
            oslist = os.listdir(dirs)
            var = 0
            total = 0
            total = len(os.listdir(dirs))

            while var != total:
                  line = ''
                  line = oslist[var]
                  osline = dirs + line
                  if os.path.isfile(osline) == True:
                        shutil.copy(osline,folder)
                        size += os.path.getsize(osline)
                        var = var + 1
                  else:
                        size += os.path.getsize(osline)
                        var = var + 1

      except FileNotFoundError as error:
            print("Invalid Path")
            app()


      size = size / 1000000000
      if size > 1.0:
            print("Completed","Size ",size, " mb")
            app()
      else:
            print("Completed","Size ",size, " kb")
            app()
            
            
      
            
            
            



def directory():
      print("Create a folder")
      folder = input("Enter name : ")
      print("Enter name of the directory you want to copy from")
      dirs = input("Enter name : ")
      size = 0

      
      try:
            shutil.copytree(dirs,folder)
            oslist = []
            oslist = os.listdir(dirs)
            var = 0
            total = 0
            total = len(oslist)
            while var != total:
                  line = ''
                  line = oslist[var]
                  osline = dirs + line
                  size += os.path.getsize(osline)
                  var = var + 1
                  
            
      except (FileExistsError,FileNotFoundError) as error:
            print("Invalid Path")
            app()
            

      size = size / 1000000
      if size > 1.0:
            print("Completed","Size ",size, " mb")
            app()
      else:
            print("Completed","Size ",size, " kb")
            app()
            
            
      
app()
