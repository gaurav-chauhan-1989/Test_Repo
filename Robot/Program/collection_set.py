s1=set()
print(type(s1))

s1.add("Gaurav")
s1.add("Archana")
print(s1)
s1.add("Gaurav")                                     # Set only consume unique values, no duplicate value in set
print(s1)
s2=set()
s2.add(1)
print(s2)
s2.add(43)
s2.add(23)
print(s2)
print(max(s2))                                      # max() to print maximum value in set,list tuple
s = {1,2,3,4,5,6,1}                                 # Set is unordered hence cannot have any fixed index
print(s)
s.add(9)
print(s)
set2={1,2,3}
print(set2)
set2.add(4)
print(set2)
set1 = {(1,2,3,4), [1,2,3]}                    # Set only take immutable objects however set himself is mutable