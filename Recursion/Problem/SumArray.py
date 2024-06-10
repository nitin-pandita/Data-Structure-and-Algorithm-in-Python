def SumArray(arr):
    # we need to find the sum of all the elements in the array
    if not arr:
        return 0
    
    return  arr[0] + SumArray(arr[1:])


arr = [1,34,45,6]
output = SumArray(arr)

print(output)