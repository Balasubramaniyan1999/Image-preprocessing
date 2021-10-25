#libraries which I used

from tkinter import *
import cv2
import numpy as np
from tkinter import filedialog
from PIL import ImageTk, Image
from matplotlib import pyplot as plt

#creating a window

root = Tk()
root.minsize(1000, 1000)
root.title("ImageApp")
l = Label(root, text="ImageProcessing", fg="black", font="Verdana 20 bold")
root.configure(background="white")
l.pack()

#creating a frame

frame =LabelFrame(root, text="Frame", padx=200, pady=200)
frame.place(x=50, y=50)
my_label =Label(frame).pack()



# creating butons and operation
def c2g():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b1 = Button(root, text="color to gray", fg="pink", bg="black", command=c2g)
b1.place(x=800, y=100)

def Rotate180():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.rotate(input, cv2.ROTATE_180)
    final_image =Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)




b2 = Button(root, text=" Rotate_180 ", fg="pink", bg="black", command=Rotate180)
b2.place(x=800, y=200)


def Rotate90():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.rotate(input, cv2.ROTATE_90_COUNTERCLOCKWISE)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b3 = Button(root, text="  Rotate_90  ", fg="pink", bg="black", command=Rotate90)
b3.place(x=800, y=300)


def Blur():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.blur(input, (5,5))
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)



b4 = Button(root, text="       Blur       ", fg="pink", bg="black", command=Blur)
b4.place(x=800, y=400)

def Resize():
    global my_image
    input = cv2.imread(root.filename, 1)
    scale = 65
    width = int(input.shape[1] * scale / 100)
    height = int(input.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(input, dim, interpolation=cv2.INTER_AREA)
    final_image = Image.fromarray(resized)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b5 = Button(root, text="     Re-size     ", fg="pink", bg="black", command=Resize)
b5.place(x=800, y=500)


def EdgeDetection():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.Canny(input, 100, 200)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)

b6 = Button(root, text="Edge detection", fg="pink", bg="black", command=EdgeDetection)
b6.place(x=1000, y=100)


def Threshold():
    global my_image
    input = cv2.imread(root.filename)
    temp,image = cv2.threshold(input, 100, 200, cv2.THRESH_BINARY)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b7 = Button(root, text="     Threshold    ", fg="pink", bg="black", command=Threshold)
b7.place(x=1000, y=200)


def Dilation():
    global my_image
    input = cv2.imread(root.filename, 1)
    dilation = np.ones((5, 5))
    image = cv2.dilate(input, dilation)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)



b8 = Button(root, text="      Dilation      ", fg="pink", bg="black", command=Dilation)
b8.place(x=1000, y=300)


def Erosion():
    global my_image
    input = cv2.imread(root.filename, 1)
    erosion = np.ones((5, 5))
    image = cv2.erode(input,erosion)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b9 = Button(root, text="      Erosion      ", fg="pink", bg="black", command=Erosion)
b9.place(x=1000, y=400)


def Border():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.copyMakeBorder(input, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)

b10 = Button(root, text="      Border     ", fg="pink", bg="black", command=Border)
b10.place(x=1000, y=500)


def UploadImage():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:\ Users\ascen", title="select a file",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root).pack()
    input = Image.open(root.filename)
    input.thumbnail((400, 400))
    my_image = ImageTk.PhotoImage(input)
    my_image_label = Label(image=my_image).place(x=60, y=60)


b11 = Button(root, text="Upload Image", fg="pink", bg="black", font="verdana 10", command=UploadImage)
b11.place(x=100, y=570)


def Crop():
    global my_image
    input = cv2.imread(root.filename)
    image = input[10:100, 50:200]
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)

b12 = Button(text="         crop        ", fg="pink", bg="black",command=Crop)
b12.place(x=1200, y=100)


def Contours():
    global my_image
    input = cv2.imread(root.filename)
    gray_image = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray_image, 127, 255, 0)
    contours, hierachy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    draw = cv2.drawContours(input, contours, -1, (0, 255, 0), 4)
    final_image = Image.fromarray(draw)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)




b13 = Button(root, text="    contours    ",fg="pink",bg="black",command=Contours)
b13.place(x=1200, y=200)


def Histogram():
    global my_image
    input = cv2.imread(root.filename)
    b, g, r =cv2.split(input)
    plt.hist(b.ravel(), 256, [0, 256])
    plt.hist(g.ravel(), 256, [0, 256])
    plt.hist(r.ravel(), 256, [0, 256])
    plt.show()

b14 = Button(root, text="    Histogram  ",fg="pink",bg="black",command=Histogram)
b14.place(x=1200, y=300)

def Blobdetection():
    global my_image
    input = cv2.imread(root.filename, 0)
    detector = cv2.SimpleBlobDetector_create()
    image = detector.detect(input)
    blobs = cv2.drawKeypoints(input,image, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    final_image = Image.fromarray(blobs)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b15 = Button(root, text="Blob_Detection",fg="pink",bg="black",command=Blobdetection)
b15.place(x=1200, y=400)


def Contrast():
    global my_image
    input = cv2.imread(root.filename)
    image = cv2.addWeighted(input, 2, np.zeros(input.shape, input.dtype), 0, 0)
    final_image = Image.fromarray(image)
    my_image = ImageTk.PhotoImage(final_image)
    Label(image=my_image).place(x=60, y=60)


b16 = Button(root, text="     contrast     ",fg="pink",bg="black",command=Contrast)
b16.place(x=1200, y=500)



root.mainloop()
