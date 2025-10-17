from tkinter import *

window = Tk()
window.geometry("1280x720")
window.title("Cardinal")

cardinal = PhotoImage(file='cardinal.png')
window.iconphoto(True,cardinal)


window.mainloop()