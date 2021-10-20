from tkinter import *
Font = ("Ephesis", 10 ,"bold")
a = ""
Window = Tk()
Window.title("Calculator")
Window.config(padx=10, pady = 7)


def value(val):
    number = ["1","2","3","4","5","6","7","8","9","0"]
    operation = ["+","-","*","/"]
    global a
    
    if val in number:
        a += str(val)
        display.config(text=a)   
        
    elif val in operation:
        a += str(val)
        display.config(text=a)
    elif val == "clear":
        display.config(text="0")
        a = ""      
    elif val == "ans":
        for i in operation:
            if i == "+":
                if i in a:
                    result = a.split("+")
                    add = int(result[0]) + int(result[1])
                    display.config(text=f"{add}")
            elif i == "-":
                if i in a:
                    result = a.split("-")
                    sub = int(result[0]) - int(result[1])
                    display.config(text=f"{sub}")
            elif i == "*":
                if i in a:
                    result = a.split("*")
                    mul = int(result[0]) * int(result[1])
                    display.config(text=f"{mul}")
            elif i == "/":
                if i in a:
                    result = a.split("/")
                    div = int(result[0]) / int(result[1])
                    display.config(text=f"{div}")
        
        
        
           
display = Label(text="0",justify=LEFT, font=Font)
display.grid(column=0, row=0, columnspan=4)

no1 = Button(text="1", width=7, bg="black", fg="white", font =Font, command = lambda  m="1": value(m))
no1.grid(column=0,row= 1)

no2 = Button(text="2", width=7, bg="black", fg="white", font =Font, command = lambda  m="2": value(m))
no2.grid(column=1,row= 1)

no3 = Button(text="3", width=7, bg="black", fg="white", font =Font, command = lambda  m="3": value(m))
no3.grid(column=2,row= 1)

plus = Button(text="+", width=7, bg="black", fg="white", font =Font, command = lambda  m="+": value(m))
plus.grid(column=3,row= 1)


no4 = Button(text="4", width=7, bg="black", fg="white", font =Font, command = lambda  m="4": value(m))
no4.grid(column=0,row= 2)

no5 = Button(text="5", width=7, bg="black", fg="white", font =Font, command = lambda  m="5": value(m))
no5.grid(column=1,row= 2)

no6 = Button(text="6", width=7, bg="black", fg="white", font =Font, command = lambda  m="6": value(m))
no6.grid(column=2,row= 2)

minus = Button(text="-", width=7, bg="black", fg="white", font =Font, command = lambda  m="-": value(m))
minus.grid(column=3,row= 2)


no7 = Button(text="7", width=7, bg="black", fg="white", font =Font, command = lambda  m="7": value(m))
no7.grid(column=0,row= 3)

no8 = Button(text="8", width=7, bg="black", fg="white", font =Font, command = lambda  m="8": value(m))
no8.grid(column=1,row= 3)

no9 = Button(text="9", width=7, bg="black", fg="white", font =Font, command = lambda  m="9": value(m))
no9.grid(column=2,row= 3)

multiplication = Button(text="*", width=7, bg="black", fg="white", font =Font, command = lambda  m="*": value(m))
multiplication.grid(column=3,row= 3)


clear = Button(text="CE", width=7, bg="black", fg="white", font =Font, command = lambda  m="clear": value(m) )
clear.grid(column=0,row= 4)

no0 = Button(text="0", width=7, bg="black", fg="white", font =Font, command = lambda  m="0": value(m))
no0.grid(column=1,row= 4)

ans = Button(text="=", width=7, bg="black", fg="white", font =Font, command = lambda  m="ans": value(m))
ans.grid(column=2,row= 4)

division = Button(text="/", width=7, bg="black", fg="white", font =Font, command = lambda  m="/": value(m))
division.grid(column=3,row= 4)

Window.mainloop()