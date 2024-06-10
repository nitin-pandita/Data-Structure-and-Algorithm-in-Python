def NumberArray(arr,n, target):
    # checking a number in a list
    if not arr:
        return False
    
    if arr[0] == target:
        return True

    return NumberArray(arr[1:],n, target)
arr = [1,2,34,45,56,67]
output = NumberArray(arr,len(arr),671)

print(output)