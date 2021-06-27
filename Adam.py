


# AI program
# Creating a mind that learns

import os
import sys
import re
import webbrowser
import shutil
import shellt

shortmem = []
longmem = []
memory = {}

# main function for the brain
def brain():
      talk = ""
      learn = " "
      count = 0
      line = ""
      memline = ""
      # opens memory file for reading
      # read data into a list
      try:
            file = open("memory.txt",'r')

            while learn != "":
                  learn = file.readline()
                  longmem.append(learn)
                  
            file.close()

      # if no memory file is found create memory file
      except FileNotFoundError:
            file = open("memory.txt",'w')
            file.close()

      # load dictionary with the data from the longmem list
      ram()
      
      # running program
      # print(memory)
      while talk != "systemc":
            talk = input()
            # test to make sure that the value is not numberic
                                                
            try:
                  eval(talk)
                  # if numeric and not in dictionary add to dictionary
                  if memory.get(talk) == None:
                        # add value to dictionary
                        memory[talk] = eval(talk)
                        # add value to file
                        newline = ""
                        newvalue = ""
                        newvalue = str(eval(talk))
                        newline = talk + "  " + newvalue 
                        file = open('memory.txt','a')

                        file.write('\n' + newline)                        
                        file.close()

                        print(eval(talk))
                  # if value is in the dictionary
                  # print the numeric value from the dictionary 
                  else:
                        print(memory.get(talk))
            except (NameError,SyntaxError) as error:
                  try:
                  # check to see if string is in the dictionary
                  # if not then add it to file and dictionary
                        if talk == "shl":
                              talk = ""
                              shel()
                        elif talk == "thinkc":
                              talk = ""
                              cont()
                        elif memory.get(talk) == None:
                              newline = ""
                              newvalue = ""
                              print(talk + '?')
                              newvalue = input()
                              newline = talk + "  " + newvalue 
                              file = open('memory.txt','a')
      
                              file.write('\n' + newline)                        
                              file.close()
                              memory[talk] = newvalue
                        else:
                   # if string is there then print string to dictionary
                              print(memory.get(talk))
                              
                              
                  except (NameError,SyntaxError) as error:
                        pass
                        
                        
                        
# The shell is for running scripts or commands

def shel():
      
      shlline = ""
      shlline = input()

      shelt = shellt.shell()
      shelt.interp(shlline)
      
# Conscienceness 
def cont():
      keys = list(memory.keys())
      values = list(memory.values())
      strvalues = []
      strkeys = []
      print(keys)
      print(values)

      # store wrong and right questions in lists
      wrongq = []
      rightq = []

      content = " "
      
      try:
            file = open("wrong.txt","r")
            
            while content != "":
                  content = file.readline()
                  wrongq.append(content)
                  
            file.close()
            
            file = open("right.txt","r")
            
            while content != "":
                  content = file.readline()
                  rightq.append(content)
                  
            file.close()

            
            
      except FileNotFoundError:
            file = open("wrong.txt",'w')
            file.close()
            file = open("right.txt",'w')
            file.close()
            

      qlen = len(keys)
      count = 0
      vline = ""
      kline = ""
      
      # copying values and keys list to other lists
      # removing numeric values while copying data
      while count != qlen:
            try:
                  
                  vline = values[count]
                  eval(vline)
                  kline = keys[count]
                  eval(kline)
            except (SyntaxError,NameError,TypeError) as error:
                  vline = values[count]
                  kline = keys[count]  
                  strvalues.append(vline)
                  strkeys.append(kline)
            count = count + 1

      # fix questions and write how to store the question
      # check to make sure that the question is not in wrong or right list of
      # questions 
      qlen = len(strvalues)
      count = 0
      qline = ""
      while count != qlen:
            num = count
            qline = strvalues[num] +" "+ strkeys[count] + " ?"
            print(qline)
            qline = strkeys[1] +" "+ strvalues[count] + " ?"
            print(qline)
            
            break
            
            
      

# move data from list into dictionary
def ram():
      
      lengthmem = len(longmem)
      count = 0
      memline = " "
      while count != lengthmem:
            line = longmem[count]
            try:
                  memline = re.search(r'.+\s\s\b',line)
                  memline = memline.group(0)
                  line = line.replace(memline,'')
                  line = line.replace('\n','')
                  line = line.replace('\t','')
                  memline = memline[:-2]
                  memory[memline] = line
                  count = count + 1
            except (AttributeError,NameError,TypeError) as error:
                  count = count + 1
                  
                  
      count = count + 1

brain()

