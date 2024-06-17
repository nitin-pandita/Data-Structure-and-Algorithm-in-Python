class Boys:
    def Kartik(self):
        self.name = "Kartik"

    @staticmethod  #static method is used when we don't want to use "self" 
    def Nitin():
        print("Hello World")

s = Boys()

s.Nitin()