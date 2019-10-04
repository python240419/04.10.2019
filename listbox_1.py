from tkinter import *

root = Tk()
root.title("File system project")
root.geometry("200x250")

lbl = Label(root, text="A list of favourite countries...")
lbl.pack()

listbox = Listbox(root)
listbox.insert(1, "India")
listbox.insert(2, "USA")
listbox.insert(3, "Japan")
listbox.insert(4, "Austrelia")
listbox.pack()

btn = Button(root, text="print selected", command=lambda:print(listbox.curselection()[0]))
btn.pack()

for n in range(listbox.size()):
    print(listbox.get(0, "end")[n])

root.mainloop()
