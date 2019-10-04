from tkinter import *
import time

class CalculatorWindow:
    def __init__(self, root):
        self.root= root
        root.title("Calculator")

        v = IntVar()
        v.set(" ")  # initialize

        for n in range(1, 10):
            b = Radiobutton(root, text=n,
                            variable=v, value=n,
                            indicatoron=0,
                            width=30)
            b.pack()
        bn = Button(root, text="Print", command=lambda:print(v.get()))
        bn.pack()

root = Tk()
my_window = CalculatorWindow(root)

root.mainloop()  # blocking

# targil:
# create option buttons from 1-10 in loop (maybe without modes?)
# print button -> will print the current selection

