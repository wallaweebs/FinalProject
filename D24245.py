import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry

# group notes


logScreen = Tk()
logScreen.geometry("800x830+360+40")
logScreen.title("Patient File")

profilePic = PhotoImage(file="placeholder.png")
resizedPfp = profilePic.subsample(3, 3)
pic = Label(logScreen, image=resizedPfp).place(x=0, y=0)

b1 = Button(logScreen, text='Upload Photo', command = lambda:upload_file()).place(x=40, y=210)

Label(logScreen, text="First Name:").place(x=230, y=20)
Label(logScreen, text="Last Name:").place(x=520, y=20)
Label(logScreen, text="MRN:").place(x=25, y=255)
Label(logScreen, text="Date of Birth:").place(x=230, y=70)
birth = DateEntry(logScreen, width= 9, background= "blue", foreground= "white",bd=2, pady=20, year = 2001, month = 1, day = 1).place(x=320, y=68)

Label(logScreen, text="Admission Date:").place(x=520, y=70)
admit = DateEntry(logScreen, width= 9, background= "blue", foreground= "white",bd=2, pady=20, year = 2020, month = 1, day = 1).place(x=630,y=68)

Label(logScreen, text="Race:").place(x=230,y=120)
afri_Ameri= IntVar()
ameri_Indi = IntVar()
white = IntVar()
native = IntVar()
asian = IntVar()
other = IntVar()

Checkbutton(logScreen, text="African American", variable=afri_Ameri, onvalue=1, offvalue=0).place(x=290, y=120)
Checkbutton(logScreen, text="American Indian", variable=ameri_Indi, onvalue=1, offvalue=0).place(x=450, y=120)
Checkbutton(logScreen, text="White", variable=white, onvalue=1, offvalue=0).place(x=600, y=120)
Checkbutton(logScreen, text="Native Hawaiian/Other Pacific Islander", variable=native, onvalue=1, offvalue=0).place(x=230, y=155)
Checkbutton(logScreen, text="Asian", variable=asian, onvalue=1, offvalue=0).place(x=690, y=120)
Checkbutton(logScreen, text="Other", variable=other, onvalue=1, offvalue=0).place(x=510, y=155)

Label(logScreen, text="Email:").place(x=230, y=205)
Label(logScreen, text="Phone Number:").place(x=230, y=255)
Label(logScreen, text="Insurance:").place(x=230, y=305)
Label(logScreen, text="Psychiatrist:").place(x=230, y=355)

var = IntVar()
Radiobutton(logScreen, text="Dr. Till", variable=var, value=1).place(x=320, y=355)
Radiobutton(logScreen, text="Outside Psychiatrist", variable=var, value=2).place(x=415, y=355)

Label(logScreen, text="Substance Use Disorders (SUD):").place(x=230, y=405)
Label(logScreen, text="Mental Health Diagnosis (if any):").place(x=230, y=550)
Label(logScreen, text="Individual Notes:").place(x=230, y=710)


entry1 = tk.Entry(logScreen, width=10)
entry2 = tk.Entry(logScreen, width=10)
entry3 = tk.Entry(logScreen, width=8)
entry4 = tk.Entry(logScreen, width=31)
entry5 = tk.Entry(logScreen, width=25)
entry6 = tk.Entry(logScreen, width=29)

text8 = Text(logScreen, height=7, width=60, padx=3, pady=3, font='Arial')
text9 = Text(logScreen, width=60, height=7, padx=3, pady=3, font='Arial')
text10 = Text(logScreen, height=5, width=60, padx=3, pady=3, font='Arial')
text8.place(x=230, y=430)
text9.place(x=230, y=575)
text10.place(x=230, y=735)

entry1.place(x=310, y=16)
entry2.place(x=600, y=16)
entry3.place(x=65, y=253)
entry4.place(x=280, y=202)
entry5.place(x=338, y=253)
entry6.place(x=307, y=303)

    #then auto save feature, export into txt file

    #stretch goal of optional export into pdf or print

    #allow this to be blank template for new patients

#questions: based on input of user for registering new patients, a new txt file and python file is created with
#this template code (blank entries). the python and txt file are named with MRN,
#which can be new one written by user or preexisting. how can I do this?

#stretch goal of having user open up txt file again, entries filled by csv read, to edit it
def getInput():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    d = entry4.get()
    e = entry5.get()
    f = entry6.get()
    g = text8.get()
    h = text9.get()
    i = text10.get()
    logScreen.destroy()

    global params
    params = [a, b, c, d, e, f, g, h, i]
    #save to txt file

def upload_file():
    global img
    f_types = [('Jpeg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((200, 200))  # new width & height
    img = ImageTk.PhotoImage(img_resized)
    b2 = Label(logScreen,image=img).place(x=0, y=0)

Button(logScreen, text = "Save", command = getInput).place(x=65, y=750)

mainloop()

#comment code last, make sure cited?
