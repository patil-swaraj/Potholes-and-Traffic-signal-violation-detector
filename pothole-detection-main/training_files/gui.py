from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import object_detection as od
import imageio
import cv2

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.pos = []
        self.line = []
        self.rect = []
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        self.counter = 0

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Open", command=self.open_file)
        
        menu.add_cascade(label="File", menu=file)
        
        analyze = Menu(menu)
        
        menu.add_cascade(label="Analyze", menu=analyze)

    def open_file(self):
        self.filename = filedialog.askopenfilename()

        cap = cv2.VideoCapture(self.filename)

    def main_process(self):

        video_src = self.filename

        cap = cv2.VideoCapture(video_src)

root = Tk()
app = Window(root)