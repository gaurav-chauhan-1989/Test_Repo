

class AgeError(Exception):
    def __init__(self,msg):
        self.msg=msg

age=12
try:
    if age<18:
        raise AgeError(f"Age ({age}) should be greater than 18")

except AgeError as e:
    print(e.msg)
print("Hello World")

