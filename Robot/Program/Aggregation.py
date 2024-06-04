class salary:
    def __init__(self, sal, bonus):
        self.sal = sal
        self.bonus = bonus

    def annual_salary(self):
        return (self.sal*12) + self.bonus

class emp:
    def __init__(self, emp, age, salary):
        self.emp = emp
        self.age = age
        self.salary = salary

    def emp_salary(self):
        return self.salary.annual_salary()                  # Calling annual salary method of salary class using above created object

obj = salary(100000, 150000)                                # Created salary class object
obj1 = emp('Gaurav', 35, obj)                               # Emp class has salary class object (Has A relationship)
print(obj1.emp_salary())