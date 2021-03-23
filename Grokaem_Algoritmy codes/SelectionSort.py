def Find_Smallest(arr):   #find smallest index
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):    #find smallest value and add this value to array
    newArr = []
    for i in range(len(arr)):
        smallest = Find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 6, 10, 1, 8, 46]))

#time O(n^2)