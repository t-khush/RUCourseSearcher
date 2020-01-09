# Rutgers Course Searcher

This Rutgers Searcher was created for the Spring 2020 Semester. 

It leverages Selenium browser automation to webscrape the Rutgers Schedule of Classes page based off the indices of classes the user is searching for. Note that the user must enter a direct path to a Chrome Driver. 

The script is constantly refreshing all classes. Once a class ia open, the user is notified through an entered email and phone-number through the SMTP Protocol Client so that they can register for the class as soon as possible. Note that in text.py, the password must be entered for the notification setting to work. 

A simple GUI is created for the user through the Tkinter Framework, allowing the user-input (Email, Phone-Number, Driver Path, and Class Indices). After clicking "Search," the respective classes and their status(open/closed) are returned and is constantly refreshed.
