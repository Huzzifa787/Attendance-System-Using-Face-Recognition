from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Face_Recongnition_System
import pymysql
import cv2
import numpy as np
import os


code = True


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Register_Window:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Register User")

        # ================== Variables

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_conatct = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securotyA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ==================  BG IMAGE
        self.bg = ImageTk.PhotoImage(
            file=r"PICS\reg.jpeg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ==================  LEFT IMAGE
        # self.bg1 = ImageTk.PhotoImage(
        #     file=r"PICS\new user.png")
        # lbl_bg1 = Label(self.root, image=self.bg1)
        # lbl_bg1.place(x=100, y=100, width=400, height=500)

        # ==================  main Frrame

        frame = Frame(self.root, bg="white")
        frame.place(x=290, y=120, width=800, height=530)

        register_lbl = Label(frame, text="REGISTRATION FORM", font=(
            "poppins", 25, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=200, y=10)

        # ==================  LABEL AND ENTRY FIELD

        # ==================  ROW 1
        fname = Label(frame, text="First Name:", font=(
            "poppins", 15, "bold"), bg="white")
        fname.place(x=32, y=75)

        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=(
            "poppins", 12))
        self.txt_fname.place(x=35, y=100, width=200)

        lname = Label(frame, text="Last Name:", font=(
            "poppins", 15, "bold"), bg="white")
        lname.place(x=442, y=75)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("poppins", 12))
        self.txt_lname.place(x=445, y=100, width=200)

        # ==================  ROW 2
        contact = Label(frame,  text="Contact No:", font=(
            "poppins", 15, "bold"), bg="white", fg="black")
        contact.place(x=30, y=140)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_conatct, font=("poppins", 12))
        self.txt_contact.place(x=35, y=170, width=200)

        email = Label(frame,  text="Email:", font=(
            "poppins", 15, "bold"), bg="white", fg="black")
        email.place(x=440, y=140)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("poppins", 12))
        self.txt_email.place(x=445, y=170, width=200)

        # ==================  ROW 3
        security_Q = Label(frame,  text="Select Security Question", font=(
            "poppins", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=30, y=220)

        self.combo_security_Q = ttk.Combobox(
            frame, textvariable=self.var_securityQ, font=("poppins", 12),state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "your birth palce", "Your Friend Name", "Your Father Name")
        self.combo_security_Q.place(x=35, y=250, width=200)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Secrity Answer", font=(
            "poppins", 15, "bold"), bg="white", fg="black")
        security_A.place(x=440, y=220)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securotyA,  font=("poppins", 12))
        self.txt_security.place(x=445, y=250, width=200)

        # ==================  ROW 4
        pswd = Label(frame,  text="Password:", font=(
            "poppins", 15, "bold"), bg="white", fg="black")
        pswd.place(x=32, y=305)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("poppins", 12))
        self.txt_pswd.place(x=35, y=340, width=200)

        confirm_pswd = Label(frame, text="Confirm Password:", font=(
            "poppins", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=442, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("poppins", 12))
        self.txt_confirm_pswd.place(x=445, y=340, width=200)

        # ==================  Check Button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text=" I Agree The Terms & Condition", font=(
            "poppins", 15, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=30, y=390)

        # ================== Register Buttons

        b1 = Button(frame, text="Register Now!", command=self.register_data, font=(
            "poppins", 15, "bold"), bd=0, relief=RIDGE, fg="white", bg="#00adb9", activeforeground="white", activebackground="#00adb9")
        b1.place(x=30, y=430, width=200)

        # ================== Login Buttons
        b1 = Button(frame, text="Back to Login", command=self.return_login, font=(
            "poppins", 15, "bold"), bd=0, relief=RIDGE, fg="white", bg="#b6833e", activeforeground="white", activebackground="#b6833e")
        b1.place(x=445, y=435, width=200)

    # ==================Functions

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.combo_security_Q.current(0)
        self.txt_security.delete(0, END)
        self.txt_pswd.delete(0, END)
        self.txt_confirm_pswd.delete(0, END)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password must be Same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please Agree Our Terms and Condition")
        else:
            #messagebox.showinfo("SUCCESS", "Welcome Friends")
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="project")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txt_email.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User alreday exit please try another email")
            else:
                my_cursor.execute("insert into register(fname,lname,contact,email,securityQ,securityA,password) values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_conatct.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securotyA.get(),
                    self.var_pass.get()
                ))

                messagebox.showinfo(
                    "SUCCESS", "REGISTER SUCCESSFULLY", parent=self.root)
                self.clear()
            conn.commit()
            conn.close()

    # ================== Return to Login page
    def return_login(self):
        self.root.destroy()


class Login_Window:

    def __init__(self, root):
        self.root = root
        self.root.geometry("340x450+560+170")
        self.root.title("Login")

        # ============================== BG IMAGE
        # self.bg = ImageTk.PhotoImage(
        #     file=r"PICS\login.jpg")
        # lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=0, y=0, width=340, height=450)

        img1 = Image.open(
            r"PICS\icon-removebg-preview.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=130, y=0, height=100, width=100)

        # ======================== Labels

        username = lbl = Label(frame, text="Email", font=(
            "poppins", 12, "bold"), fg="white", bg="black")
        username.place(x=40, y=145)

        self.txtuser = ttk.Entry(frame, font=("poppins", 11))
        self.txtuser.place(x=40, y=175, width=270, height=25)

        password = lbl = Label(frame, text="Password", font=(
            "poppins", 12, "bold"), fg="white", bg="black")
        password.place(x=40, y=220)

        self.txtpass = ttk.Entry(frame, font=("poppins", 11))
        self.txtpass.place(x=40, y=250, width=270, height=25)

        # ========================= ICON IMAGES

        img2 = Image.open(
            r"PICS\user.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg2.place(x=10, y=145, height=25, width=25)

        img3 = Image.open(
            r"PICS\pass.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg3.place(x=10, y=220, height=25, width=25)

        # ======================== Login Button

        loginbtn = Button(frame, text="Login", command=self.login, font=("poppins", 13, "bold"), bd=0,
                          relief=RIDGE, fg="white", bg="#b6833e", activeforeground="white", activebackground="#b6833e")
        loginbtn.place(x=40, y=315, width=270, height=35)

        # ======================= Reg Button

        regbtn = Button(frame, text="Register", command=self.register_window, font=("poppins", 11, "bold"),
                        borderwidth=0, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")
        regbtn.place(x=20, y=365, width=100, height=20)

        # ======================= Forgot Button

        forgotbtn = Button(frame, text="Forgot", command=self.forgot_password_window, font=("poppins", 11, "bold"),
                           borderwidth=0, relief=RIDGE, fg="white", bg="black", activebackground="black", activeforeground="white")
        forgotbtn.place(x=110, y=365, width=100, height=20)

    # =======================FUNCTIONS

    # ============= REGISTER WINDOW
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_Window(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Required for Login")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "123":
            messagebox.showinfo("SUCCESS", "WELCOME TO OFFICE")
        else:
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="project")
            cursor = conn.cursor()
            cursor.execute(
                "select * from register where email=%s and password=%s", (
                    self.txtuser.get(), self.txtpass.get()
                ))

            row = cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invaled Username and Password")
            else:
                open_main = messagebox.askyesno("YESNO", "Access Only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recongnition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


# =============================== RESET PASSWORD

    def reset_pass(self):
        if self.combo_security_Q == "Select":
            messagebox.showerror(
                "Error", "Select Security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror(
                "Error", "Please enter the Answer", parent=self.root2)
        elif self.txt_pass.get() == "":
            messagebox.showerror(
                "Error", "Please enter the New Password", parent=self.root2)
        else:
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="project")
            cursor = conn.cursor()
            cursor.execute(
                "select * from register where email=%s and securityQ=%s and securityA=%s", (
                    self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get()))
            row = cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Please enter Correct Answer", parent=self.root2)
            else:
                query = ("update register set password =%s and email = %s")
                value = (self.txt_pass.get(), self.txtuser.get())
                cursor.execute(query, value)
                conn.commit()
                conn.close()

                messagebox.showinfo(
                    "Info", "Your Password has been reset , try logging with your new password", parent=self.root2)
                self.root2.destroy()
# =============================== FORGOT PASSWORD

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Valid User Name")
        else:
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="project")
            cursor = conn.cursor()
            cursor.execute(
                "select * from register where email=%s", (
                    self.txtuser.get()))

            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter Valid UserName")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+560+170")

                l = Label(self.root2, text="Forgot Password", font=(
                    "poppins", 22, "bold"), fg="white", bg="#36151e")
                l.place(x=0, y=10, relwidth=1)
                security_Q = Label(self.root2,  text="Select Security Question", font=(
                    "poppins", 15, "bold"))
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(
                    self.root2, font=("poppins", 12))
                self.combo_security_Q["values"] = (
                    "Select", "your birth palce", "Your Friend Name", "Your Father Name")
                self.combo_security_Q.place(x=52, y=110, width=270, height=25)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Secrity Answer:", font=(
                    "poppins", 15, "bold"))
                security_A.place(x=50, y=160)

                self.txt_security = ttk.Entry(
                    self.root2,  font=("poppins", 12))
                self.txt_security.place(x=52, y=190, width=270, height=25)
                new_password = Label(self.root2, text="Enter New Password:", font=(
                    "poppins", 15, "bold"))
                new_password.place(x=50, y=250)

                self.txt_pass = ttk.Entry(
                    self.root2,  font=("poppins", 12))
                self.txt_pass.place(x=52, y=280, width=270)

                btn = Button(self.root2, command=self.reset_pass, text="Reset", font=(
                    "poppins", 15, "bold"), bg="#ab5567", fg="white", activebackground="#ab5567", activeforeground="white", borderwidth=0)
                btn.place(x=52, y=350, width=270, height=35)

    def fun(self):

        self.new_window = Toplevel(self.root)
        self.app = Face_Recongnition_System(self.new_window)


if __name__ == "__main__":

    main()
