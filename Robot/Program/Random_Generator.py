import random
import string

r=random.randint(1,99999999999)
print(r)

z=random.randrange(1,10000000)
print(z)

list=[7,5,8,6,78,986,45,345,22]
y=random.choice(list)
print(y)

a= ''.join(random.choices(string.ascii_lowercase,k=7))
print(a)