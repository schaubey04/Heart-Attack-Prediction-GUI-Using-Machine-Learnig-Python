from tkinter import *
from tkinter import messagebox
import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8485",
    database="datasheet"
)
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) NOT NULL
)
""")

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.resizable(False, False)

image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

def signin():
    username = user.get()
    password = code.get()
    
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    
    if result:
        os.system(f"python main.py")    
    else:
        messagebox.showerror("Invalid", "Invalid username and password")

def sign_up_command():
    window = Toplevel(root)
    window.title("SignUp")
    window.geometry("925x500+300+200")
    window.resizable(False, False)
    
    image_icon1=PhotoImage(file="Images/icon.png")
    root.iconphoto(False,image_icon1)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
    
        if password == confirm_password:
            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            result = cursor.fetchone()
            
            if result:
                messagebox.showerror("Error", "Username already exists")
            else:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                db.commit()
                messagebox.showinfo("Signup", "Successfully signed up")
                window.destroy()
        else:
            messagebox.showerror("Invalid", "Both passwords should match")

    def signin_command():
        window.destroy()

    img = PhotoImage(file="signup-login.png")
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        if user.get() == "":
            user.insert(0, "Username")

    user = Entry(frame, width=25, bd=0, bg="white", fg="black", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        if code.get() == "":
            code.insert(0, "Password")

    code = Entry(frame, width=25, bd=0, bg="white", fg="black", font=("Microsoft YaHei UI Light", 11,))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    def on_enter(e):
        confirm_code.delete(0, "end")

    def on_leave(e):
        if confirm_code.get() == "":
            confirm_code.insert(0, "Confirm Password")

    confirm_code = Entry(frame, width=25, bd=0, bg="white", fg="black", font=("Microsoft YaHei UI Light", 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, "Confirm Password")
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    Button(frame, width=39, padx=7, text="Sign up", bg="#57a1f8", fg="white", bd=0, command=signup).place(x=35, y=280)
    Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=90, y=340)

    signin = Button(frame, width=6, text="Signin", bd=0, bg="white", cursor="hand2", fg="#57a1f8", command=signin_command)
    signin.place(x=200, y=340)

    window.mainloop()

img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    if user.get() == "":
        user.insert(0, "Username")

user = Entry(frame, width=25, fg="black", bg="white", bd=0, font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    if code.get() == "":
        code.insert(0, "Password")

code = Entry(frame, width=25, fg="black", bg="white", bd=0,font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, padx=7, text="Signin", bg="#57a1f8", fg="white", bd=0, command=signin).place(x=35, y=204)
Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign_up_command)
sign_up.place(x=215, y=270)

root.mainloop()
