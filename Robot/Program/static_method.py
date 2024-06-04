class a:

    @staticmethod                            # Static methods are bound to class not class object.
    def banking(product):                    # While class method are bound with class object
        list = ["Netbanking", "Auto Loan", "Personal Loan"]

        for i in list:
            if i==product:
                break
        print(i)

a.banking("Personal Loan")                               # Static method can be run without creating the object. It can be call using class name