import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# root.geometry("1200x800")
# root.mainloop()

# Using frame
root.geometry("1200x800")
# root.wm_title("Conway's game of life") # or
root.title("Conway's game of life")

frame = ttk.Frame(root)
# this tells the frame how to arrange itself with the window
frame.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)

# creating a canvas
canvas = tk.Canvas(frame)
canvas.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)
# to draw a rectangle at the canva
canvas.create_rectangle(0, 0, 1200, 800, fill='blue') # fills the screen with blue


root.mainloop()