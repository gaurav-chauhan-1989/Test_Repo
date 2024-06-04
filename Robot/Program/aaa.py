string="Hello World"                        # To remove duplicate value from a string
a = "".join(dict.fromkeys(string))          # dict.fromkeys will remove the duplicate characters and put it in keys
print(a)                                    # "".join will join the keys as string in insertion order
