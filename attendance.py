from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime
import numpy as np


mydata = []


class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Page")

        # ==================== Variables =======================
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_reg = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attend = StringVar()

        # ==================== Header Image =====================
        img = Image.open(
            r"PICS\attendance.png")
        img = img.resize((1400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-10, y=0)

        # =================== BG IMAGE ==========================
        image1 = Image.open(
            r"PICS\bg2.jpg")
        image1 = image1.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(image1)

        bg_img = Label(self.root, image=self.photoimg12)
        bg_img.place(x=0, y=185, width=1530, height=710)

        # ==================== Title ============================
        title_lbl = Label(self.root, text="Welcome To Attendance Page", font=(
            "poppins", 40, "bold"), fg="white", bg="#d65f82", justify=CENTER)
        title_lbl.place(x=0, y=125, width=1530, height=60)

        # ================== Main Frame ========================

        main_frame = Frame(self.root, bd=2, bg='white')
        main_frame.place(x=30, y=190, width=1290, height=520)

        # ================== Left Frame ========================

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("poppins", 11, "bold"))
        left_frame.place(x=10, y=10, width=630, height=480)

        # ================== PIC Frame ========================

        img1 = Image.open(
            r"PICS\attend.png")
        img1 = img1.resize((610, 145), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        t_lbl = Label(left_frame, image=self.photoimg1)
        t_lbl.place(x=10, y=10)

        # ================== Detail Frame ========================

        detail_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Details", font=("poppins", 11, "bold"))
        detail_frame.place(x=15, y=195, width=620, height=250)

        # ========== Student ID =================
        studentId_label = Label(detail_frame, text="Student ID:", font=(
            "poppins", 11), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(detail_frame, textvariable=self.var_std_id, width=50, font=(
            "poppins", 10))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ========== REG NO =================
        studentName_label = Label(detail_frame, text="REG_No:", font=(
            "poppins", 11), bg="white")
        studentName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(detail_frame, textvariable=self.var_reg, width=50, font=(
            "poppins", 10))
        studentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # ========== Student Name =====================
        reg_label = Label(detail_frame, text="Student Name:", font=(
            "poppins", 11), bg="white")
        reg_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        reg_entry = ttk.Entry(detail_frame, textvariable=self.var_std_name, width=50, font=(
            "poppins", 10))
        reg_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # ========== Department =====================
        attend_combo_label = Label(detail_frame, text="Department:", font=(
            "poppins", 11), bg="white")
        attend_combo_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        attend_combo = ttk.Combobox(detail_frame, textvariable=self.var_dep, width=48, font=(
            "poppins", 10), state="readonly")
        attend_combo["values"] = ("Select", "CS", "ME", "EE", "BME", "CHEM")
        attend_combo.current(0)
        attend_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ========== Time =====================
        time_label = Label(detail_frame, text="Time:", font=(
            "poppins", 11), bg="white")
        time_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(detail_frame, textvariable=self.var_time, width=50, font=(
            "poppins", 10))
        time_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # ========== Date =====================
        date_label = Label(detail_frame, text="Date:", font=(
            "poppins", 11), bg="white")
        date_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(detail_frame, textvariable=self.var_date, width=50, font=(
            "poppins", 10))
        date_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # ========== Attendance =====================
        attend_combo_label = Label(detail_frame, text="Attendance:", font=(
            "poppins", 11), bg="white")
        attend_combo_label.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        attend_combo = ttk.Combobox(detail_frame, textvariable=self.var_attend, width=48, font=(
            "poppins", 10), state="readonly")
        attend_combo["values"] = ("Status", "Present", "Absent", "Leave")
        attend_combo.current(0)
        attend_combo.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # ================= BUTTONS ==========================
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=3, y=417, width=620, height=38)

        # ================== IMPORT BUTTON ===================
        import_btn = Button(btn_frame, command=self.import_csv, text="Import", font=("poppins", 12, "bold"),
                            bg="#ff4c54", fg="white", activebackground="#ff4c54", activeforeground="white", width=13, borderwidth=0)
        import_btn.grid(row=0, column=0, padx=9, pady=3, sticky=W)

        # ================== EXPORT BUTTON ===================
        export_btn = Button(btn_frame, command=self.export_data, text="Export", font=("poppins", 12, "bold"), bg="#2a6665",
                            fg="white", activebackground="#2a6665", activeforeground="white", width=13, borderwidth=0)
        export_btn.grid(row=0, column=1, padx=9, pady=3, sticky=W)

        # ================== UPDATE BUTTON ===================
        export_btn = Button(btn_frame, command=self.update_data, text="UPDATE", font=("poppins", 12, "bold"), bg="#f26722",
                            fg="white", activebackground="#f26722", activeforeground="white", width=13, borderwidth=0)
        export_btn.grid(row=0, column=2, padx=9, pady=3, sticky=W)

        # ================== Reset BUTTON ===================
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", font=("poppins", 12, "bold"), bg="#e3b505",
                           fg="white", activebackground="#e3b505", activeforeground="white", width=13, borderwidth=0)
        reset_btn.grid(row=0, column=3, padx=9, pady=3, sticky=W)

        # ================== RIGHT Frame ========================

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("poppins", 11, "bold"))
        right_frame.place(x=650, y=10, width=630, height=480)

        # ========== Table Frame =====================
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=10, width=610, height=445)

        # ============= SCROLL BAR ============
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # ============ CREATE TABLE ==================
        self.attendance_report_right = ttk.Treeview(table_frame, columns=(
            "ID", "Reg_No", "Name", "Dep", "Time", "Date", "Attend"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_report_right.xview)
        scroll_y.config(command=self.attendance_report_right.yview)

        self.attendance_report_right.heading("ID", text="Student_ID")
        self.attendance_report_right.heading("Reg_No", text="Reg_No")
        self.attendance_report_right.heading("Name", text="Student_Name")
        self.attendance_report_right.heading("Dep", text="Department")
        self.attendance_report_right.heading("Time", text="Time")
        self.attendance_report_right.heading("Date", text="Date")
        self.attendance_report_right.heading(
            "Attend", text="Attendance_status")
        self.attendance_report_right["show"] = "headings"

        self.attendance_report_right.column("ID", width=100)
        self.attendance_report_right.column("Reg_No", width=100)
        self.attendance_report_right.column("Name", width=100)
        self.attendance_report_right.column("Dep", width=100)
        self.attendance_report_right.column("Time", width=100)
        self.attendance_report_right.column("Date", width=100)
        self.attendance_report_right.column("Attend", width=120)
        self.attendance_report_right.pack(fill=BOTH, expand=1)
        self.attendance_report_right.bind(
            "<ButtonRelease>", self.get_cursor_up)
        # self.show_data()
    # ===================== FUNCTIONS ====================================

    # ================ SHOW DATA =================
    def show_data(self):
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="project")
        cursor = conn.cursor()
        cursor.execute("select * from attendance")
        data = cursor.fetchall()
        # print(data)
        if len(data) != 0:
            self.attendance_report_right.delete(
                *self.attendance_report_right.get_children())
            for i in data:
                self.attendance_report_right.insert("", END, values=i)
            conn.commit()
            conn.close()
        else:
            self.attendance_report_right.delete(
                *self.attendance_report_right.get_children())
            self.attendance_report_right.insert("", END)
            conn.commit()
            conn.close()

    # ================ IMPORT DATA =================
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)

        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="project")
            cursor = conn.cursor()
            for i in csvread:
                mydata.append(i)
        # print(mydata)
        self.add_data()
        self.show_data()
        # self.delete_data()

    # =================== EXPORT DATA =====================

    def export_data(self):
        global mydata
        # mydata.clear()
        # data = []
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                conn = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
                cursor = conn.cursor()
                cursor.execute("select * from attendance")
                data = cursor.fetchall()
                for i in data:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export", "Your Data  Exported to Successfully", parent=self.root)
                conn.commit()
                self.delete_data()
                temp = list(data)
                temp.clear()
                self.show_data()
                conn.close()

            # self.show_data()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to : {str(es)}", parent=self.root)
    # ========================= INSERT =========================

    def add_data(self):
        global mydata
        for i in mydata:
            # print(i)
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="project")
            cursor = conn.cursor()
            cursor.execute("insert into attendance(std_id,std_reg,std_name,dep,time,date,attend_status) values(%s,%s,%s,%s,%s,%s,%s)", (
                i
            ))
            conn.commit()
            conn.close()

    # ========================= UPDATE =========================

    def update_data(self):
        try:
            Update = messagebox.askyesno(
                "Update", "Do you want to update this detail", parent=self.root)
            if Update > 0:
                conn = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
                cursor = conn.cursor()
                cursor.execute("update attendance set std_reg=%s,std_name=%s,dep=%s,time=%s,date=%s,attend_status=%s where std_id = %s", (
                    self.var_reg.get(),
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_std_id.get(),
                ))
            else:
                if not Update:
                    return
            messagebox.showinfo(
                "SUCCESS", "STUDENT DETAILS HAS BEEN SUCCESSFULLY UPDATED", parent=self.root)
            conn.commit()
            self.show_data()
            conn.close()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to : {str(es)}", parent=self.root)

    # ========================= Delete =========================

    def delete_data(self):
        # for i in mydata:
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="project")
        cursor = conn.cursor()
        cursor.execute("delete from attendance")
        # messagebox.showinfo(
        #     "SUCCESS", "STUDENT DETAILS HAS BEEN SUCCESSFULLY UPDATED", parent=self.root)
        conn.commit()
        # self.show_data()
        conn.close()

    # ====================== GET CURSOR FUNCTION =======================
    def get_cursor_up(self, event=""):
        cursor_row = self.attendance_report_right.focus()
        content = self.attendance_report_right.item(cursor_row)
        row = content['values']

        self.var_std_id.set(row[0])
        self.var_reg.set(row[1])
        self.var_std_name.set(row[2])
        self.var_dep.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attend.set(row[6])

    # =================== RESET DATA =====================

    def reset_data(self):
        self.var_std_id.set("")
        self.var_reg.set("")
        self.var_std_name.set("")
        self.var_dep.set("Select")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")


if __name__ == "__main__":

    root = Tk()
    obj = Attendance(root)
    root.mainloop()
