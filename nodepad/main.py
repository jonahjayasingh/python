from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfile
from tkinter import Text

# This function is used display information about the creater
def info():
    # It create a dialogbox an display the info
    mb.showinfo("Info","Created by Jonah Jayasingh")
# This function is used to open a file
def open_file():
    #  It is used to open file
    opening_file= askopenfile(mode="r", filetypes=[('Text Files', '*.txt')])
    content = opening_file.read()
    type_text.index(end)

   
window = Tk()
window.title("Notepad")
window.minsize(500,500)
# To create a menu
menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label="New")
file.add_command(label="open", command= open_file)
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_command(label="close")
file.add_separator()
file.add_command(label="Exit",command=window.quit)
menu.add_cascade(label="File", menu=file)

edit = Menu(menu,tearoff=0)
edit.add_command(label="Undo")
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
menu.add_cascade(label="Edit",menu=edit)

about = Menu(menu,tearoff=0)
about.add_command(label="Info", command=info)
menu.add_cascade(label="About",menu=about)
window.config(menu=menu)

type_text = Text(window, height=40, width=60)
type_text.pack()


window.mainloop()