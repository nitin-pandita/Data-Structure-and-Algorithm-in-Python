def lastIndex(arr,x):
    n = len(arr)
    if n == 0:
        return -1
    
    smallestList = arr[1:]
    smallestListOutput = lastIndex(smallestList,x)

    if smallestListOutput != -1:
        return smallestListOutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1
        

arr = [12,34,45,56,7,2,21,2]
x = 2
output = lastIndex(arr,x)
print(output)
