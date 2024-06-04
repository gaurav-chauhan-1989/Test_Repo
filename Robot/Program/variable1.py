class var:
    def var1(self):
        x = 20
        print(x)

        def var2():
            print(x)                        # Using parent function variable in child function (Enclosing)

        var2()


    def var3(self):
        global y                            # Declaring global variable. Now this variable can be used anywhere within the class
        y = 30                              # Even if it is declared inside a method we can use this variable from other methods as well
        print("Value is {}".format(y))

    def var4(self):
        print(y)


obj = var()
obj.var1()
obj.var3()
obj.var4()