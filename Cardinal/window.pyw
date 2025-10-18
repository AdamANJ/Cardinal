from tkinter import *

window = Tk()
import ctypes

window.geometry("905x509")
window.title("Cardinal")
window.config(bg="#81b3a0")

cardinal = PhotoImage(file='cardinal.png')
window.iconphoto(True,cardinal)

head = Label(window,text="Have You Coded Today?",
					font=("Lucida Console",25,"bold"),
					pady=20,
					bg="#81b3a0"
			)
head.pack()


myappid = u'cardinal.coding'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window.iconbitmap('')

window.mainloop()