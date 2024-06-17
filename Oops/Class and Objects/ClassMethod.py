from datetime import date
class Boys:
    def __init__(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage
        
    @classmethod
    def brotherYear(cls, name, age, percentage):
        return cls(name, date.today().year - age, percentage)

    def studentDetails(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Percentage = ", self.percentage)


s1 = Boys.brotherYear("Nitin",2001,89)
s1.studentDetails()
