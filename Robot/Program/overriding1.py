class a:
    def hello(self):
        print("Hello1")

class b(a):
    def hello(self):
        print("Hello2")
        super().hello()

obj=b()
obj.hello()

