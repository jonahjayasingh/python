from tkinter import Tk,Label,Button
from PIL import Image,ImageTk
import signup
import login
ui = Tk()  
ui.geometry('720x720')
logo_image = "logo/download.jpg"
img = ImageTk.PhotoImage(Image.open(logo_image))
logo = Label(ui, image= img).place(x=200, y =50)
log_in = Button(text="Log in",fg= "black", bg="#ff8080", command= login.login).place(x = 350 , y= 350)
sign_in = Button(text = "Create a Account",fg= "black", bg="#ff8080" ,command=signup.sign_up_ui).place(x=330, y=400)
ui.mainloop()