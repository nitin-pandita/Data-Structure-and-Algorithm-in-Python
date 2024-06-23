# 4 3 2 1
# 4 3 2 1
# 4 3 2 1
# 4 3 2 1


n = int(input("Enter a Number: "))

i = 1

while i <= n: 
    j = 1
    while j <= n:
        print(n - j + 1, end=" ")
        j += 1

    print()

    i += 1