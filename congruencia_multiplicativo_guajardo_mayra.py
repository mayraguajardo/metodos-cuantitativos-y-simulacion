xn = 5
n = 0
def metodo(xn,n):
    a = 5
    m = 32
    val1 = a * xn 
    val2 = val1 % m
    n += 1
    print (val2)
    if(n<=10):
        metodo(val2,n)


metodo(xn,n)