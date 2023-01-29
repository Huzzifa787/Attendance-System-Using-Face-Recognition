from tkinter import *  # for GUI
from tkinter import ttk  # for stylish
from PIL import Image, ImageTk
from tkinter import messagebox


class Chatbot:

    def __init__(self, root):
        self.root = root
        self.root.geometry("730x620+320+40")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_fun)

        # ================== MAIN FRAME =======================
        main_frame = Frame(self.root, bd=4, bg='powder blue',
                           width=610)
        main_frame.pack()
        # ================== IMAGE  =======================
        img = Image.open(
            r"PICS\chatbot.png")
        img = img.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # ================= TITLE ==========================
        title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=720, compound=LEFT,
                            image=self.photoimg, text="Chat Me", font=('poppins', 40, 'bold'), fg='#034956', bg='white')
        title_label.pack(side=TOP)

        # ================== SCROLL BAR ========================
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=80, height=20, bd=3, relief=RAISED, font=(
            'poppins', 11), yscrollcommand=self.scroll_y)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # ================== BUTTON FRAME ======================
        btn_frame = Frame(self.root, bg="white",
                          width=720)
        btn_frame.pack()
        # ================== LABEL ======================
        label_1 = Label(btn_frame, text="Type Something", font=(
            'poppins', 14, 'bold'), fg='#fbec04', bg='#043b5c')
        label_1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.var_entry1  = StringVar()
        self.entry = ttk.Entry(btn_frame,textvariable=self.var_entry1, width=55, font=('poppins', 11))
        self.entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # ================== BUTTON ======================
        self.send = Button(btn_frame, command=self.send, text="Send", width=10, font=(
            'poppins', 11, 'bold'), fg="white", bg='#e66e2e', border=0, activebackground='#e66e2e', activeforeground='white')
        self.send.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.clr = Button(btn_frame,command=self.clear, text="Clear Chat", width=12, font=(
            'poppins', 11, 'bold'), fg="white", bg='#95190c', border=0, activebackground='#95190c', activeforeground='white')
        self.clr.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=(
            'poppins', 14, 'bold'), fg='#fbec04', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # ========================= FUNCTION DECLARATION ======================
    def enter_fun(self,event = ""):
        self.send.invoke()
        self.var_entry1.set('')
    #=================== CLEAR FUNCTION ==================
    def clear(self):
        self.text.delete('1.0',END)
        self.var_entry1.set('')
    #=================== SEND FUNCTION ==================
    def send(self):
        send = '\t\t\t'+'You:  '+self.entry.get()
        self.text.insert(END, '\n'+send)

        if self.entry.get() == '':
            self.msg = "Please, enter some Input"
            self.label_11.config(text=self.msg, fg='red', bg='white')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')
        if self.entry.get() == 'hello':
            self.text.insert(END, '\n\n'+'Bot : Hi')

        elif self.entry.get() == 'hi':
            self.text.insert(END, '\n\n'+'Bot : Hello')

        elif self.entry.get() == 'Fantastic':
            self.text.insert(END, '\n\n'+'Bot : Nice to Hear')

        elif self.entry.get() == 'What is your name ?':
            self.text.insert(END, '\n\n'+'Bot : My name is Alice')

        elif self.entry.get() == 'help':
            self.text.insert(
                END, '\n\n'+'Bot : yes, of course\n\n     1: What is Machine Learning?\n     2: What is Artifical Intelligence?\n     3: How does face Recongnition work?\n     4: Which algorithm did you used in your project?\n     5: What is meant by Haarsacde Open CV(Object Detection)?\n     6: What is meant by LBPH Opencv (Face Recognition)?\n     7: Link for reference.')

        elif self.entry.get() == '1':
            self.text.insert(
                END, '\n\n'+'Bot : Machine learning is a subfield of artificial intelligence\n         which is broadly defined as the capability of a machine \n         to imitate intelligent human behavior.')

        elif self.entry.get() == '2':
            self.text.insert(
                END, '\n\n'+'Bot : Artificial intelligence is the simulation\n         of human intelligence processes by machines,  \n         especially computer systems.')

        elif self.entry.get() == '3':
            self.text.insert(
                END, '\n\n'+'Bot : Facial Recongnition is a way of recognizing\n         a human face through technology.A facial \n         recognition system uses biometrics to map\n         facial features from a photograph or video.\n         It compares the information with a database\n        of known faces to find a match.')
        elif self.entry.get() == '4':
            self.text.insert(
                END, '\n\n'+'Bot : We have used two algorithms in our Project:\n\n         The first One is : Haarscade OpenCv (Object Detection) \n         The Second One is : LBPH OpenCv (Face Recognition)')
        elif self.entry.get() == '5':
            self.text.insert(
                END, '\n\n'+'Bot : Haar cascade is an algorithm that can detect \n         objects in images, irrespective of their scale \n         in image and location.This algorithm is not \n         so complex and can run in real-time. As we\n         are using for face detection so we use frontal \n         face in our project.')
        elif self.entry.get() == '6':
            self.text.insert(
                END, '\n\n'+'Bot : LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm \n         it is used to recognize the face of a person.It is known for its performance \n         and how it is able to recognize the face of a person from both front face and\n         side face.')
        elif self.entry.get() == '7':
            self.url = "https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b"
            self.text.insert(
                END, '\n\n'+self.url)


if __name__ == "__main__":

    root = Tk()
    obj = Chatbot(root)
    root.mainloop()
