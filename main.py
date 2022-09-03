from tkinter import *
from tkinter import ttk
from bubbleSort import bubblesort
from insertionSort import insertionsort
from selectionSort import selectionsort
from quickSort import quicksort



window = Tk()
window.title("Algorithm Visualizer")
window.geometry("700x500")
data = []


greeting = Label(text="Algorithm Visualizer")
greeting.pack()
temp = Label(text="Algorithm:")
temp.place(x=1, y=20)

selected_algorithm = StringVar()
algo = ttk.Combobox(window, width = 20, textvariable = selected_algorithm
    , values= ["Bubble Sort", "Selection Sort","Insertion Sort","Quick Sort"]
    , state = "readonly")







algo.place(x=1,y=40)
algo.current(0)

def StartAlgorithm():
    global data

    if selected_algorithm.get() == "Bubble Sort":
        bubblesort(data,drawData)
    elif selected_algorithm.get() == "Selection Sort":
        selectionsort(data,drawData)
    elif selected_algorithm.get() == "Insertion Sort":
        insertionsort(data,drawData)
    elif selected_algorithm.get() == "Quick Sort":
        quicksort(data,drawData)



def drawData(data, colourArray):
    canvas.delete("all")
    norm_data = [i/max(data) for i in data]
    for i, h in enumerate(norm_data):

        x0 = i* ( 700/(len(data)) )+1
        y0= 360 -h *350
        x1 = (i+1)*( 700/(len(data)) )
        y1 = 350 + 20

        canvas.create_rectangle(x0,y0,x1,y1,fil=colourArray[i])
        canvas.create_text(x0+8,y0+5,text=str(data[i]),fill="dark red")

    window.update()
def Generate():
    global data
    data = [19,16,3,14,6,8,20,15,1,24,17,25,4,21,5,18,9,10,2,11,22,7,12,23,13]
    drawData(data, ["yellow" for x in range(len(data))])

button = Button(
    text = "Randomize",
    command = Generate
)
button.place(x= 620, y= 20)

button2 = Button(
    text = "Sort",
    command = StartAlgorithm
)
button2.place(x=620,y= 40)



canvas= Canvas(master=window,bg= "black", width = 700, height = 355)

canvas.place(y = 70, x= 0)










window.mainloop()
