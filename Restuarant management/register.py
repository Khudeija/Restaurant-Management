from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #Bg image
        self.bg=ImageTk.PhotoImage(file="images/bg.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, width=1350, height=700)

        # Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        title=Label(frame1, text="REGISTER HERE", font=("times new roman",20, "bold"),bg="white", fg="#366F06").place(x=50,y=30)
#ROW 1
        name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=50, y=100)
        self.txt_name= Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_name.place(x=50,y=130, width=250)

        staff = Label(frame1, text="Staff Position", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=370, y=100)
        self.txt_staff= ttk.Combobox(frame1, font=("times new roman",13), state="readonly", justify=CENTER)
        self.txt_staff['values']= ("Select", "Manager", "Assistant Manager", "Server")
        self.txt_staff.place(x=370,y=130, width=250)
        self.txt_staff.current(0)
#ROW 2

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=50, y=170)
        self.txt_email= Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_email.place(x=50,y=200, width=250)

        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=370, y=170)
        self.cmb_question= ttk.Combobox(frame1, font=("times new roman",13),state="readonly", justify=CENTER)
        self.cmb_question['values']= ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend's Name")
        self.cmb_question.place(x=370,y=200, width=250)
        self.cmb_question.current(0)
#ROW 3
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=50, y=240)
        self.txt_answer= Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_answer.place(x=50,y=270, width=250)

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="#5C3911").place(
            x=370, y=240)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.config(show="*")
        self.txt_password.place(x=370, y=270, width=250)

#Terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree to the Terms & Conditions",variable=self.var_chk ,onvalue=1, offvalue=0, bg="white", fg="#5C3911",font=("times new roman", 12)).place(x=50, y=320)

        btn=Button(frame1,text="Register",bd=0,cursor="hand2", bg="#366F06", fg="white", font=("times new roman",15), command=self.register_data).place(x=270, y=370, width=150)

        logintxt = Label(frame1, text="Already Registered?", font=("times new roman", 12), bg="white", fg="#5C3911").place(
            x=280, y=420)
        btn_login = Button(frame1, text="Login", command=self.login_win, bd=0, cursor="hand2", bg="#366F06", fg="white", font=("times new roman", 15)).place(
            x=270, y=450, width=150)

    def login_win(self):
        self.root.destroy()
        import login

    def clear(self):
        self.txt_name.delete(0,END)
        self.txt_staff.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)


    def register_data(self):
        if self.txt_name.get()=="" or self.txt_staff.get()=="Select" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" :
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree to the Terms and Conditions", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="restaurant")
                cur=con.cursor()
                cur.execute("select * from users where email=%s", self.txt_email.get())
                row=cur.fetchone()
                #if email already registered:
                if row!=None:
                    messagebox.showerror("Error", "User already exists. Please register with another email", parent=self.root)

                else:
                    cur.execute("insert into users (name,staff,email,question,answer,password) values (%s,%s,%s,%s,%s,%s)",
                                    (self.txt_name.get(),
                                     self.txt_staff.get(),
                                     self.txt_email.get(),
                                     self.cmb_question.get(),
                                     self.txt_answer.get(),
                                     self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)} ", parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()
