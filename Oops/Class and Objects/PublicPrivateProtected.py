class Boys:
    def __init__(self, name, age):
        # privates are used using the  __ for marking it as private
        self.__name = name
        self.age = age

    def Kartik(self): 
        print(self.__name)
        print(self.age)

    @staticmethod
    def thisStatic():
        print("Kya bolti tu")


s = Boys("Nitin",23)


s.Kartik()