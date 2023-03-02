from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class Help:
    def __init__(self,root):
        self.root=root
        self.root.title("Help Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #Bg image
        self.bg=ImageTk.PhotoImage(file="images/bg.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, width=1350, height=700)
        #ab = Label(self.root, text="About Us", font=("times new roman", 20, "bold"),
                      #fg="white", bg="none").place(x=50, y=30)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        message='''         To use this system,
        
        Click on the items checkbox, then insert the number of items ordered.
        
        Once all the items are ordered, click on total to view the total of all 
        subcategories and the final total.
        
        Click receipt to generate a receipt.
        
        Click save to save the order into the database.
        
        Click print to generate a printable receipt.
        
        Click reset to reset the system to start afresh.
        '''

        title=Label(frame1, text="HELP GUIDE", font=("times new roman",20, "bold"),bg="white", fg="#366F06").place(x=270,y=30)
        title1 = Label(frame1, text=message, font=("times new roman", 15), bg="white", fg="#366F06").place(
            x=40, y=100)
root = Tk()
obj = Help(root)



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
    root.destroy()
    import about


def help():
    x = 0

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
menubar.add_cascade(label="Help", command=help)

root.config(menu=menubar)
menubar = Menu(root)
root.mainloop()


