from tkinter import *
import sqlite3

window = Tk()
import ctypes

window.geometry("905x509")
window.title("Cardinal")
window.config(bg="#81b3a0")


#Database
conn = sqlite3.connect('cardinal_database.db') #Create or Connect to db

c = conn.cursor()

# Table Create Example
# Types: Text, Integers, REAL (decimals), NULL, Blob (image)

# c.execute("""
# 	CREATE TABLE addresses (
#		first_name text,
#		last_name text,
#		address text,
#		city text,
#		state text,
#		zipcode integer
# 	)""")

conn.commit() #Commits changes

conn.close() #Closes db


#Other
cardinal = PhotoImage(file='cardinal.png')
window.iconphoto(True,cardinal)

head = Label(window,text="Have You Coded Today?",
					font=("Lucida Console",25,"bold"),
					pady=20,
					bg="#81b3a0"
			)
head.pack()

count = 0

def counter():
	global count
	count += 1
	countr.config(text=count)

button = Button(window,text='I did!')
button.config(command=counter)
button.config(font=("Lucida Console", 15))

countr = Label(window, text=count)
countr.config(font=("Lucida Console",15))
countr.pack()
button.pack()


myappid = u'cardinal.coding'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.mainloop()