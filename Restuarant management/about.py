from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class About:
    def __init__(self,root):
        self.root=root
        self.root.title("About Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #Bg image
        self.bg=ImageTk.PhotoImage(file="images/bg.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, width=1350, height=700)
        #ab = Label(self.root, text="About Us", font=("times new roman", 20, "bold"),
                      #fg="white", bg="none").place(x=50, y=30)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        message='''
        This system is designed to be used by restaurant staff.
        The restaurant staff will be required to register on the system by using 
        their email and password. Thereafter, they can login and access the system.
        A menu will be displayed and the waiter can click and enter the number of 
        each item selected by the customer. 
        
        Once the customer is satisfied with  their order, a total bill will be 
        generated and saved on a database. 
        The bill can be printed and presented to the customer.  
        '''

        title=Label(frame1, text="ABOUT", font=("times new roman",20, "bold"),bg="white", fg="#366F06").place(x=290,y=30)
        title1 = Label(frame1, text=message, font=("times new roman", 15), bg="white", fg="#366F06").place(
            x=10, y=100)
root = Tk()
obj = About(root)




def quit():
    answer = messagebox.askyesno('confirmation', 'Are you sure that you want to logout?')
    if answer:
        root.destroy()

def reg():
    root.destroy()
    import register

def log():
    root.destroy()
    import login

def about():
    x=0

def help():
    root.destroy()
    import help



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Register", command=reg)
filemenu.add_command(label="Login", command=log)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", command=about)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help",command=help)

root.config(menu=menubar)
menubar = Menu(root)
root.mainloop()


