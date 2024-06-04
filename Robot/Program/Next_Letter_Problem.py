def next_char(n):
    s = ''
    for i in n:
        if i=='z':
            s += 'a'
        else:
            s += chr(ord(i)+1)
    return s

x = next_char('Hellz')
print(x)