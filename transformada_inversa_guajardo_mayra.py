import math
import time
from datetime import datetime
import matplotlib.pyplot as plt

xn = int(time.mktime(datetime.now().timetuple()))
n = 10000
lambda1 = 0.5
lambda2 = 1
lambda3 = 1.5

def metodo(xn,n):
    a = 22695477 #multiplicador
    c = 1 # incremento
    m =  math.pow(2,32)# max
    array = []
    array_linear_regression1 = []
    array_linear_regression2 = []
    array_linear_regression3 = []
    
    for _ in range(n):
        val1 = a * xn + c
        val2 = val1 % m
        val_normal = round(val2/m,5)
        # print (val_normal)
        array.append(val_normal)
        xn = val2
    
    for i in array:
        x1  = -1*(math.log(1-i)/lambda1)
        x2  = -1*(math.log(1-i)/lambda2)
        x3  = -1*(math.log(1-i)/lambda3)
        
        array_linear_regression1.append(x1)
        array_linear_regression2.append(x2)
        array_linear_regression3.append(x3)

    plt.title('Transformada Inversa')
    plt.scatter(array_linear_regression1, array)
    plt.scatter(array_linear_regression2, array)
    plt.scatter(array_linear_regression3, array)
    plt.grid(True)
    plt.show()
    

metodo(xn,n)
