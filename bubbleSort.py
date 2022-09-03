import time


def bubblesort(data,drawData):
    for x in range(len(data)):
        for i in range(len(data)-1-x):
            drawData(data, ["green" if t == i or t==i +1 else "yellow" for t in range(len(data))])
            time.sleep(0.1)
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1],data[i]


                drawData(data, ["light green" if t == i or t==i +1 else "yellow" for t in range(len(data))])
                time.sleep(0.1)

    drawData(data,["light green" for i in range(len(data))])
