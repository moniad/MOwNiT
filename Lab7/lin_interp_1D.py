# Linear interpolation 1D
import math
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def plot_interpolated_function(f, a, b, n):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(a,b,n*100)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none') # remove unnecessary borders
    ax.spines['top'].set_color('none')
    plt.plot(x, f(x), '-r')

def linear_interpolation(f, a, b, n):
    plot_interpolated_function(f, a, b, n)
    
    # measuring time
    start = time.time()
    h = (b-a)/n
    print("h = ", h)
    x_cur = a
    while(x_cur < b):
        x_next = x_cur + h
        # print("Xnext: ", x_next)
        # interpolate
        a_i = (f(x_next) - f(x_cur))/h
        b_i = f(x_cur) - a_i * x_cur
        _range = np.array([x_cur, x_next])
        # plot next part of the graph
        plt.plot(_range, _range * a_i + b_i, 'm')
        x_cur = x_next

    # end of measuring time
    end = time.time()
    print("time: ", end-start)
    plt.show()

def f3(x):
    return np.sin(x)

def f4(x):
    return pow(2, x)

def f5(x):
    return 5 * x + 2

def main():
    a = (float) (input("Give me the left limit: "))
    b = (float) (input("Give me the right limit: "))
    n = (int) (input("Give me the number of interpolation nodes: "))

    # interpolating f3, f4, f5
    for i in range(0, 3):
        if i == 0: f = f3
        elif i == 1: f = f4
        else: f = f5
        
        print("Time taken to interpolate f(x) = ", f, " using: ")
    # -----------------------------------------------
        print("- linear interpolation:")
        linear_interpolation(f, a, b, n)
        print("\n")

if __name__== "__main__":
    main()