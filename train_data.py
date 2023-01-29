from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import numpy as np


class Train_data:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")

        # ==================== Header Image =====================
        img = Image.open(
            r"PICS\train.png")
        img = img.resize((1400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-10, y=0)

        # ==================== Title ============================
        title_lbl = Label(self.root, text="Welcome To Train Dataset", font=(
            "poppins", 40, "bold"), fg="white", bg="#f26722", justify=CENTER)
        title_lbl.place(x=0, y=125, width=1530, height=60)

        # =================== BG IMAGE ==========================
        img1 = Image.open(
            r"PICS\bg.jpeg")
        img1 = img1.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=185, width=1530, height=710)

        # =================== BUTTONS ==============================

        std_img_btn = Image.open(r"PICS\t_btn1.png")
        std_img_btn = std_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        b1 = Button(bg_img, command=self.train_data, image=self.std_img1, cursor="hand2",
                    borderwidth=0)
        b1.place(x=600, y=150, width=180, height=180)

        b1_1 = Button(bg_img, command=self.train_data, text="Train Dataset",
                      cursor="hand2", font=("poppins", 13, "bold"), bg="#b6833e", fg="white", borderwidth=0, activebackground="#b6833e", activeforeground="white")
        b1_1.place(x=600, y=325, width=180, height=45)

        # =================== FUNCTION For Training ====================
    def train_data(self):
        data_dir = ("data")
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
        clf.train(faces, ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training Dataset Completed !!!!!!!!!!!!!!", parent=self.root)


if __name__ == "__main__":

    root = Tk()
    obj = Train_data(root)
    root.mainloop()
