n = int(input("Enter a Number: "))

i = 1

while i <= n:
    j = 1 # 2
    value = i #1
    while j <= i:
        print(value, end= " ")
        j += 1
        value -= 1
    print()
    i += 1
