def bubblesort(arr):
    arr= [19,16,3,14,6,8,20,15,1,24,17,25,4,21,5,18,9,10,2,11,22,7,12,23,13,]

    for x in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]

    print(arr)
    return arr
