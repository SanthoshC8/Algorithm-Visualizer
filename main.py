import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
temp = tk.Label(text="YOOO")
temp.pack()

button = tk.Button(
    text = "CLick me"
)
button.pack()

frame1 = tk.Frame(master=window, width=100, height = 100,bg="red")
frame1.pack()

frame2 = tk.Frame(master=window,width= 50, height = 50, bg = "yellow")
frame2.pack()
frame3 = tk.Frame(master=window,width = 25, height= 25, bg = "blue")
frame3.pack()


window.mainloop()
