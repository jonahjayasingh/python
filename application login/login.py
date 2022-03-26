from tkinter import Toplevel,Label,Entry,Button,messagebox
import sql_link

def password_check():
    sql_link.from_database()
    myresult = sql_link.from_database()
    for i in range(0,len(myresult)):
        if myresult[i][0] == user_name.get() and myresult[i][1] == password.get():
            loginWindow.destroy()
            messagebox.showinfo("login","login successfull")
            

def login():

    global user_name,password,loginWindow
    
    loginWindow = Toplevel()
    loginWindow.title("Login")
    loginWindow.geometry("300x300")
    Label(loginWindow,text="User Name").place(x = 20 , y =20)
    user_name = Entry(loginWindow)
    user_name.place(x=20, y =40)
    Label(loginWindow,text="Passwor").place(x = 20 , y =80)
    password = Entry(loginWindow)
    password.place(x=20, y =100)
    Button(loginWindow,text="Submit", command=password_check).place(x=100,y = 160)
    loginWindow.mainloop()
     
    