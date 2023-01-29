from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser


class HelpDesk:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk Page")

        # ==================== Header Image =====================
        img = Image.open(
            r"PICS\help.png")
        img = img.resize((1400, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-10, y=0)

        # ==================== Title ============================
        title_lbl = Label(self.root, text="Welcome To Help Desk Page", font=(
            "poppins", 40, "bold"), fg="white", bg="#433d25", justify=CENTER)
        title_lbl.place(x=0, y=125, width=1530, height=60)

        # =================== BG IMAGE ==========================
        img1 = Image.open(
            r"PICS\bg4.png")
        img1 = img1.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=185, width=1530, height=710)

        # ================== BUTTONS 1 ===========================
        std_img1_btn = Image.open(r"PICS\web.png")
        std_img1_btn = std_img1_btn.resize(
            (180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img1_btn)

        b1 = Button(bg_img, command=self.fun, image=self.std_img1, cursor="hand2",
                    borderwidth=0)
        b1.place(x=300, y=135, width=180, height=180)

        b1_1 = Button(bg_img, command=self.fun, text="Google",
                      cursor="hand2", font=("poppins", 12, "bold"), bg="#ef436b", fg="white", borderwidth=0, activebackground="#ef436b", activeforeground="white")
        b1_1.place(x=300, y=314, width=180, height=45)

        # ================== BUTTONS 2 ===========================
        std_img2_btn = Image.open(r"PICS\yt.png")
        std_img2_btn = std_img2_btn.resize(
            (180, 180), Image.Resampling.LANCZOS)
        self.std_img2 = ImageTk.PhotoImage(std_img2_btn)

        b2 = Button(bg_img, command=self.fun1, image=self.std_img2, cursor="hand2",
                    borderwidth=0)
        b2.place(x=600, y=135, width=180, height=180)

        b2_1 = Button(bg_img, command=self.fun1, text="Youtube",
                      cursor="hand2", font=("poppins", 12, "bold"), bg="#05c793", fg="white", borderwidth=0, activebackground="#05c793", activeforeground="white")
        b2_1.place(x=600, y=314, width=180, height=45)

        # ================== BUTTONS 3 ===========================
        std_img3_btn = Image.open(r"PICS\gmail.png")
        std_img3_btn = std_img3_btn.resize(
            (180, 180), Image.Resampling.LANCZOS)
        self.std_img3 = ImageTk.PhotoImage(std_img3_btn)

        b3 = Button(bg_img, command=self.fun2, image=self.std_img3, cursor="hand2",
                    borderwidth=0)
        b3.place(x=900, y=135, width=180, height=180)

        b3_1 = Button(bg_img, command=self.fun2, text="Contact Us",
                      cursor="hand2", font=("poppins", 12, "bold"), bg="#ff9000", fg="white", borderwidth=0, activebackground="#ff9000", activeforeground="white")
        b3_1.place(x=900, y=314, width=180, height=45)

    # ================= FUNCTION ===========================
    def fun(self):
        self.new = 1
        self.url = "https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b"
        webbrowser.open(self.url, new=self.new)
        

    # ================= FUNCTION ===========================
    def fun1(self):
        self.new = 1
        self.url = "https://youtu.be/sz25xxF_AVE"
        webbrowser.open(self.url, new=self.new)

    # ================= FUNCTION ===========================
    def fun2(self):
        self.new = 1
        self.url = "www.gmail.com"
        webbrowser.open(self.url, new=self.new)


if __name__ == "__main__":

    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()
