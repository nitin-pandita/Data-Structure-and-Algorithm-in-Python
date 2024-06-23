# 1
# 2 3
# 3 4 5
# 5 6 7 8

# taking the inputs
n = int(input("Enter a Number: "))

i = 1
while i <= n:
    j = 1
    k = i
    while j <= i:
        print(k, end=" ")
        j += 1
        k += 1
    print()
    i += 1
        