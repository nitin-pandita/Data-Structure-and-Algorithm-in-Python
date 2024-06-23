# * * * *
# * * * *
# * * * *
# * * * *


n = int(input("Enter the number: "))

i = 1

while i <= n:
    # print the col also
    j = 1
    while j <= n:
        print("*", end=" ")

        j += 1
    print() # this is for a new line

    i += 1