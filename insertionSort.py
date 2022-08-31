import time

def insertionsort(data,drawData):
    for i in range(1,len(data)):
        val = data[i]
        pos = i
        drawData(data, ["green" if t == pos or t==pos -1 else "yellow" for t in range(len(data))])
        time.sleep(0.1)
        temp = True


        while pos > 0 and val < data[pos-1]:
            if temp == False:
                drawData(data, ["green" if t == pos or t==pos -1 else "yellow" for t in range(len(data))])
                time.sleep(0.1)
            temp = False
            data[pos],data[pos-1] = data[pos-1],data[pos]

            drawData(data, ["light green" if t== pos or t== pos-1 else "yellow" for t in range(len(data))])
            time.sleep(0.1)

            pos-=1

        if pos > 0:
            drawData(data, ["green" if t == pos or t==pos -1 else "yellow" for t in range(len(data))])
            time.sleep(0.1)
    drawData(data, ["light green"  for t in range(len(data))])
