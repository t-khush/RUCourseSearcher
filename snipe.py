import requests
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import os.path
###
import tkinter as tk
from os import path
from tkinter import *
import tkinter.messagebox
###
from text import notify

def updateText (now_open, closed):
    canvas.delete("text")
    canvas.create_text(285,450,fill="white",font="Arial 20 bold",text="\n\n"+now_open+closed, tag = "text")


def courseSearch(emailID, phoneNumber, indexList, driverPath):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome("chromedriverdir/chromedriver",options=chrome_options)
    now_open = ""
    driver = webdriver.Chrome(driverPath, options = chrome_options)
    #for x in range(1, 2):
    while len(indexList)!=0:
        print(indexList)
        deletions=[]
        closed=""
        for index in indexList:
            index_nospace = index.strip()  
            if(index_nospace==""):
                continue
            url = "https://sis.rutgers.edu/soc/#keyword?keyword="+index_nospace+"&semester=12020&campus=NB&level=U"
            print(url)
            driver.get(url)
            driver.refresh()
            time.sleep(2)
            html = driver.page_source
            flag = html.find("section sectionStatus_open")
            indexOfClass = html.find("courseMetadata.title")
            endIndex=0
            for x in range(indexOfClass, len(html)):
                if(html[x]=='<'):
                    endIndex=x
                    break
            className = html[indexOfClass+22:endIndex]

            if(flag!=-1):
                flag = True
            else:
                flag = False
            ans = ""
            if(flag):
                ans="true"
            else:
                ans="false"
                closed+=index_nospace + "\t" + className + ":\t"+ "Closed"+"\n\n"

            print(index_nospace+": "+className+" - "+ans)
            if(flag):
                deletions.append(index)
                now_open += index_nospace + "\t" + className + ":\t"+ "Open"+"\n\n"
                notify(emailID, phoneNumber, className, url)
        updateText(now_open, closed)
        canvas.update()

        for num in deletions:
            indexList.remove(num)
            
    driver.close()
    driver.quit()

###

    
def grabData():
    emailID = e1.get()
    phoneNumber = e2.get()
    driverPath = e3.get()
    indexList = e4.get()
    indexListSeparated = indexList.split(",")
    if(emailID=="" or phoneNumber == "" or indexList == "" or driverPath==""):
        tkinter.messagebox.showinfo("Message", "Please Enter All Data")
    else:
        updateText("", "")
        with open("save.txt", "w") as f:
            f.write(emailID+","+phoneNumber+","+indexList) # remember you deleted driver path from here and courseSearch
        courseSearch(emailID, phoneNumber, indexListSeparated, driverPath)




flag = False
totalList = ""
if(os.path.isfile("save.txt")):
    flag = True
    with open("save.txt", "r") as f:
        totalList = f.read()
        totalList = totalList.split(",")
        if(len(totalList)<=1):
            flag=False

root=tk.Tk()
root.resizable(False, False)
root.title("Rutgers Course Searcher")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='ico.png'))

hheight =root.winfo_screenheight()
wwidth = root.winfo_screenwidth()
canvas = tk.Canvas(root, height=hheight/1.5, width=wwidth/1.5, bg = "#FF5733")
canvas.pack()
updateText("", "")
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

#original x, y for "Enter Indexes text box" was 190, 175+y. e4 entry original was 500, 175+y_increase
canvas.create_text(190,175+y_increase,fill="white",font="Arial 20 bold",text="Enter Indexes (separated by comma):")
e4 = Entry(canvas, width = 20)
if(flag):
    placeholder = ""
    for item in totalList[2:len(totalList)]:
        placeholder += item +","
    placeholder = placeholder[0:len(placeholder)-1]
    e4.insert(END, placeholder)
canvas.create_window(500, 175+y_increase, window=e4)


enterData = Button(canvas, text = "Search Courses", command = grabData)
enterData.config(height= 5, width= 13)
canvas.create_window(800, 225, window=enterData)



canvas.pack()

root.mainloop()