def sum(*args):
    a = 0
    for i in args:
        a = a+i
    print(a)

sum(4,5,6)
sum(4,5,6,5)

def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}" )

details(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
details(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)



