from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username:")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password:")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()

# Implementing event on register button

def register_user():
    global username_info
    username_info = username.get()
    password_info = password.get()

    if password_info == "DEB058":
        file = open(username_info, "w")
        file.write(username_info)
        file.write(username_info + "\n")
        file.write("DEB058")
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(register_screen, text="Registration Success", fg="green").pack()
    else:
        Label(register_screen, text="Incorrect ID Number", fg="red").pack()


# Implementing event on login button

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            patientForm()
            #main_screen.destroy()
        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title("Login Failed")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid ID").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    user_not_found_screen.title("Login Failed")
    user_not_found_screen.geometry("200x100")
    Label(user_not_found_screen, text="Patient Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups
def delete_registration():
    register_user.after(3000, lambda: register_user.destroy())

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(text="Username:").pack()
    username_login_entry = Entry(textvariable=username_verify)
    username_login_entry.pack()
    Label(text="").pack()
    Label(text="Password:").pack()
    password_login_entry = Entry(textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(text="").pack()
    Button(text="Login", width=10, height=1, command=login_verify).pack()

    Label(text="").pack()
    Button(text="Register", height=1, width=10, command=register).pack()

    main_screen.mainloop()

def patientForm():
    global logScreen
    logScreen = Toplevel(main_screen)
    logScreen.geometry("800x830+360+40")
    logScreen.title("Patient File")

    profilePic = PhotoImage(file="placeholder.png")
    resizedPfp = profilePic.subsample(3, 3)
    Label(logScreen, image=resizedPfp).place(x=0, y=0)

    Button(logScreen, text='Upload Photo', command=lambda:upload_file()).place(x=40, y=210)

    Label(logScreen, text="First Name:").place(x=230, y=20)
    Label(logScreen, text="Last Name:").place(x=520, y=20)
    Label(logScreen, text="MRN:").place(x=25, y=255)
    Label(logScreen, text="Date of Birth:").place(x=230, y=70)
    DateEntry(logScreen, width= 9, background= "blue", foreground= "white",bd=2, pady=20, year = 2001, month = 1, day = 1).place(x=320, y=68)

    Label(logScreen, text="Admission Date:").place(x=520, y=70)
    DateEntry(logScreen, width= 9, background= "blue", foreground= "white",bd=2, pady=20, year = 2020, month = 1, day = 1).place(x=630,y=68)

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

        #stretch goal of having user open up txt file again, entries filled by csv read, to edit it
    def getInput():
        a = entry1.get()
        b = entry2.get()
        c = entry3.get()
        d = entry4.get()
        e = entry5.get()
        f = entry6.get()
        #g = text8.get()
        #h = text9.get()
        #i = text10.get()

        global params
        params = [a, b, c, d, e, f]

        for entry in params:
            paramstr = ''
            paramstr += str(entry)
        save(paramstr, username1)

    def save(content, filename):
        patient_win = str("Patient: " + filename + ".txt")
        saved_file = open(patient_win, "w")
        saved_file.write(content)
        saved_file.write(content + "\n")
        saved_file.close()

        #save to txt file

    def upload_file():
        global img
        f_types = [('Jpeg Files', '*.jpeg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = Image.open(filename)
        img_resized = img.resize((200, 200))  # new width & height
        img = ImageTk.PhotoImage(img_resized)
        Label(logScreen,image=img).place(x=0, y=0)

    Button(logScreen, text="Save", command=getInput).place(x=65, y=750)

main_account_screen()