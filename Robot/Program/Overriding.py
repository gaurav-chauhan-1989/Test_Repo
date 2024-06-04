class a:
    var1="This is class variable"
    def __init__(self):
        self.var1="This is a class instance variable"
        self.special="Special"

class b(a):
    var1="This is class b class variable"
    def __init__(self):
        super().__init__()
        v1="Hello"
        self.var1="This is b class instance variable"

obj=b()
print(obj.special,obj.var1
      )             # Overloading concept - Instance variable (Variable under constructor) in Class B
                            #  Then it will look for instance variable of class A
                            # Then it will look for class variable of Class B
                            # Then it will look for class variable of class A