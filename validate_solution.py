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

        # register a function into the window
        validate_command_str = root.register(self.validate_str)

        self.inputText_name = Entry(root,
                               validate="key",
                               validatecommand=(validate_command_str, '%P'))
        self.inputText_name.pack()
    def validate(self, new_text):
        try:
            if new_text == "":
                return True
            fl = float(new_text)
            if fl > 999:
                return False
            return True
        except ValueError:
            return False

    def validate_str(self, new_text):
        if new_text == "":
            return True
        if new_text.find(' ') >= 0:
            return False
        return True

root = Tk()
root.geometry("200x100")
my_window = CalculatorWindow(root)

root.mainloop()  # blocking

