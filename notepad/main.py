from tkinter import *
from tkinter.filedialog import askopenfile,asksaveasfilename
import os
# This function is used display information about the creater
def info():
    # It create a dialogbox an display the info
    mb.showinfo("Info","Created by Jonah Jayasingh")
# This function is used to open a file
def open_file():
    global file
    if file == None:
        
        #  It is used to open file
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt", 
                                filetypes=[("All File", "*.*"),
                                    ('Text Documents','*.txt')])
        # content = opening_file.read()
        if file == "":
            file=None
        else:
            # To open a file
            window.title(os.path.basename(file) + " - Notepad")
            type_text.delete(1.0, END)
            f = open(file, "r")
            type_text.insert(1.0, f.read())
            f.close()


def save_file():
    global file
    if file == None:
        
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                                 filetypes=[("All Files","*.*"),
                                            ("Text Documents","*.txt")])
        if file == "":
            file = None
            
        else:
            # It is used save the file
            f = open(file, "w")
            f.write(type_text.get(1.0,END))
            f.close()
            window.title(os.path.basename(file) + " - Notepad")
            print("file saved")
            
            
        
    
def new_file():
    window.title("Untitled-Notepad")
    type_text.delete(1.0,END)
    

   
def cut_text():
    type_text.event_generate("<<Cut>>")
   
def copy_text():
    type_text.event_generate("<<Copy>>")

def paste_text():
    type_text.event_generate("<<Paste>>")


window = Tk()
window.title("Untitled-Notepad")
window.minsize(500,500)

# To create a menu
menu = Menu(window)
# To create sub menu
filemenu = Menu(menu,tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="open", command= open_file)
filemenu.add_command(label="Save", command= save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
menu.add_cascade(label="File", menu=filemenu)

edit = Menu(menu,tearoff=0)
edit.add_command(label="Cut", command=cut_text)
edit.add_command(label="Copy", command=copy_text)
edit.add_command(label="Paste", command=paste_text)
menu.add_cascade(label="Edit",menu=edit)

about = Menu(menu,tearoff=0)
about.add_command(label="Info", command=info)
menu.add_cascade(label="About",menu=about)
window.config(menu=menu)


type_text = Text(window)
file =None
type_text.pack(expand=True, fill=BOTH)


scroll =Scrollbar(type_text)
scroll.pack(side=RIGHT,fil=Y)
scroll.config(command=type_text.yview)
type_text.config(yscrollcommand=scroll.set)

window.mainloop()