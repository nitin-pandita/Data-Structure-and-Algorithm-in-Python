# sorting an array using the recursion.

def checkIfSorted(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return True
    
 
    if arr[0] > arr[1]:
        return False
    
    smallestList = arr[1:]
    isSmallerList = checkIfSorted(smallestList)


    if isSmallerList:
        return True
    else:
        return False

arr = [2,4,6,8]

output = checkIfSorted(arr)

print(output)

