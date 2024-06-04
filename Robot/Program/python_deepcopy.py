import copy

l=[[1,2],[2,3],[4,5]]

s=copy.deepcopy(l)                       # Create deep copy of list object
print(s)
print(l)

s[2][1]=10                          # If we update copied list. Changes will not reflect on original list
print(s)
print(l)


""" When we create a deepcopy python create a compound object (like list, set)
then it insert copy of recursive child objects from original object

Note: Copy and deepcopy diff is only for compound object (like list, set, class instance)
"""