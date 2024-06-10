def IndexValue(arr, x, start):
    if(start == len(arr)):
        return -1
    

    if (arr[start] == x):
        return start


    return IndexValue(arr,x,start + 1)


arr = [13,45,56,23,23,34]
output = IndexValue(arr,23,0)

print(output)