from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pymysql
import cv2
import os
import time 
import numpy as np


class face_recong:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition")

        #==================== Header Image =====================
        img = Image.open(
            r"PICS\face.png")
        img = img.resize((1400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-10, y=0)

        #==================== Title ============================
        title_lbl = Label(self.root, text="Welcome To Face Recongnition Page", font=(
            "poppins", 40, "bold"), fg="white", bg="#24162b", justify=CENTER)
        title_lbl.place(x=0, y=125, width=1530, height=60)

        #=================== BG IMAGE ==========================
        img1 = Image.open(
            r"PICS\bg2.jpg")
        img1 = img1.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=185, width=1530, height=710)

        #=================== BUTTONS ==============================

        std_img_btn = Image.open(r"PICS\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        b1 = Button(bg_img,command=self.face_recong, image=self.std_img1, cursor="hand2",
                    borderwidth=0)
        b1.place(x=600, y=135, width=180, height=180)

        b1_1 = Button(bg_img,command=self.face_recong, text="Face Recongnition",
                      cursor="hand2", font=("poppins", 13, "bold"), bg="#f26722", fg="white", borderwidth=0, activebackground="#f26722", activeforeground="white")
        b1_1.place(x=600, y=314, width=180, height=45)

    #=================== ATTENDANCE FUNCTION ============================
    def mark_attendance(self,n,r,k,l):
        with open("a.csv","r+",newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((n not in name_list) and (r not in name_list) and (k not in name_list) and (l not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r}, {k}, {n},{l}, {dtString}, {d1}, Present")

    #=================== FACE RECOGNITION FUNCTION ============================

    def face_recong(self):
        flag = 0
        def draw_boundary(img,Classifier,scaleFactor,minNeighbours,color,text,clf):
            
            gary_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = Classifier.detectMultiScale(
                gary_img, scaleFactor, minNeighbours)
            
            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict = clf.predict(gary_img[y:y+h,x:x+w])
                # print("PRDEICT :  ",predict)
                confidence = int((100*(1-predict/300)))
                # print("CONFIDENCE :  ",confidence)
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
                cursor = con.cursor()

                cursor.execute("select Name from student where Student_id="+str(id))
                n = cursor.fetchone()
                n = "+".join(n)

                cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute(
                    "select Reg_No from student where Student_id="+str(id))
                k = cursor.fetchone()
                k = "+".join(k)

                cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                l = cursor.fetchone()
                l = "+".join(l)

                if confidence > 77:
                    cv2.putText(
                        img, f"Student-ID:{r}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 2)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 2)
                    cv2.putText(
                        img, f"Reg-No:{k}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 2)
                    cv2.putText(
                        img, f"Dep:{l}", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 100, 0), 2)
                    self.mark_attendance(n, r, k,l)
                    
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, f"Unkown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                    # break
                    messagebox.showerror("Error","USER NOT EXIT",parent = self.root)
                    cv2.destroyAllWindows()
                coord = [x,y,w,y]
            return coord
        
        #============= FUNC ===========
        def recongnizer(img,clf,faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            # print("COORD :   ",coord)
            # cord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        cam = cv2.VideoCapture(0)

        while True:
            ret, img = cam.read()
            img = recongnizer(img,clf,faceCascade)
            # print("Image is :  ",img)
            cv2.imshow("Face Detector ",img)

            if cv2.waitKey(1) == 13:
                break
        cam.release()
        cv2.destroyAllWindows()
        


                    






if __name__ == "__main__":

    root = Tk()
    obj = face_recong(root)
    root.mainloop()
