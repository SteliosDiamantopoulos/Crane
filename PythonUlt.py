# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:40:47 2022

@author: User
"""
import pandas as pd
import random
import numpy as np
import string
import datetime
import sympy as smp
from tkinter import *
import queue


def createData():
    k=1
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 2, 1)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    dataset=[]
    S=1
    for i in range (5):
        for j in range (10):
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
            data_config=[name, random.randint(3,6),i%5 ,j , round(random.randint(0,1)),round(random.randint(0,1)),round(random.randint(0,1)),random_date]
            k=k+1
            dataset = dataset + [data_config]
      
    global df
    df = pd.DataFrame(dataset, columns = ['OrderID', 'Weight(T)','PosX','PosY','Occupied','StaffIn','Alarm','Date'])   
    df.to_csv(r'C:\Users\stdia\Desktop\CranePeoject\CraneDATA.csv', index = False)
    return df
def mainDataset():
    return df

def maintnaceBlocks():
    #Print the Number And Location of the Blocks that staff are working on
    alarms=np.array(df['StaffIn'])
    print((alarms))
    no_alarms = 0
    print (alarms[6])
    alarm_pos = []
    for alarm in alarms:
        if alarm==1:
            no_alarms = no_alarms+1        
    for i in range (len(alarms)):
        if alarms[i] == 1:
            alarm_pos = alarm_pos+[i]
    print(alarm_pos)
    print(len(alarm_pos),no_alarms)
    return alarm_pos

    
def alarms():   
    #Print the Number of alarms as well as the Location 
    alarms=np.array(df['Alarm'])
    print((alarms))
    no_alarms = 0
    print (alarms[6])
    alarm_pos = []
    for alarm in alarms:
        if alarm==1:
            no_alarms = no_alarms+1        
    for i in range (len(alarms)):
        if alarms[i] == 1:
            alarm_pos = alarm_pos+[i]
    print(alarm_pos)
    print(len(alarm_pos),no_alarms)
    return alarm_pos

def id_search(user_input):  
    orderID=np.array(df['OrderID'])
    list1 = orderID.tolist()
    print(list1)
    pos = []
    for i in range(len(list1)):
        if user_input==list1[i]:
            pos.append(i)
    
    if len(pos)==0:
        print ("No such order Found")
    return (pos)
def color_check(counter):
    occupied=np.array(df['Occupied'])
    staff_in=np.array(df['StaffIn'])      
    if occupied[counter]==1:
        color="GRAY"
    else:
        color = "WHITE"
    if staff_in[counter]==1:
        color = "RED"
    return(color)

def right_click(index):
    rows=np.array(df['PosX'])
    cols=np.array(df['PosY'])
    orderID=np.array(df['OrderID'])
    print("OrderID:"+str(orderID[index]),"PosX:"+str(rows[index]),"PosY"+str(cols[index]))
    string = str(orderID[index]),str(rows[index]),str(cols[index])
    status_label = Label(mainFrame,text=string,bd=1,relief=SUNKEN,anchor=E)
    status_label.pack(fill=X,side =BOTTOM,ipady=2)
    return(rows[index],cols[index])
def openGrid():
    mainwindow = Tk()
    mainFrame = Frame(mainwindow, bg="White")
    mainFrame.pack(fill="both", expand=True)
    #Grid Data
    orderID=np.array(df['OrderID'])
    counter = 0
    grid_frame = Frame(mainFrame)
    button_list=[]
    for row in range(5):
        for column in range(10):
            counter = row*10+column
            color = color_check(counter)#colorCheck
            button = Button(grid_frame,text="Item"+str(orderID[counter])+str(counter),command= lambda id=counter:right_click(id) ,bg = color,fg="black",padx=5,pady=5)
            button.grid(row=row,column=column,padx=5,pady=5,sticky = "nsew")
            button_list.append([counter,row,column])
            grid_frame.grid_columnconfigure(column,weight=1)  
             
    
    grid_frame.pack(fill = "x")
    menu_frame = Label(mainFrame,text=string,bd=1)
    
    menu_frame.pack(fill = "x")

def returnPos(index):
    return(button_list[index][1],button_list[index][2])
def returnMass(index):
    mass=np.array(df['Weight(T)'])
    return(mass[index])    

    mainwindow.mainloop()
def gridOpener():
    mainwindow = Tk()
    mainFrame = Frame(mainwindow, bg="White")
    mainFrame.pack(fill="both", expand=True)
    #Grid Data
    orderID=np.array(df['OrderID'])
    counter = 0
    grid_frame = Frame(mainFrame)
    button_list=[]
    for row in range(5):
        for column in range(10):
            counter = row*10+column
            color = color_check(counter)#colorCheck
            button = Button(grid_frame,text="Item"+str(orderID[counter])+str(counter),command= lambda id=counter:right_click(id) ,bg = color,fg="black",padx=5,pady=5)
            button.grid(row=row,column=column,padx=5,pady=5,sticky = "nsew")
            button_list.append([counter,row,column])
            grid_frame.grid_columnconfigure(column,weight=1)  
             
    
    grid_frame.pack(fill = "x")
    menu_frame = Label(mainFrame,text=string,bd=1)
    
    menu_frame.pack(fill = "x")

    try:
        pass
    except NameError:
        return "NameError occurred. Some variable isn't defined."
    
def createMaze2():
    rows=np.array(df['PosX'])
    cols=np.array(df['PosY'])
    occupied=np.array(df['StaffIn'])
    print(type(rows))
    rows.tolist()
    cols.tolist()
    occupied.tolist()
    occupied_star=[]
    pos = []
    output=[]
    list1=np.array(df['StaffIn'])
    for i in range(len(list1)):
            if(i%10==0):
                if len(pos)!=0:
                    
                    output.append(pos)
                    pos = []
            
            if list1[i]==1:
                pos.append("#")
            if list1[i]==0:
                pos.append(" ")
                
           
                
    output.append(pos)
    output[0][0]="O"  #Define start position
    output[4][9]="X"  #Define end position
   #Make sure there is a free path 
    output[1][0]=" "
    output[2][0]=" "
    output[2][1]=" "
    output[2][2]=" "
    output[2][3]=" "
    output[2][4]=" "
    output[2][5]=" "
    output[2][6]=" "
    output[2][7]=" "
    output[2][8]=" "
    output[2][9]=" "
    output[3][9]=" "
    

    for i in range(len(output)):
     
        print(str(output[i])+"\n")   
   



   
    return output



def printMaze(maze, path=" "):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    move_list = ()
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        print('The moves are:',moves)
        return True,moves

    return False
# MAIN ALGORITHM

def PathFinding():
    nums = queue.Queue()
    nums.put(" ")
    add = " "
    maze  = createMaze2()
    while not findEnd(maze, add): 
        
        add = nums.get()
        #print(add)
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put):
                nums.put(put)
    