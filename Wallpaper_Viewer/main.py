from tkinter import *
from PIL import Image, ImageTk  # python imaging library (PIL)
import os


def handle_rotation():
    global ind;
    img_label.config(image=img_array[ind])
    ind = (ind + 1) % len(img_array)


ind = 0

root = Tk()

root.title("Wallpaper Viewer")

root.geometry('600x600')
root.configure(background='black')

image = os.listdir('Wallpaper')
image.remove('.DS_Store')

img_array = list()

for i in image:
    img = Image.open(os.path.join('Wallpaper', i))
    resized_img = img.resize((500, 350))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image=img_array[0])
img_label.pack(pady=(10, 10))

next_btn = Button(root, text="NEXT", fg='black', bg='white', width=10, height=2, command=handle_rotation)
next_btn.pack()

root.mainloop()
