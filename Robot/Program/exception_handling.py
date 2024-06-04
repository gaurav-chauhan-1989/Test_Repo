class Arithmetic:

    def div(self,a,b):
        try:
            c=a/b
            print(c)

        except IOError as e:
            print("IO error occured",e)

        except ArithmeticError as e:
            print("Arithmetic error occured", e)

        else:
            print("print only when exception is not run")

        finally:
            print("Run always whether error occured or not")

obj=Arithmetic()
obj.div(12,0)