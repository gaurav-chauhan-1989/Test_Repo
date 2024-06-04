import pickle

#cars=['Audi','BMW','Skoda','Mercedes']

#file="car.pkl"
#fileobj= open(file,"wb")
#pickle.dump(cars, fileobj)

file="car.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)

