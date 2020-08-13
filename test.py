print("KI" == "ki")

class parent():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
class child():
    def __init__(self,a,b,c,d):
        parent.__init__(self,a,b,c)
        self.d = d
    def printAll(self):
        print(self.a, self.b, self.c, self.d)

newchild = child(1,2,3,4)
newchild.printAll()

