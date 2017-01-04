# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01 * x**2 + 0.1*x
    
def liner(a,b,x):
    return x*a + b
    
def calcb(a,x1,y1):
    return y1 - a*x1

def main():
    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    d1=numerical_diff(function_1,5))
    d2=numerical_diff(function_1,10))
    plt.show()

if __name__ == '__main__':
    main() 