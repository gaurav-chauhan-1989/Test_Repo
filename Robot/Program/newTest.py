def solution(S):
    count = 1
    city = []
    for i in S:
        city.append(i.split(',')[1])

    for j in range(len(S)):
        S[j] = S[j].split(',')[1] + str(count) + '.' + (S[j].split(',')[0]).split('.')[1]
        count +=1
    return S


s = ["photo.jpg, Warsaw, 2013-09-05 14:08:15", "john.png, London, 2015-06-20 15:13:22"]
z = solution(s)
print(z)





