def suma(x, y):
    res = x + y
    return res

print(suma(3,4))

def mayor_de_dos(a,b):
    res = -1
    if(a>b):
        res = a
    else:
        res = b
    return res


def mayor_a_tres(a,b,c):
    res = -1
    if(a<b):
     if(a>c):
        return a
     else:
        if(b>c):
            return b
        else:
           return c

    print(mayor_a_tres(12, 23, 56))
