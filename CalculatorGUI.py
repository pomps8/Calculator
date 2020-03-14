import tkinter

# FileName: CalculatorGUI.py
# Author: Anthony Pompili
# Date: March 13, 2020
# Description: This file holds the GUI interface for the Calculator Application.

# Init a window with tkinter for application
window = tkinter.Tk()
window.title("Calculator")

display = tkinter.Label(window, text="00000000", font=("Arial Bold", 50))

window.geometry('400x500')
window.mainloop()