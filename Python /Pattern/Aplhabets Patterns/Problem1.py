# A B C D 
# A B C D 
# A B C D 
# A B C D 
n = int(input("Enter a String: "))

i = 1
while i <= n:
    j = 1
    while j <= n:
        chartP = chr(ord('A' ) + j -1) 

        print(chartP, end=" ")
        j += 1
    print()
    i += 1

