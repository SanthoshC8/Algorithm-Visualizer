import time
def quicksort(data,drawData):
    quicksort2(data,drawData,0,len(data)-1)
    drawData(data,["light green" for i in data])

def quicksort2(data,drawData,left,right):

    if left>=right:
        return

    p_index = partition(data,drawData,left,right)


    quicksort2(data,drawData,left,p_index-1)

    quicksort2(data,drawData,p_index+1,right)





def partition(data,drawData,left,right):
    pivot = data[right]
    p_index = left
    drawData(data,["green" if t== right else "light blue" if left<=t<=right  else "yellow" for t in range(len(data))])
    time.sleep(0.1)
    for i in range(left,right):
        drawData(data,["green" if t== i or t==right  else "light blue" if left<=t<=right else "yellow" for t in range(len(data))])
        time.sleep(0.1)
        if data[i] <= pivot :
            data[i], data[p_index] = data[p_index],data[i]

            drawData(data,["light green" if t== i or t==p_index else "green" if t==right  else "light blue" if left<=t<=right else "yellow" for t in range(len(data))])
            time.sleep(0.1)
            p_index+=1
    data[p_index], data[right] = data[right], data[p_index]
    drawData(data,["light green" if t == right or t== p_index  else "light blue" if left<=t<=right else "yellow" for t in range(len(data))])
    time.sleep(0.1)
    return p_index
