def mayor(x, y):
    if x > y:
        return x
    return y   


a = 17
b = 16
c = 14
d = 67

maximo = mayor(mayor (a, b), mayor(c, d))

print (maximo)