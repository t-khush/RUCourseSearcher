import tkinter as tk
import os
import os.path
from os import path
from tkinter import *
import tkinter.messagebox
from snipe import courseSearch


root=tk.Tk()
root.resizable(False, False)
root.title("Rutgers Course Searcher")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='ico.png'))
flag = False
totalList = ""
if(os.path.isfile("save.txt")):
    flag = True
    with open("save.txt", "r") as f:
        totalList = f.read()
        totalList = totalList.split(",")
    
def grabData():
    emailID = e1.get()
    phoneNumber = e2.get()
    driverPath = e3.get()
    indexList = e4.get()
    indexListSeparated = indexList.split(",")
    if(emailID=="" or phoneNumber == "" or indexList == ""):
        tkinter.messagebox.showinfo("Message", "Please Enter All Data")
    else:
        with open("save.txt", "w") as f:
            f.write(emailID+","+phoneNumber+","+driverPath+","+indexList)
        courseSearch(emailID, phoneNumber, indexListSeparated, driverPath)





hheight =root.winfo_screenheight()
wwidth = root.winfo_screenwidth()
canvas = tk.Canvas(root, height=hheight/1.5, width=wwidth/1.5, bg = "#FF5733")
canvas.pack()



canvas.create_text(wwidth/4+125,60, text="Rutgers Course Searcher", anchor="center", fill="white", font = "Arial 40 bold")


y_increase = 130

canvas.create_text(75,25+y_increase,fill="white",font="Arial 20 bold",text="Enter Email:")
e1 = Entry(canvas)
if(flag):
    e1.insert(END, totalList[0] )
canvas.create_window(500, 25+y_increase, window=e1)

canvas.create_text(117,75+y_increase,fill="white",font="Arial 20 bold",text="Enter Phone Number:")
e2 = Entry(canvas)
if(flag):
    e2.insert(END, totalList[1])
canvas.create_window(500, 75+y_increase, window=e2)


canvas.create_text(100,125+y_increase,fill="white",font="Arial 20 bold",text="Enter Driver Path:")
e3 = Entry(canvas)
if(flag):
    e3.insert(END, totalList[2])
canvas.create_window(500, 125+y_increase, window=e3)

canvas.create_text(190,175+y_increase,fill="white",font="Arial 20 bold",text="Enter Indexes (separated by comma):")
e4 = Entry(canvas, width = 20)
if(flag):
    placeholder = ""
    for item in totalList[3:len(totalList)]:
        placeholder += item +","
    placeholder = placeholder[0:len(placeholder)-1]
    e4.insert(END, placeholder)
canvas.create_window(500, 175+y_increase, window=e4)


enterData = Button(canvas, text = "Search Courses", command = grabData)
enterData.config(height= 5, width= 13)
canvas.create_window(800, 225, window=enterData)



canvas.pack()

root.mainloop()