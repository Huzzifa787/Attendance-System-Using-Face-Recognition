from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os
import cv2


class Student:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        # ==================== Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_reg = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # ================== Header Image
        img = Image.open(
            r"PICS\student.png")
        img = img.resize((1400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-10, y=0)

        # ================== BackGround Image

        img1 = Image.open(
            r"PICS\bg.jpeg")
        img1 = img1.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=185, width=1530, height=710)

        # ================== Title Label

        title_lbl = Label(self.root, text="Student Management System", font=(
            "poppins", 35, "bold"), fg="black", bg="#e3b505", justify=CENTER)
        title_lbl.place(x=0, y=125, width=1530, height=60)

        # ================== Main Frame

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=195, width=1300, height=520)

        # ================== Left Frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("poppins", 11, "bold"))
        left_frame.place(x=10, y=10, width=630, height=480)

        # ========== Current Courses

        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Courses Details", font=("poppins", 11, "bold"))
        current_course_frame.place(x=5, y=10, width=600, height=125)

        # ========= Department Label

        dep_label = Label(current_course_frame, text="Department", font=(
            "poppins", 11), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "poppins", 10), state="readonly", width=20)
        dep_combo['values'] = ("Select Department", "Mechanical",
                               "Civil", "Electrical", "Chemical", "Biomedical", "Computer Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # ========= Courses Label

        course_label = Label(current_course_frame, text="Course", font=(
            "poppins", 11), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "poppins", 10), state="readonly", width=20)
        course_combo['values'] = ("Select Courses", "BS(CS)",
                                  "BS(ME)", "BS(SE)", "BS(EE)", "BS(CHEM)", "BS(BME)")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # ========= Year Label

        year_label = Label(current_course_frame, text="Year", font=(
            "poppins", 11), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "poppins", 10), state="readonly", width=20)
        year_combo['values'] = ("Select Year", "2019",
                                "2020", "2021", "2022")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # ========= Semester Label

        semester_label = Label(current_course_frame, text="Semester", font=(
            "poppins", 11), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "poppins", 10), state="readonly", width=20)
        semester_combo['values'] = ("Select Semester", "1st semester",
                                    "5th semester", "6th semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # ========== Class Student Info

        class_Student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Student Information", font=("poppins", 11, "bold"))
        class_Student_frame.place(x=5, y=140, width=600, height=240)

        # ========== Student ID
        studentId_label = Label(class_Student_frame, text="Student ID:", font=(
            "poppins", 11), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=20, font=(
            "poppins", 10))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ========== Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=(
            "poppins", 11), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=15, font=(
            "poppins", 10))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # ========== Student Didvision
        student_div_label = Label(class_Student_frame, text="Class Section:", font=(
            "poppins", 11), bg="white")
        student_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        student_div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, font=(
            "poppins", 10), state="readonly", width=18)
        student_div_combo['values'] = ("Select Division", "A",
                                       "B", "C")
        student_div_combo.current(0)
        student_div_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # ========== Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=(
            "poppins", 11), bg="white")
        gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, font=(
            "poppins", 10), state="readonly", width=13)
        gender_combo['values'] = ("Select", "male",
                                  "female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # ========== Date of Birth
        dob_label = Label(class_Student_frame, text="DOB:", font=(
            "poppins", 11), bg="white")
        dob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=(
            "poppins", 10))
        dob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # ========== Reg No
        reg_label = Label(class_Student_frame, text="REG_NO:", font=(
            "poppins", 11), bg="white")
        reg_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        reg_entry = ttk.Entry(class_Student_frame, textvariable=self.var_reg, width=15, font=(
            "poppins", 10))
        reg_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # ========== Email
        email_label = Label(class_Student_frame, text="Email:", font=(
            "poppins", 11), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20, font=(
            "poppins", 10))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ========== Phone No
        phone_label = Label(class_Student_frame, text="Phone No:", font=(
            "poppins", 11), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=15, font=(
            "poppins", 10))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # ========== Teacher
        teacher_label = Label(class_Student_frame, text="Teacher Name :", font=(
            "poppins", 11), bg="white")
        teacher_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20, font=(
            "poppins", 10))
        teacher_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # ========== addrees
        address_label = Label(class_Student_frame, text="Address:", font=(
            "poppins", 11), bg="white")
        address_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=15, font=(
            "poppins", 10))
        address_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # =========== Radio Buttons

        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(
            class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=5, column=0)
        radionbtn2 = ttk.Radiobutton(
            class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=5, column=1)

        # ============= Buttons Frame

        btn_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=17, y=420, width=598, height=60)

        # ========= Save Button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", font=("poppins", 10, "bold"),
                          bg="#ff4c54", fg="white", activebackground="#ff4c54", activeforeground="white", width=7, borderwidth=0)
        save_btn.grid(row=0, column=0, padx=13, pady=15, sticky=W)

        # ========= Update Button
        update_btn = Button(btn_frame, command=self.update_data, text="Update", font=("poppins", 10, "bold"), bg="#2a6665",
                            fg="white", activebackground="#2a6665", activeforeground="white", width=7, borderwidth=0)
        update_btn.grid(row=0, column=1, padx=13, pady=15, sticky=W)

        # ========= Delete Button
        delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", font=("poppins", 10, "bold"), bg="red",
                            fg="white", activebackground="red", activeforeground="white", width=7, borderwidth=0)
        delete_btn.grid(row=0, column=2, padx=13, pady=15, sticky=W)

        # ========= Reset Button
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", font=("poppins", 10, "bold"), bg="#e3b505",
                           fg="white", activebackground="#e3b505", activeforeground="white", width=7, borderwidth=0)
        reset_btn.grid(row=0, column=3, padx=13, pady=15, sticky=W)

        # # ========== Take Photo

        take_photo_btn = Button(btn_frame, command=self.photo_sample, text="Take Photo", font=("poppins", 10, "bold"), bg="#e66e2e",
                                fg="white", activebackground="#e66e2e", activeforeground="white", width=10, borderwidth=0)
        take_photo_btn.grid(row=0, column=4, padx=13, pady=15, sticky=W)

        # # ========== Update Photo

        update_photo_btn = Button(btn_frame, command=self.photo_sample,  text="Update Photo", font=("poppins", 10, "bold"), bg="#0d11c7",
                                  fg="white", activebackground="#0d11c7", activeforeground="white", width=12, borderwidth=0)
        update_photo_btn.grid(row=0, column=5, padx=13, pady=15, sticky=W)

        # ================== Right Frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("poppins", 11, "bold"))
        right_frame.place(x=650, y=10, width=620, height=480)

        # =================== Search Frame

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search Information", font=("poppins", 11, "bold"))
        search_frame.place(x=5, y=10, width=600, height=80)

        # ===== Search Label
        search_label = Label(search_frame, text="Search By:", font=(
            "poppins", 11), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.var_search = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search, font=(
            "poppins", 10), state="read only", width=15)
        search_combo['values'] = ("Select", "Student-ID", "Name",
                                  "Email", "Reg_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        self.var_search_entry = StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_entry, width=15, font=(
            "poppins", 10))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # ===== Search Button
        search_btn = Button(search_frame, command=self.Search_data, text="Search", font=("poppins", 9, "bold"), bg="#ff4c54",
                            fg="white", activebackground="#ff4c54", activeforeground="white", width=8, borderwidth=0)
        search_btn.grid(row=0, column=3, padx=5, sticky=W)
        # ===== Show ALL Button
        showAll_btn = Button(search_frame, command=self.show_data, text="Show All", font=("poppins", 9, "bold"), bg="#2a6665",
                             fg="white", activebackground="#2a6665", activeforeground="white", width=8, borderwidth=0)
        showAll_btn.grid(row=0, column=4, padx=5, sticky=W)

        # =================== TABLE FRAME

        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=100, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_Table = ttk.Treeview(table_frame, columns=("id", "reg", "name", "dep", "div", "sem", "year", "course", "teacher", "gender",
                                                                "dob", "email", "phone", "address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_Table.xview)
        scroll_y.config(command=self.student_Table.yview)

        self.student_Table.heading("id", text="StudentId")
        self.student_Table.heading("reg", text="REG_NO")
        self.student_Table.heading("name", text="Name")
        self.student_Table.heading("dep", text="Department")
        self.student_Table.heading("div", text="Division")
        self.student_Table.heading("sem", text="Semester")
        self.student_Table.heading("year", text="Year")
        self.student_Table.heading("course", text="Course")
        self.student_Table.heading("teacher", text="Teacher")
        self.student_Table.heading("gender", text="Gender")
        self.student_Table.heading("dob", text="DOB")
        self.student_Table.heading("email", text="Email")
        self.student_Table.heading("phone", text="Phone")
        self.student_Table.heading("address", text="Address")
        self.student_Table.heading("photo", text="PhotoSampleStatus")
        self.student_Table['show'] = "headings"

        self.student_Table.column("id", width=100)
        self.student_Table.column("reg", width=100)
        self.student_Table.column("name", width=100)
        self.student_Table.column("dep", width=100)
        self.student_Table.column("div", width=100)
        self.student_Table.column("sem", width=100)
        self.student_Table.column("year", width=100)
        self.student_Table.column("course", width=100)
        self.student_Table.column("teacher", width=100)
        self.student_Table.column("gender", width=100)
        self.student_Table.column("dob", width=100)
        self.student_Table.column("email", width=100)
        self.student_Table.column("phone", width=100)
        self.student_Table.column("address", width=100)
        self.student_Table.column("photo", width=150)

        self.student_Table.pack(fill=BOTH, expand=1)
        self.student_Table.bind("<ButtonRelease>", self.get_cursor)
        self.show_data()
    # ============================== FUNCTIONS

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror(
                "Error", "ALL fields required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
                cursor = conn.cursor()
                cursor.execute(
                    "insert into student(Student_id,Reg_No,Name,Dep,Division,Semester,Year,course,Teacher,Gender,Dob,Email,Phone,Address,PhotoSample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_std_id.get(),
                        self.var_reg.get(),
                        self.var_std_name.get(),
                        self.var_dep.get(),
                        self.var_div.get(),
                        self.var_semester.get(),
                        self.var_year.get(),
                        self.var_course.get(),
                        self.var_teacher.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get()

                    ))
                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo(
                    "SUCCESS", "Student has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

    # ========================== FETCH DATA

    def show_data(self):
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="project")
        cursor = conn.cursor()
        cursor.execute("select * from student")
        data = cursor.fetchall()

        if len(data) != 0:
            self.student_Table.delete(*self.student_Table.get_children())
            for i in data:
                self.student_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ================== GET CURSOR

    def get_cursor(self, event=""):
        cursor_focus = self.student_Table.focus()
        content = self.student_Table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_reg.set(data[1]),
        self.var_std_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_div.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_year.set(data[6]),
        self.var_course.set(data[7]),
        self.var_teacher.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_email.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_address.set(data[13]),
        self.var_radio1.set(data[14])

    # ======================= UPDATE DATA =================================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror(
                "Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student detail", parent=self.root)
                if Update > 0:
                    conn = pymysql.connect(
                        host="localhost", user="root", password="", database="project")
                    cursor = conn.cursor()
                    cursor.execute("update student set Reg_No=%s, Name=%s,Dep=%s,Division=%s,Semester=%s,Year=%s,course=%s,Teacher=%s,Dob=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s", (
                        self.var_reg.get(),
                        self.var_std_name.get(),
                        self.var_dep.get(),
                        self.var_div.get(),
                        self.var_semester.get(),
                        self.var_year.get(),
                        self.var_course.get(),
                        self.var_teacher.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
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

    # ================ DELETE FUNCTION
    def delete_data(self):
        if self.var_std_id == "":
            messagebox.showerror(
                "Error", "Student ID must be required", parent=self.root)

        else:
            try:
                Delete = messagebox.askyesno(
                    "Delete", "Do you want to delete this student detail", parent=self.root)
                if Delete > 0:
                    conn = pymysql.connect(
                        host="localhost", user="root", password="", database="project")
                    cursor = conn.cursor()
                    sql = ("delete from student where Student_id=%s")
                    value = (self.var_std_id.get())
                    cursor.execute(sql, value)
                    try:
                        for x in range(1,101):
                            os.remove("data/user."+str(value)+"."+str(x)+".jpg")
                    except:
                        messagebox.showinfo(
                    "Info", "Photo Sample against that id does not Exit", parent=self.root)
                else:
                    if not Delete:
                        return
                messagebox.showinfo(
                    "STUDENT DELETE PAGE", "STUDENT DETAILS HAS BEEN SUCCESSFULLY DELETED", parent=self.root)
                conn.commit()
                self.show_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)

    # =============== RESET DATA

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Courses"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_reg.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_teacher.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")

    # ===================== SEARCH DATA =============
    def Search_data(self):
        if self.var_search.get() == "Select" or self.var_search_entry == "":
            messagebox.showerror("Error", "Select any one option in combo box")
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
                cursor = con.cursor()
                if self.var_search.get() == "Student-ID":
                    sql = "select * from student where Student_id='" + \
                        str(self.var_search_entry.get())+"'"
                    cursor.execute(sql)
                elif self.var_search.get() == "Name":
                    sql = "select * from student where Name='" + \
                        str(self.var_search_entry.get())+"'"
                    cursor.execute(sql)
                elif self.var_search.get() == "Reg_No":
                    sql = "select * from student where Reg_No='" + \
                        str(self.var_search_entry.get())+"'"
                    cursor.execute(sql)
                else:
                    sql = "select * from student where Email='" + \
                        str(self.var_search_entry.get())+"'"
                    cursor.execute(sql)
                row = cursor.fetchall()
                if len(row) != 0:
                    self.student_Table.delete(
                        *self.student_Table.get_children())
                    for i in row:
                        self.student_Table.insert("", END, values=i)
                if len(row) == 0:
                    messagebox.showerror(
                        "Error", "Data Not Found!!!!!!!!!", parent=self.root)
                    con.commit()
                con.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ===================================== TAKE PHOTO SAMPLE

    def photo_sample(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror(
                "Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="project")
                my_cursor = con.cursor()
                my_cursor.execute("select * from student where Student_id=%s",(self.var_std_id.get()))
                result = my_cursor.fetchone()
                r  = self.var_std_id.get()
                id = r
                # for x in result:
                #     id += 1
                my_cursor.execute("update student set Reg_No=%s, Name=%s,Dep=%s,Division=%s,Semester=%s,Year=%s,course=%s,Teacher=%s,Dob=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s", (
                    self.var_reg.get(),
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_div.get(),
                    self.var_semester.get(),
                    self.var_year.get(),
                    self.var_course.get(),
                    self.var_teacher.get(),
                    self.var_dob.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))
                con.commit()
                self.show_data()
                self.reset_data()
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
                        file_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
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


if __name__ == "__main__":

    root = Tk()
    obj = Student(root)
    root.mainloop()
