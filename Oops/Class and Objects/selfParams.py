class Boys:
    def Kartik(self):
        self.name = "Nitin"
        self.percentage = 89
        print(self.name)

    def Nitin(self):
        if self.percentage > 80:
            print("Passed !")
        else:
            print("Not Passed!")



s1 = Boys()
# Boys.Kartik(s1)
s1.Kartik() #it very important to run the function which has that attribute and then run the other function
s1.Nitin()