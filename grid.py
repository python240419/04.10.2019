from tkinter import *
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0
        # IntVar, StrVar
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master,
            textvariable = self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master,
                           validate="key",
                           validatecommand=(vcmd, '%P'))
        self.add_button = Button(master,
            text="+",command=lambda: self.update("add"))
        self.sub_button = Button(master,
            text="-",command=lambda: self.update("sub"))
        self.reset_button = Button(master,
            text="C",command=lambda: self.update("clr"))

        # layuot
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column = 1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3)
        self.add_button.grid(row=2, column=0)
        self.sub_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2)

    def add(self):
        self.total += float(self.entry.get())
        self.total_label_text.set(self.total)
    def update(self, method):
        if method== "add":
            self.total += float(self.entered_number)
        elif method == "sub":
            self.total -= float(self.entered_number)
        else: # reset
            self.total = 0
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)
    def validate(self, new_text):
        if not new_text:
            self.entered_number = 0
            return True
        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            return False
root = Tk()
my_window = Calculator(root )
root.mainloop() # blocking

print("Goodbye...")
