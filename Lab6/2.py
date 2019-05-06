# Linear, polynomial and spline interpolation 2D
import math
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

spline_points_count = 10

def plot_interpolated_function(f, a, b, c, d, n):
    x = np.arange(a, b, (b-a)/n) # the last arg is step
    y = np.arange(c, d, (d-c)/n)
    
    X, Y = np.meshgrid(x, y) # returns coordinate matrices from coordinate vectors
    Z = f(X,Y) # function values on the grid

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                        cmap=cm.RdBu, linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


# def linear_interpolation(f, a, b, n):
#     plot_interpolated_function(f, a, b, n)
    
#     # measuring time
#     start = time.time()
#     # coefficients = []
#     h = (b-a)/n
#     print("h = ", h)
#     x_cur = a
#     while(x_cur < b):
#         x_next = x_cur + h
#         print("Xnext: ", x_next)
#         # interpolate
#         a_i = (f(x_next) - f(x_cur))/h
#         b_i = f(x_cur) - a_i * x_cur
#         # tuple_a_b = (a_i, b_i)
#         _range = np.array([x_cur, x_next])
#         plt.plot(_range, _range * a_i + b_i, 'm')
#         # coefficients.append(tuple_a_b)
#         x_cur = x_next

#     # end of measuring time
#     end = time.time()
#     print("time: ", end-start)
#     plt.legend(loc='upper left')
#     plt.show()
#     # return coefficients

# def polynomial_interpolation(f, a, b, n):
#     plot_interpolated_function(f, a, b, n)
    
#     # measuring time
#     start = time.time()
#     x = np.linspace(a, b, n)
#     poly = lagrange(x, f(x))
#     # print("poly: ", poly)
#     plt.plot(x, poly(x), 'g')
#     # end of measuring time
#     end = time.time()
#     print("time: ", end-start)
#     plt.legend(loc='upper left')
#     plt.show()

def spline_interpolation(f, a, b, c, d, n):
    plot_interpolated_function(f, a, b, c, d, n)   
    # measuring time
    start = time.time()
    
    # x = np.arange(a, b, (b-a)/spline_points_count) # the last arg is step
    # y = np.arange(c, d, (d-c)/spline_points_count)
    # X, Y = np.meshgrid(x, y) # returns coordinate matrices from coordinate vectors
    # f_x_y = f(x,y)


    # h = (b-a)/n
    # print("h = ", h)
    # x_cur = a
    # while(x_cur < b):
    #     x_next = x_cur + h
    #     # interpolate
    #     x = np.linspace(x_cur, x_next, spline_points_count)
    #     y = []
    #     for x_i in x:
    #         y.append(f(x_i))
    #     slope, intercept = np.polyfit(x, y, 1)
    #     plt.plot(x, slope * x + intercept, 'b')
    #     # coefficients.append(tuple_a_b)
    #     x_cur = x_next
    
    # # end of measuring time
    # end = time.time()
    # print("time: ", end-start)
    # plt.legend(loc='upper left')
    # plt.show()

# def get_fct_values(f, a, b, n):
#     h = (b-a)/n
#     print("h = ", h)
#     # x_cur = a
#     y = []
#     for i in range(0, n):
#         x_cur = a + i * h
#         # x_next = a + (i+1) * h
#         y.append(f(x_cur))
#     print("y: ", y)
#     return y

# def f1(x):
#     return 5 * x

def f3(x, y):
    return (1-(x**2+y**3))*np.exp(-(x**2+y**2)/2)
 
    # return np.sin(x) * np.cos(x)

def f4(x, y):
    return pow(x, y)

def f5(x, y):
    return x * y + 2

def main():
    a = (float) (input("Give me the left x limit: "))
    b = (float) (input("Give me the right x limit: "))
    c = (float) (input("Give me the left y limit: "))
    d = (float) (input("Give me the right y limit: "))
    n = (int) (input("Give me the number of interpolation nodes: "))

    # interpolating f3, f4, f5
    for i in range(0, 3):
        if i == 0: f = f3
        elif i == 1: f = f4
        else: f = f5
        
        # fct_values = get_fct_values(f1, a, b, n)
        print("Time taken to interpolate f(x) = ", f, " using: ")
    # -----------------------------------------------
        print("- linear interpolation:")
        # linear_interpolation(f, a, b, n)
        print("\n")
    # -----------------------------------------------
        print("- polynomial interpolation:")
        # polynomial_interpolation(f, a, b, n)
        print("\n")
    # -----------------------------------------------
        print("- spline interpolation:")
        spline_interpolation(f, a, b, c, d, n)
        print("\n")

if __name__== "__main__":
    main()