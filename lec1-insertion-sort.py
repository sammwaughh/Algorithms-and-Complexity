# Insertion Sort

def insertionSort(arr):
    l = len(arr)
    for i in range(1, l):
        val = arr[i]
        stop = False
        while ((i == 0) or (val < arr[i-1])) and (not stop):
            if i != 0:
                arr[i] = arr[i-1]
                i -= 1
            else:
                stop = True
        arr[i] = val
    return arr

arr = [4,3,5,1,2]
print(insertionSort(arr))