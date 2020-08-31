xn = 7 #semilla 
n = 0 
def metodo(xn,n):
    a = 22695477 #multiplicador
    c = 1 # incremento
    m = 13 # max
    val1 = a * xn + c
    val2 = val1 % m
    n += 1
    print (val2)
    if(n<=10000):
        metodo(val2,n)


metodo(xn,n)
