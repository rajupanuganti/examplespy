class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()


    def show(self):
        print(self.name ,self.rollno)
        self.lap.show()


    class Laptop:
        def __init__(self):
            self.brand = 'Dell'
            self.pros = 'i3'  

        def show(self):
            print(self.brand,self.pros)


s1 = student('raju',25)
s1.show()