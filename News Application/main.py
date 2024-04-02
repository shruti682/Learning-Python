import io
import webbrowser
from tkinter import *
import requests
from urllib.request import urlopen, Request
from PIL import ImageTk, Image


class NewsApp:

    def __init__(self):
        # fetch data through api
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=174123bf153940af8f377634b85abdc5').json()

        # load GUI
        self.load_gui()

        # load news-items
        self.load_news_items(0)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_gui(self):
        self.root = Tk()
        self.root.title('Inshorts')
        self.root.geometry('432x700')
        self.root.configure(background='black')
        self.root.resizable(0, 0)

    def load_news_items(self, index):
        # clear the screen for new items
        self.clear()

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            req = Request(
                url=img_url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            raw_data = urlopen(req).read()  # binary data
            img = Image.open(io.BytesIO(raw_data)).resize((400, 250))
            photo = ImageTk.PhotoImage(img)
        except:
            req = 'https://www.stellarinfo.com/blog/wp-content/uploads/2018/05/Media-file-error-in-online-video.png'
            raw_data = urlopen(req).read()  # binary data
            img = Image.open(io.BytesIO(raw_data)).resize((400, 250))
            photo = ImageTk.PhotoImage(img)

        photo_label = Label(self.root, image=photo)
        photo_label.pack(pady=(10, 10))

        # title
        title_label = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white',
                            wraplength=380, justify='center', height=6)
        title_label.pack(pady=(10, 15))
        title_label.config(font=('verdana', 19, 'bold'))

        # description
        description_label = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                                  wraplength=380, justify='center',height=6)
        description_label.pack(pady=(10, 1))
        description_label.config(font=('verdana', 15))

        # buttons
        frame = Frame(self.root, bg='black')
        frame.pack(expand=TRUE, fill=BOTH)

        if index != 0:
            prev = Button(frame, text='PREV', bg='grey', width=12, height=3,
                          command=lambda: self.load_news_items(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text='READ', bg='grey', width=12, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            nextt = Button(frame, text='NEXT', bg='grey', width=12, height=3,
                           command=lambda: self.load_news_items(index + 1))
            nextt.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


NewsApp()
