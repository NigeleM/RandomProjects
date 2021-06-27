
# System Shell
# Command line tool

import getpass
import os, sys, shutil,re,webbrowser
def shell():
      print('System Shell []:', getpass.getuser())
      command = ''
      command = input()
      while command != '[systemc]':
            if command == '':
                  command = input()
            try:  # Digits
                  var = re.search(r'\d.+', command)
                  var = var.group(0)
                  if var != "None":
                        var = eval(var)
                        print(var)
                        command = ''
                        
                        
            except AttributeError:
                  try:
                        var = re.search(r'\[w]',command)
                        var = var.group(0)
                        try:
                              # file to know what is being written
                              var = re.search(r'file',command)
                              var = var.group(0)
                              
                              filename = input()
                              file = open(filename, 'w')
                              fileinput = input()
                              file.write(fileinput + '\n')
                              file.close()
                              command = ''
                        except AttributeError:
                              var = 'file argument missing'
                              print(var)
                              command = ''
                              
                              
                              
                  except AttributeError:
                        try:
                              var = re.search(r'\[r]',command)
                              var = var.group(0)
                              try:
                                    # file to know what is being written
                                    var = re.search(r'file',command)
                                    var = var.group(0)
                                    try:
                                          
                                          filename = input()
                                          file = open(filename, 'r')

                                          for linz in file:
                                                print(linz)
                                          
                                          file.close()
                                          command = ''
                                    except  FileNotFoundError:
                                          var = 'file not found'
                                          print(var)
                                          command = ''
                              except AttributeError:
                                    var = 'file argument missing'
                                    print(var)
                                    command = ''
                              
                        except AttributeError:
                              try:
                                    var = re.search(r'\[rw]',command)
                                    var = var.group(0)
      
                                    try:
                                          # file to know what is being read
                                          var = re.search(r'file',command)
                                          var = var.group(0)
                                          var = var.replace(' ','')
                                          filename = ''
                                          fileinput = ''
                                          try:
                                                filename = input()
                                                file = open(filename, 'r')

                                                for linz in file:
                                                      print(linz)
                                          
                                                file.close()

                                                file = open(filename, 'w')
                                                fileinput = input()
                                                file.write(fileinput + '\n')
                                                file.close()
                                          except  FileNotFoundError:
                                                var = 'file not found'
                                                print(var)
                                                command = ''
                                          
                                    except AttributeError:
                                          var = 'file argument missing'
                                          print(var)
                                          command = ''
                                          
                              except AttributeError:
                                    var = 'nothing read'
                                    print(var)
                                    command = ''
                              
                            
                                                                        

                   
                   
      

            
            
            
            

shell()
