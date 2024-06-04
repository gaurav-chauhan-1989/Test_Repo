print("Enter Your age")
a=int(input())                                #To take input from user. int() is used to convert user input into int
                                              # By default user input is of string type

if a>70:
    print("You are too old to drive")

elif a>18:
    print("You can drive")

elif a==18:
    print("You can drive with assist")

else:
    print("You cannot drive")

l=[1,3,6,8]
if 10 in l:
    print("Match Found")

else:
    print("Match not found")