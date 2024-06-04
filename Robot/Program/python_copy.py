"""In shallow copy python first create an compound object(like list,set etc) then insert reference of child object (
Inner list (list under list l) in below example) from original object (list l in below example)
"""

import copy

l=[[1,2],[4,5],[7,8]]
a=copy.copy(l)                                # Create shallow copy of list (l) object
print(l)
print(a)
a[1][1]=10
print(a)
print(l)

a.append([8,9])
print(a)
print(l)
