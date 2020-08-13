#  importing important libraries
from tkinter import *
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


h = (np.pi)

root = Tk()
root.title("ANALYSIS OF GRAPHS ")
root.configure(bg="#90ee90")
root.geometry("1000x550")
label = Label(root, text="ENTER THE FOLLOWING DETAILS TO SEE GRAPHS  :- ", font=("bold", 20))
label.place(x=70, y=20)
label.configure(bg="#FFDAB9")
# v = IntVar()


btn_1 = Label(root, text=" 2 D GRAPH DEPICTION : ", font=("bold", 15))
btn_1.place(x=70, y=100)
btn_1.configure(bg="#00ff00")

btn_2 = Label(root, text=" 3 D GRAPH DEPICTION : ", font=("bold", 15))
btn_2.place(x=70, y=300)
btn_2.configure(bg="#00ff00")

entry_1 = Entry(width=20)
entry_1.place(x=400, y=150)
stem_label = Label(root, text="Enter the starting coordinate of x axis in your graph  :")
stem_label.place(x=70, y=150)
stem_label.configure(bg="#ffa500")

entry_2 = Entry(root, width=20)
entry_2.place(x=400, y=180)
stem_label_1 = Label(root, text= "Enter the factor of pi as the final coordinate in your graph : ")
stem_label_1.place(x=70, y=180)
stem_label_1.configure(bg="#ffa500")

entry_3 = Entry(root, width=20)
entry_3.place(x=400, y=210)
stem_label_2 = Label(root, text="enter the scaling factor on the x axis : ")
stem_label_2.place(x=70, y=210)
stem_label_2.configure(bg="#ffa500")



# lower_limit = int(entry_1.get())
# upper_limit = float(entry_2.get())
# scale = float(entry_3.get())


def twoD():

   #  x = np.arange(lower_limit, upper_limit * int(h), scale)

    x = np.arange(int(entry_1.get()), int(entry_2.get())* int(h), float(entry_3.get()))
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)

    plt.xlabel('Values of angle as entered by user', color='b')
    plt.ylabel('Sin(x) and Cos(x)', color='k')
    plt.title("PLOT OF TRIGONOMETRIC CURVES IN 2-D", color='r')
    plt.legend(['sin(x)', 'cos(x)'])
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()




btn_3 = Button(root, text="SUBMIT", highlightbackground="cyan", command=twoD)
btn_3.place(x=70, y=250)

entry_4 = Entry(root, width=20)
entry_4.place(x=400, y=350)
stem_label = Label(root, text="Enter the starting coordinate on the z axis of your graph  :")
stem_label.place(x=70, y=350)
stem_label.configure(bg="#ffa500")

entry_5 = Entry(root, width=20)
entry_5.place(x=400, y=380)
stem_label_1 = Label(root, text="Enter the final coordinate on the z axis of your graph  :")
stem_label_1.place(x=70, y=380)
stem_label_1.configure(bg="#ffa500")

entry_6 = Entry(root, width=20)
entry_6.place(x=400, y=410)
stem_label_2 = Label(root, text=" Enter the no. of scattered points to be for graph formation  :")
stem_label_2.place(x=70, y=410)
stem_label_2.configure(bg="#ffa500")


ll = int()
uu = int()
n = int()


def threeD():

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.grid(True, which='both', color='y')
    plt.title("PLOT OF TRIGONOMETRIC CURVES IN 3-D", color='navy')
    zline = np.linspace(int(entry_4.get()), int(entry_5.get()), int(entry_6.get()))
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, color='orangered')
    ax.view_init(15, 60)
    ax.set_facecolor("yellowgreen")
    plt.show()


btn_4 = Button(root, text="SUBMIT", highlightbackground="magenta", command=threeD)
btn_4.place(x=70, y=460)

root.mainloop()
