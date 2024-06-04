class a():
    def _b(self):
        print("This is protected")

    def __c(self):
        print("This is private")

obj=a()
obj._b()
obj._a__c()
