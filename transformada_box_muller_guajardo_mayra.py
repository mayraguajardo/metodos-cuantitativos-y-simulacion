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
    array_box_muller = []
    
    for _ in range(n):
        val1 = a * xn + c
        val2 = val1 % m
        val_normal = round(val2/m,5)
        # print (val_normal)
        array.append(val_normal)
        xn = val2
    
    for i in range(0,n,2):
        r1 = array[i]
        r2 = array[i+1]
        x1 = math.sqrt(-2 * math.log(r1)) * math.cos(2 * math.pi * r2)
        array_box_muller.append(x1)
        x2 = math.sqrt(-2 * math.log(r1)) * math.sin(2 * math.pi * r2)
        array_box_muller.append(x2)

    plt.title('Box Muller_ Normal Distribution')
    plt.hist(array_box_muller, bins=50, alpha=1, edgecolor = 'white',  linewidth=1)
    plt.grid(True)
    plt.show()
    plt.clf()

metodo(xn,n)
