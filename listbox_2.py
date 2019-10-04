from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("File system project")
# root.geometry("200x250")

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
    print(listbox.get(n))

v = StringVar()
v.set('')
entry1 = Entry(root, textvariable = v)
entry1.pack()
def add_item():
    listbox.insert('end', v.get())
    v.set('')
btn_add = Button(root, text="add", command=add_item)
btn_add.pack()


def dbl(item):
    if len(listbox.curselection()) > 0:
        selected_item_index = listbox.curselection()[0]
        msgbox = messagebox.askquestion('Delete?', f'Sure you want to delete {listbox.get(selected_item_index)}?', icon='warning')
        if msgbox == 'yes':
            listbox.delete(selected_item_index)
listbox.bind('<Double-Button>', dbl)

root.mainloop()
