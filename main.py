from tkinter import *
from pytube import YouTube
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import threading
from tkinter import filedialog


root = tb.Window(themename="superhero")
root.geometry("1000x500")
root.iconbitmap("ikonica.ico")
root.title("Youtube Downloader")


class Labels:
    y=tb.Label(root, text="Downloading...", bootstyle="default", font=("Arial", 15))
    folder = ""
    z = Label(root)

x=StringVar()

def text():
    Labels.y.config(text="Downloading...", bootstyle="default")
    Labels.y.pack(pady=40)
    start_time = threading.Timer(1, downloader)
    start_time.start()


def downloader():
    url=YouTube(str(x.get()))
    video=url.streams.filter(progressive=True).last()
    
    video.download(Labels.folder)
    Labels.y.config(text="FINISHED", bootstyle="success")
    
def folder_func():
    Labels.folder = filedialog.askdirectory()
    Labels.z.config(text=Labels.folder)
    Labels.z.pack()
    






naslov = tb.Label(root, text="YOUTUBE DOWNLOADER", bootstyle="danger", font=("Arial", 30))
naslov.pack(pady=60)

link = tb.Entry(root, textvariable=x, width=70)
link.pack()

dugme = tb.Button(root, text="DOWNLOAD", command=text)
dugme.pack(pady=10)

folder_dugme = tb.Button(root, text="Choose output folder:", command=folder_func, bootstyle="outline")
folder_dugme.pack(pady=10)

Labels.z.pack()




root.mainloop()