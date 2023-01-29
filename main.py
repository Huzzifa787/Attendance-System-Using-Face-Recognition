from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
from student import Student
from train_data import Train_data
from face_recong import face_recong
from developers import Developer
from attendance import Attendance
from helpdesk import HelpDesk
import os


class Face_Recongnition_System:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        # ================== Header Image =======================
        img = Image.open(
            r"PICS\header.png")
        img = img.resize((1400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-10, y=0)

        # ================== BackGround Image ===================

        img1 = Image.open(
            r"PICS\bg2.jpg")
        img1 = img1.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=132, width=1530, height=710)

        # ================== Title Label =======================

        title1_lbl = Label(bg_img, text="Student Attendance System Using Face Recongnition", font=(
            "poppins", 30, "bold"), fg="white", bg="#ab5567")
        title1_lbl.place(x=0, y=-10, width=1530, height=60)

        # ================= Student Button ======================

        img3 = Image.open(
            r"PICS\s.jpg")
        img3 = img3.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(self.root, command=self.student_detail, image=self.photoimg3,
                    cursor="hand2", activebackground="darkblue", borderwidth=0)
        b1.place(x=200, y=250, width=150, height=150)

        b1_1 = Button(self.root, command=self.student_detail,  text="Student Details", cursor="hand2", font=(
            "poppins", 11, "bold"), fg="white", background="#613f75", activeforeground="white", activebackground="#613f75", borderwidth=0)
        b1_1.place(x=200, y=400, width=151, height=40)

        # ================= Face Detector Button ================

        img4 = Image.open(
            r"PICS\det1.jpg")
        img4 = img4.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2 = Button(self.root, command=self.face_recong, image=self.photoimg4, cursor="hand2", activebackground="darkblue",
                    borderwidth=0)
        b2.place(x=500, y=250, width=150, height=150)

        b2_1 = Button(self.root, command=self.face_recong, text="Face Detector", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#034956", activeforeground="white", activebackground="#034956", borderwidth=0)
        b2_1.place(x=500, y=400, width=150, height=40)

        # ================= Attendance Button ========================

        img5 = Image.open(
            r"PICS\att.jpg")
        img5 = img5.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b3 = Button(self.root, command=self.attendance, image=self.photoimg5, cursor="hand2",
                    borderwidth=0, activebackground="darkblue")
        b3.place(x=800, y=250, width=150, height=150)

        b3_1 = Button(self.root, command=self.attendance, text="Attendance", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#f26722", activeforeground="white", activebackground="#f26722", borderwidth=0)
        b3_1.place(x=800, y=400, width=150, height=40)

        # ================= Train Data Button ======================

        img6 = Image.open(
            r"PICS\tra1.jpg")
        img6 = img6.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b4 = Button(self.root, command=self.train_data, image=self.photoimg6, cursor="hand2",
                    borderwidth=0, activebackground="darkblue")
        b4.place(x=200, y=500, width=150, height=150)

        b4_1 = Button(self.root, command=self.train_data, text="Train Data", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#5d2e46", activeforeground="white", activebackground="#5d2e46", borderwidth=0)
        b4_1.place(x=200, y=640, width=150, height=40)

        # ================= Photos Button =====================

        img7 = Image.open(
            r"PICS\photo.jpeg")
        img7 = img7.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b5 = Button(self.root, command=self.open_photos, image=self.photoimg7, cursor="hand2",
                    borderwidth=0, activebackground="darkblue")
        b5.place(x=500, y=500, width=150, height=150)

        b5_1 = Button(self.root, command=self.open_photos, text="Photos", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#65743a", activeforeground="white", activebackground="#65743a", borderwidth=0)
        b5_1.place(x=500, y=640, width=150, height=40)

        # ================= Help Button =====================

        img8 = Image.open(
            r"PICS\hlp.jpg")
        img8 = img8.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b6 = Button(self.root, command=self.help, image=self.photoimg8, cursor="hand2",
                    activebackground="darkblue", borderwidth=0)
        b6.place(x=800, y=500, width=150, height=150)

        b6_1 = Button(self.root, command=self.help, text="Help Desk", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#be5683", activeforeground="white", activebackground="#be5683", borderwidth=0)
        b6_1.place(x=800, y=640, width=150, height=40)

        # ================= Developer Button ====================

        img9 = Image.open(
            r"PICS\dev.jpg")
        img9 = img9.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(self.root, command=self.developer, image=self.photoimg9, cursor="hand2",
                    borderwidth=0, activebackground="darkblue")
        b6.place(x=1050, y=250, width=150, height=150)

        b6_1 = Button(self.root, command=self.developer, text="Developer", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#b6833e", activeforeground="white", activebackground="#b6833e", borderwidth=0)
        b6_1.place(x=1050, y=400, width=150, height=40)

        # ================= Exit Button ====================

        img10 = Image.open(
            r"PICS\exi.jpg")
        img10 = img10.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(self.root, command=self.exit, image=self.photoimg10, cursor="hand2",
                    borderwidth=0, activebackground="darkblue")
        b7.place(x=1050, y=500, width=150, height=150)

        b7_1 = Button(self.root, command=self.exit, text="Exit", cursor="hand2", font=("poppins", 11, "bold"),
                      fg="white", background="#95190c", activeforeground="white", activebackground="#95190c", borderwidth=0)
        b7_1.place(x=1050, y=640, width=150, height=40)

    # ================== STUDENT DETAIL FUNCTION  ====================

    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # ================== TRAIN DATA FUNCTION  ====================

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train_data(self.new_window)

    # ================== FACE RECOGNITION FUNCTION  ====================

    def face_recong(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recong(self.new_window)

    # ==================== PHOTOS FUNCTIONS ====================

    def open_photos(self):
        os.startfile("data")

    # ================== ATTENDANCE FUNCTION  ====================

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    # ================== DEVLOPER FUNCTION  ====================

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    # ================== Help Desk Page  ====================

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = HelpDesk(self.new_window)

    # ================== EXIT FUNCTION  ====================

    def exit(self):
        self.iexit = messagebox.askyesno(
            "YESORNO", "Do you want to exit", parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":

    root = Tk()
    obj = Face_Recongnition_System(root)
    root.mainloop()
