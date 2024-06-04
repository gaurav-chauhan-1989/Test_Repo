dict={}                                               # To create empty dictionary

dict.update({"1":"Gaurav"})                           # Updating dictionary (1 is key and Gaurav is value)
print(dict)

print(dict["1"])                                      # To print certain value

dict["2"]="Chauhan"                                   # Add key and value in Dictionary
print(dict)

print(dict.keys())                                    # To print only keys

print(dict.values())                                  # To print only values

dict["2"]="Rajput"                                    # To change the value for specific key
print(dict)

dict1=dict.copy()                                    # To create a separate copy of dictionary
dict1["3"]="Archana"
print(dict)
print(dict1)

del(dict1["2"])                                      # To delete specific key and value for dictionary
print(dict1)

list=list(dict.values())                                      # To convert dictionary values to list
print(list)
