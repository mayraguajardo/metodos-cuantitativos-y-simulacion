import math
import time
from datetime import datetime
import matplotlib.pyplot as plt
xn = int(time.mktime(datetime.now().timetuple()))
n = 10000 


def metodo(xn,n):
    a = 22695477 #multiplicador
    c = 1 # incremento
    m =  math.pow(2,32)# max
    array = []
    for _ in range(n):
        val1 = a * xn + c
        val2 = val1 % m
        val_normal = round(val2/m,5)
        # print (val_normal)
        array.append(val_normal)
        xn = val2
    plt.title('PRUEBA')
    plt.hist(array, bins=50, alpha=1, edgecolor = 'black',  linewidth=1)
    plt.grid(True)
    plt.show()
    plt.clf()

metodo(xn,n)
