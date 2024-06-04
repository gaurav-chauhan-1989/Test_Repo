list=["Gaurav","Amit","Shekhar","Radhika","Akhil","Aditya"]

for index,item in enumerate(list):      # Will print even index value
    if index%2==0:
        print(item, end=",")


l1=[1,2,3,4,5,6,7,8,9]

for index,item in enumerate(l1):
    if index%2!=0:
        print(item)