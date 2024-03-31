from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email == 'shrutikumari0606@gmail.com' and password == 'Sonal**':
        messagebox.showinfo('yayyyy', 'Login Successful')
    else:
        messagebox.showinfo('Error', 'Login Failed')


root = Tk()

root.title("Login form")

root.iconbitmap('favicon.ico')

root.minsize(400, 400)

root.geometry('450x700')

root.configure(background='white')

img = Image.open('google-logo1.png')
resized_img = img.resize((150, 130))
final_img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=final_img)
img_label.pack(pady=(20, 20))

text_label = Label(root, text='Google', bg='white')
text_label.pack(pady=(1, 25))
text_label.config(font=('verdana', 24))

email_label = Label(root, text='Enter Email', bg='white')
email_label.pack(pady=(10, 10))
email_label.config(font=('verdana', 17))

email_input = Entry(root, width=45)
email_input.pack(ipady=5, pady=(1, 20))

password_label = Label(root, text='Enter Password', bg='white')
password_label.pack(pady=(10, 10))
password_label.config(font=('verdana', 17))

password_input = Entry(root, width=45)
password_input.pack(ipady=5, pady=(1, 20))

login_btn = Button(root, text='Login', bg='white', width=10, height=2, command=handle_login)
login_btn.pack(pady=(10, 10))
login_btn.config(font=('Verdana', 17))

root.mainloop()
