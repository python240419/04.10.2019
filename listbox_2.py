from tkinter import *
from tkinter import messagebox

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

def print_selected_item():
    selected_item_index = listbox.curselection()[0]
    print(listbox.get(selected_item_index))

def delete_selected_item():
    selected_item_index = listbox.curselection()[0]
    listbox.delete(selected_item_index)

btn_print = Button(root, text="print selected", command=print_selected_item)
btn_print.pack()

btn_del = Button(root, text="delete selected", command=delete_selected_item)
btn_del.pack()

for n in range(listbox.size()):
    print(listbox.get(0, "end")[n])

def dbl(item):
    if len(listbox.curselection()) > 0:
        msgbox = messagebox.askquestion('Delete?', 'Sure you want to delete?', icon='warning')
        if msgbox == 'yes':
            selected_item_index = listbox.curselection()[0]
            listbox.delete(selected_item_index)
listbox.bind('<Double-Button>', dbl)

root.mainloop()

# 1 - delete dialog show the name of the country?
# 2 - add Entry with "Add" button - will insert the new item into the listbox
