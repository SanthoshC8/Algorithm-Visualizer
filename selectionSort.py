import time

def selectionsort(data,drawData):
    temp = True
    for i in range(len(data)):
        curr_min = i
        for x in range(i+1,len(data)):

            if data[x] < data[curr_min]:
                drawData(data,["green" if t==curr_min or t==x else "yellow" for t in range(len(data))])
                time.sleep(0.1)
                curr_min = x
                temp = False

            if temp:
                drawData(data,["green" if t==curr_min or t==x else "yellow" for t in range(len(data))])
                time.sleep(0.1)
            temp = True


        data[curr_min], data[i] = data[i], data[curr_min]

        drawData(data,["light green" if t == i or t== curr_min else "yellow" for t in range(len(data))])
        time.sleep(0.1)
    drawData(data,["light green" for t in range(len(data))])
