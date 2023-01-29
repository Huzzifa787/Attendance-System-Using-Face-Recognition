from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import numpy as np


class Register_Window:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Register User")

        # ================== Variables

        self.var_id = StringVar()
        self.var_name = StringVar()
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
        fname = Label(frame, text="ID:", font=(
            "poppins", 15, "bold"), bg="white")
        fname.place(x=32, y=75)

        self.txt_fname = ttk.Entry(frame, textvariable=self.var_id, font=(
            "poppins", 12))
        self.txt_fname.place(x=35, y=100, width=200)

        lname = Label(frame, text="Name:", font=(
            "poppins", 15, "bold"), bg="white")
        lname.place(x=442, y=75)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_name, font=("poppins", 12))
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
            frame, textvariable=self.var_securityQ, font=("poppins", 12))
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
        # ================== Take Photo Buttons
        b1 = Button(frame, text="Take Photo",command=self.photo_sample, font=(
            "poppins", 15, "bold"), bd=0, relief=RIDGE, fg="white", bg="#584942", activeforeground="white", activebackground="#584942")
        b1.place(x=445, y=430, width=120)

        # ================== Train Photo Buttons
        b1 = Button(frame, text="Train Data",command=self.train_data, font=(
            "poppins", 15, "bold"), bd=0, relief=RIDGE, fg="white", bg="#034956", activeforeground="white", activebackground="#034956")
        b1.place(x=600, y=430, width=120)

        # ================== Login Buttons
        b1 = Button(frame, text="Back to Login", command=self.return_login, font=(
            "poppins", 15, "bold"), bd=0, relief=RIDGE, fg="white", bg="#b6833e", activeforeground="white", activebackground="#b6833e")
        b1.place(x=445, y=480, width=275)

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
        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_securityQ.get() == "Select":
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
                my_cursor.execute("insert into register(id,name,contact,email,securityQ,securityA,password) values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_name.get(),
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
    # ================== PHOTO SAMPLE
    def photo_sample(self):
        try:
            con = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
            my_cursor = con.cursor()
            my_cursor.execute(
                    "select * from register ")
            result = my_cursor.fetchall()
            r = self.var_id.get()
            id = r
            con.commit()
            con.close()
                #====== FACE DETECTION============#
            face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

            def face_croped(img):
                    # conver gary sacle
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum naber 5
                for (x, y, w, h) in faces:
                        face_croped = img[y:y+h, x:x+w]
                        return face_croped
            cam = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cam.read()
                if face_croped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_croped(my_frame), (500, 500))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_path = "admin/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 100, 0), 2)
                    cv2.imshow("Capture Images", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
            cam.release()
            cv2.destroyAllWindows()
            messagebox.showinfo(
                    "Result", "Generating dataset completed!", parent=self.root)
        except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    def train_data(self):
        data_dir = ("admin")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # convert into Gray Scale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # =============== Train Classifier ======================

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf1.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training Dataset Completed !!!!!!!!!!!!!!", parent=self.root)



if __name__ == "__main__":

    root = Tk()
    app = Register_Window(root)
    root.mainloop()
