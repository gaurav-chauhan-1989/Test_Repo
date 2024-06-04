class emp:
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}.{lname}@abc.com"

    def details(self):
        print(f"Name is {self.fname} {self.lname}")
        print(self.email)

obj=emp("Gaurav", "Chauhan")
obj.details()
obj.fname="Archana"
obj.details()
obj.email="archana.chauhan@gmail.com"
obj.details()