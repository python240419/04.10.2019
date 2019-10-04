from tkinter import *
import time

class CalculatorWindow:
    def __init__(self, root):
        self.root= root
        root.title("Calculator")

        # register a function into the window
        validate_command = root.register(self.validate)

        self.inputText = Entry(root,
                               validate="key",
                               validatecommand=(validate_command, '%P'))
        self.inputText.pack()

        self.v = DoubleVar() # -- double var for demo of lable, could be simple variable
        self.v.set(0)
        self.mylbl = Label(root, textvariable=self.v)
        self.mylbl.pack()

    def validate(self, new_text):
        try:
            if new_text == "":
                self.v.set(0)
                return True
            fl = float(new_text)
            self.v.set(fl)
            return True
        except ValueError:
            return False



root = Tk()
root.geometry("200x100")
my_window = CalculatorWindow(root)

root.mainloop()  # blocking
