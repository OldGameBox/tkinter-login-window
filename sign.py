import tkinter as tk
import os

os.system("pip install cryptography")

from cryptography.fernet import Fernet

def save(u,l):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    global u_e
    global l_e
    u_e = fernet.encrypt(u.encode())
    l_e = fernet.encrypt(l.encode())
    print(key,u_e,l_e)
    file = open("config.cfg","wb")
    file.write(u_e)
    file.write(l_e)
    file.close()
    file = open("key.cfg","wb")
    file.write(key)
    file.close()


def login():
    ErrorCode.set("")
    if len(username.get()) > 3:
        print("username ok")
        if len(password.get()) > 5:
            print("password ok")
        else:
            print("password error")
            ErrorCode.set("Password is too short")
    else:
        print("error")
        ErrorCode.set("Username is too short ")

def register():
    ErrorCode.set("")
    if len(username.get()) > 3:
        print("username ok")
        if len(password.get()) > 5:
            print("password ok")
            save(username.get(),password.get())
        else:
            print("password error")
            ErrorCode.set("Password is too short")
    else:
        print("error")
        ErrorCode.set("Username is too short ")

root = tk.Tk()

fore = "#1c1c1c"
back = "#f0f0f0"

mfont = "main"
barcode = "barcode.ttf"

root.title("Talker")
root.geometry("300x600")
root.resizable(height = False, width = False)
root.configure(background='#f0f0f0')

ErrorCode = tk.StringVar()
ErrorCode.set("")

tk.Label(text="",bg = back).pack()

Name = tk.Label(text = "Talker", bg = back, fg = fore, font = (mfont,50,"normal")).pack(pady=60)

tk.Label(text="",bg = back,fg = fore).pack(pady = 29)
tk.Label(text="Username:                     ", bg = back, fg = fore, font = (mfont,18,"normal")).pack()

username = tk.StringVar()
usernameEntry = tk.Entry(bg = fore, textvariable=username, fg = back, font = (mfont,17,"normal"),width=20,highlightthickness=0,borderwidth=0, justify='center').pack()

tk.Label(text="",bg = back).pack()
tk.Label(text="Password:                     ", bg = back, fg = fore, font = (mfont,18,"normal")).pack()

password = tk.StringVar()
passwordEntry = tk.Entry(bg = fore, textvariable=password, fg = back, font = (barcode,17,"normal"),width=20,highlightthickness=0,borderwidth=0, justify='center').pack()

tk.Label(textvariable = ErrorCode,bg = back, fg = "#960000", font = (mfont,12,"normal")).pack(pady = 7)
Login = tk.Button(command = login,text = "Login", bg = fore, fg = back, font = (mfont,17,"normal"),highlightthickness=0,borderwidth=0,width = 20, justify='left').pack()
Register = tk.Button(command = register,text = "Register", bg = fore, fg = back, font = (mfont,17,"normal"),highlightthickness=0,borderwidth=0,width = 20, justify='left').pack(pady=15)

root.mainloop()
