class Boys:
    pp = 90 #class attribute

s1 = Boys()
s2 = Boys()

s1.name = "Kartik" # assigning the value
s1.pp = 45 # instance attribute

# it will go to the instance attribute if not any then go to the class attribute
print(s1.pp)