
from tkinter import Toplevel,Label,Entry,Button,messagebox
from tkcalendar import Calendar
import sql_link

def sign_up_ui():
    def submit():
        
        if first_name.get() == "" or second_name.get() == "":
            print(f"{first_name.get()} , {second_name.get()}")
            messagebox.showinfo("Error","You should fill all the data")
        elif password.get() != re_password.get():
            messagebox.showinfo("Error","Type the password correctly in both places")
        else:

            try:
                sql_link.into_database(first_name,second_name,password,DOB,user_name)
                signupwindow.destroy()
                messagebox.showinfo("login","Account created successfully")
                
            except:
                messagebox.showinfo("Error","The name already exist")

    signupwindow = Toplevel()
    signupwindow.title("Sign up")
    signupwindow.geometry("600x600")
    Label(signupwindow,text= "First Name", fg ="black").place(x=20,y=20)
    first_name = Entry(signupwindow,width=20, fg="black")
    first_name.place(x=20,y=40)
    Label(signupwindow,text= "Second Name", fg ="black").place(x=200,y=20)
    second_name = Entry(signupwindow,width=20, fg="black")
    second_name.place(x=200,y=40)
    Label(signupwindow,text="User Name").place(x=20,y=70)
    user_name = Entry(signupwindow,width=30)
    user_name.place(x=20,y=90)
    Label(signupwindow,text="Date-of-Birth").place(x=20,y=120)
    DOB  = Calendar(signupwindow,date_pattern= 'yyyy/mm/dd' ,selectmode = 'day',
        year = 2020, month = 5,
            day = 22)
    DOB.place(x=20,y=140)
                
    Label(signupwindow,text="New passwor").place(x=400,y=150)
    password = Entry(signupwindow)
    password.place(x=400,y=170)
    Label(signupwindow,text="Retype the passwor").place(x=400,y=210)
    re_password = Entry(signupwindow)
    re_password.place(x=400,y=230)
    Button(signupwindow,text = "submit", command=submit).place(x=250,y=350)
    signupwindow.mainloop()