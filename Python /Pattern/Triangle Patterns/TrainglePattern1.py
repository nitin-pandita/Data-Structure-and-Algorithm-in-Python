# 1
# 1 2
# 1 2 3
# 1 2 3 4

n = int(input("Enter a Number: "))

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1