from tkinter import *
from bubbleSort import bubblesort

window = Tk()
window.title("Algorithm Visualizer")
window.geometry("700x500")
greeting = Label(text="Algorithm Visualizer")
greeting.pack()
temp = Label(text="Algorithm:")
temp.place(x=1, y=20)

def Generate():
    arr= [19,16,3,14,6,8,20,15,1,24,17,25,4,21,5,18,9,10,2,11,22,7,12,23,13,]

    star_x = 0
    for i in arr:
        canvas.create_rectangle(star_x,350-i*14+10, star_x+28,355,fil="yellow")
        canvas.create_text(star_x+9,350-i*14+16,text=str(i),fill="dark red")
        star_x+=28


button = Button(
    text = "Randomize",
    command = Generate
)
button.place(x= 620, y= 20)

button2 = Button(
    text = "Sort",
    command = bubblesort
)
button2.place(x=620,y= 40)



canvas= Canvas(master=window,bg= "black", width = 700, height = 355)

canvas.place(y = 70, x= 0)










window.mainloop()
