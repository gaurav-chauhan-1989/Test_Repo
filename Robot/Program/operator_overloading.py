class a:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return self.x+other.x,self.y+other.y




obj=a(5,6)
obj1=a(8,7)
print (obj+obj1)

