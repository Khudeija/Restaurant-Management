from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #Bg image
        self.bg=ImageTk.PhotoImage(file="images/bg.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, width=1350, height=700)

        # Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        title=Label(frame1, text="LOGIN HERE", font=("times new roman",20, "bold"),bg="white", fg="#366F06").place(x=50,y=30)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=250, y=150)
        self.txt_email= Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_email.place(x=250,y=180, width=250)



        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=250, y=240)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.config(show="*")
        self.txt_password.place(x=250, y=270, width=250)

        btn_login = Button(frame1, text="Login", bd=0, cursor="hand2", bg="#366F06", fg="white", command=self.login,
                           font=("times new roman", 15)).place(
            x=290, y=370, width=150)

        btn=Button(frame1,text="Register new Account?", command= self.register_win,bd=0,cursor="hand2", bg="white", fg="#5C3911", font=("times new roman",15)).place(x=265, y=450)


    def clear(self):
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)

    def register_win(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or  self.txt_password.get()=="" :
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="restaurant")
                cur=con.cursor()
                cur.execute("select * from users where email=%s and password=%s", (self.txt_email.get(), self.txt_password.get()))
                row=cur.fetchone()
                #if invalid details:
                if row==None:
                    messagebox.showerror("Error", "Invalid username and password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Login Successful", parent=self.root)
                    self.clear()
                    root.destroy()
                    import Restmanagement
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)} ", parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()
