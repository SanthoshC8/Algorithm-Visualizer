arr = [19,16,3,14,6,8,20,15,1,24,17,25,4,21,5,18,9,10,2,11,22,7,12,23,13,]

c1,c2=0,0
for i in range(1,len(arr)):
    val = arr[i]
    pos = i
    c1+=1
    while pos > 0 and val < arr[pos-1]:
        arr[pos] = arr[pos-1]
        c1+=1
        pos-=1

    arr[pos] =val



print(arr,c1 )
data = [19,16,3,14,6,8,20,15,1,24,17,25,4,21,5,18,9,10,2,11,22,7,12,23,13,]
for x in range(len(data)):
    for i in range(len(data)-1-x):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1],data[i]
        c2+=1


print(data, c2)
