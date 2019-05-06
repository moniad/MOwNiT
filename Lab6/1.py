# Linear, polynomial and spline interpolation
import math
import numpy as np
import time
import matplotlib.pyplot as plt

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

    print("Time taken to interpolate using: ")
# -----------------------------------------------
    print("- linear interpolation:")
    # interpolating f1, f2, f3, f4, f5 using linear interpolation
    print("result - f3(x) = sin(x); ")
    linear_interpolation(f3, a, b, n)
    print("\n")
# -----------------------------------------------
#     print("- polynomial interpolation:")
#     start = time.time()
#     print("result: - f1 ", trapezoidal_rule(f1, a, b, n))
#     end = time.time()
#     print("time: ", end-start)

#     print("- another adaptive quadrature: ")
#     start = time.time()
#     print("result: - f1 ", another_adaptive_quadrature(f1, a, b, error))
#     end = time.time()
#     print("time: ", end-start)
#     print("\n")
# # -----------------------------------------------
#     print("- spline interpolation:")
#     start = time.time()
#     print("result: - f2 ", trapezoidal_rule(f2, a, b, n))
#     end = time.time()
#     print("time: ", end-start)

#     print("- rectangle rule: ")
#     start = time.time()
#     print("result: - f2 ", rectangle_rule(f2, a, b, n))
#     end = time.time()
#     print("time: ", end-start)
    
if __name__== "__main__":
    main()