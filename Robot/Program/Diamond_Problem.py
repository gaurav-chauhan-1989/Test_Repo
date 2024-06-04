class a:
    def p(self):
        print("This is class a")

class b(a):
    def p(self):
        print("This is class b")

class c(a):
    def p(self):
        print("This is class c")
                                # In multiple inheritence
class d(c,b):                     # if c is inherit first then the output will print c method. If b is inherit first then class b method will print
    pass

obj=d()
obj.p()