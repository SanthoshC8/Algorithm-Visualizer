import time

def mergesort(data,drawData):

    mergesort2(data,drawData)

def mergesort2(data,drawData):


    if len(data)<2:
        return

    m = (len(data))//2

    left= data[:m]
    right= data[m:]

    drawData(data,["light blue" if i <len(left) else "yellow" for i in range(len(data))])
    time.sleep(0.1)


    mergesort2(left,drawData)

    drawData(data,["light blue" if i >len(right) else "yellow" for i in range(len(data))])
    time.sleep(0.1)

    mergesort2(right,drawData)

    merge(left,right,data,drawData)
    drawData(data,["light green" for i in range(len(data))])
    time.sleep(0.1)



def merge(left,right,data,drawData):
    nL = len(left)
    nR = len(right)

    l = 0
    r = 0
    k = 0

    while l <nL and r<nR:
        drawData(data,["green" if i == l or i==r else "yellow" for i in range(len(data))])
        time.sleep(0.1)
        if left[l]<right[r]:
            data[k] = left[l]
            l+=1
            drawData(data,["light green" if i == l or i==k else "yellow" for i in range(len(data))])
            time.sleep(0.1)

        else:
            data[k] = right[r]
            drawData(data,["light green" if i == r or i==k else "yellow" for i in range(len(data))])
            time.sleep(0.1)
            r+=1

        k+=1

    while l < nL:
        drawData(data,["green" if i == l or i==r else "yellow" for i in range(len(data))])
        time.sleep(0.1)
        data[k] = left[l]
        drawData(data,["light green" if i == l or i==k else "yellow" for i in range(len(data))])
        time.sleep(0.1)
        l+=1
        k+=1
    while r < nR:
        drawData(data,["green" if i == l or i==r else "yellow" for i in range(len(data))])
        time.sleep(0.1)
        data[k] = right[r]
        drawData(data,["light green" if i == r or i==k else "yellow" for i in range(len(data))])
        time.sleep(0.1)
        r+=1
        k+=1
