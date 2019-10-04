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
    def validate(self, new_text):
        try:
            if new_text == "":
                return True
            fl = float(new_text)
            return True
        except ValueError:
            return False



root = Tk()
root.geometry("200x100")
my_window = CalculatorWindow(root)

root.mainloop()  # blocking

# targil:
# 1. create entry which will not accept numbers beyond 1000
# 2. create entry which will not accept a name with spaces
