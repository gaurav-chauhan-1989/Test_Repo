class salary:
    def __init__(self, sal, bonus):
        self.sal = sal
        self.bonus = bonus

    def annual_salary(self):
        return (self.sal*12) + self.bonus

class emp:
    def __init__(self, emp, age, sal, bonus):
        self.emp = emp
        self.age = age
        self.sal = sal
        self. bonus = bonus
        self.obj = salary(sal, bonus)                    # Here we create object of Salary class in emp class constructor

    def emp_salary(self):
        return self.obj.annual_salary()                  # Calling annual salary method of salary class using above created object

obj1 = emp('Gaurav', 35, 100000, 150000)
print(obj1.emp_salary())
