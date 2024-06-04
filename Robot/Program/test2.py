f=open("io.txt","r+")
a = f.readlines()
d = {}
e = {}
for i in a:
    s = i.split(" ")
    if s[0] in d:
        d[s[0]] +=1
        e[s[0]] = s[-1]

    else:
        d[s[0]] = 1
        e[s[0]] = s[-1]

print(d)
print(e)
