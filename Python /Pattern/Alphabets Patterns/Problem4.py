n = int(input("Enter a Number: "))

i = 1

while i <= n:
    charP = chr(ord('A') + i - 1)

    j = 1
    while j <= i:
        print(charP, end=" ")
        j += 1
    
    print()
    i += 1
    
