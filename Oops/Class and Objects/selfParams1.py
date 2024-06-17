# class where the self is passed is called instance method
class Boys:
    name = "Nitin"
    def Kartik(self):
        self.age = 60

    def print_age(self):
        print(self.age)

s = Boys()

s.Kartik()

s1 = Boys()
# will give error because we have not assigned value of age before the print_age is declared
s1.print_age()
