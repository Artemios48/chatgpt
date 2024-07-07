from tkinter import *
from interface import *

window = Tk()
window.title("2048Game")
window.resizable(False, False)
window.geometry("450x650+450+50")
i = Interface(window)
window.mainloop()