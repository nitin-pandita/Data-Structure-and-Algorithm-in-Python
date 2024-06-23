# A B C D 
# B C D E 
# C D E F 
# D E F G 
n = int(input("Enter a String: "))

i = 1
while i <= n:
    j = 1
    start_char = chr(ord('A') + i - 1)
    while j <= n:
        chartP = chr(ord(start_char) + j -1) 

        print(chartP, end=" ")
        j += 1
    print()
    i += 1

