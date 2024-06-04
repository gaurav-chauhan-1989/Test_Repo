class art():


    def calc(self, a, b):
        try:
            print(a/b)

        except IOError as e:
            print("IO Error occured", e)

        except ArithmeticError as e:
            print("Arithmatic error occured", e)

        else:
            print("This will run when except don't run")

        finally:
            print('Always run')

x=art()
x.calc(10, 0)