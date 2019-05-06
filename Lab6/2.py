# Linear, polynomial and spline interpolation 2D
import math
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

spline_points_count = 10

def plot_interpolated_function(f, a, b, n):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(a,b,n*100)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none') # remove unnecessary borders
    ax.spines['top'].set_color('none')
    plt.plot(x, f(x), '-r', label='Interpolated fct')

def linear_interpolation(f, a, b, n):
    plot_interpolated_function(f, a, b, n)
    
    # measuring time
    start = time.time()
    # coefficients = []
    h = (b-a)/n
    print("h = ", h)
    x_cur = a
    while(x_cur < b):
        x_next = x_cur + h
        print("Xnext: ", x_next)
        # interpolate
        a_i = (f(x_next) - f(x_cur))/h
        b_i = f(x_cur) - a_i * x_cur
        # tuple_a_b = (a_i, b_i)
        _range = np.array([x_cur, x_next])
        plt.plot(_range, _range * a_i + b_i, 'm')
        # coefficients.append(tuple_a_b)
        x_cur = x_next

    # end of measuring time
    end = time.time()
    print("time: ", end-start)
    plt.legend(loc='upper left')
    plt.show()
    # return coefficients

def polynomial_interpolation(f, a, b, n):
    plot_interpolated_function(f, a, b, n)
    
    # measuring time
    start = time.time()
    x = np.linspace(a, b, n)
    poly = lagrange(x, f(x))
    # print("poly: ", poly)
    plt.plot(x, poly(x), 'g')
    # end of measuring time
    end = time.time()
    print("time: ", end-start)
    plt.legend(loc='upper left')
    plt.show()

def spline_interpolation(f, a, b, n):
    plot_interpolated_function(f, a, b, n)
    
    # measuring time
    start = time.time()
    h = (b-a)/n
    print("h = ", h)
    x_cur = a
    while(x_cur < b):
        x_next = x_cur + h
        # interpolate
        x = np.linspace(x_cur, x_next, spline_points_count)
        y = []
        for x_i in x:
            y.append(f(x_i))
        slope, intercept = np.polyfit(x, y, 1)
        plt.plot(x, slope * x + intercept, 'b')
        # coefficients.append(tuple_a_b)
        x_cur = x_next
    
    # end of measuring time
    end = time.time()
    print("time: ", end-start)
    plt.legend(loc='upper left')
    plt.show()

def f1(x):
    if(x > 0):
        return np.exp(-x*x) * pow(math.log(x),2)
    return -500.0

def f2(x):
    denominator = math.pow(x, 3) - 2*x - 5
    if(denominator != 0):
        return 1/denominator
    return -500.0

def f3(x):
    return np.sin(x)

def f4(x):
    # print("f(x) = 2^x")
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
    # -----------------------------------------------
        print("- polynomial interpolation:")
        polynomial_interpolation(f, a, b, n)
        print("\n")
    # -----------------------------------------------
        print("- spline interpolation:")
        spline_interpolation(f, a, b, n)
        print("\n")

    
if __name__== "__main__":
    main()