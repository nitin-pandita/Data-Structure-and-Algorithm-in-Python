class Boys:
    pass # means do nothing it is an empty class


# attributes of the class
s1 = Boys() # attribute
s2 = Boys()
s3 = Boys()

# creating an instance of the attribute
s1.name = "Nitin"
s2.rollno = 12 
s3.name = "Kartik"
s3.rollno = 34


# checking the values of an instance
showAll = s3.__dict__
print(showAll)

# Functions for finding the instance of an attribute
# 1. hasAttribute
# 2. getAttribute

doesHaveAttr = hasattr(s1, "rollno") # will return true or false
getAttribute = getattr(s2,"rollno", "Sorry the attribute is not there")
print(getAttribute)
