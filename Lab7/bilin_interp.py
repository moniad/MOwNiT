# Linear interpolation 2D
import math
import numpy as np
import time
from scipy.linalg import solve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

distance = 0.1

def just_plot(X, Y, Z, text):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                        cmap=cm.RdBu, linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.text2D(0.05, 0.95, text, transform=ax.transAxes)

    plt.show()



def plot_interpolated_function(f, text):
    X, Y = np.meshgrid(all_x, all_y) # returns coordinate matrices from coordinate vectors
    Z = f(X,Y) # function values on the grid (all combinations of (x_i,y_i))

    just_plot(X, Y, Z, text)


def getCoefficients(f, x1, x2, y1, y2):
    row1 = [1.0, x1, y1, x1*y1]
    row2 = [1.0, x1, y2, x1*y2]
    row3 = [1.0, x2, y1, x2*y1]
    row4 = [1.0, x2, y2, x2*y2]

    A = []
    A.append(row1)
    A.append(row2)
    A.append(row3)
    A.append(row4)

    print("A = ", A, "\n")

    b = [f(x1, y1), f(x1, y2), f(x2, y1), f(x2, y2)]
    
    print("b = ", b, "\n")
    coef = solve(A, b)
    print("coefficients after solving:\n", coef, "\n")
    return coef


def plot_interpolating_function(f, text):

    X, Y = np.meshgrid(all_x, all_y) # returns coordinate matrices from coordinate vectors
    print("X = ", X, "\nY = ", Y)
    Z = f(X, Y) # function values on the grid

    just_plot(X, Y, Z, text)


def interp_range_function(coef):
    # print("coef = ", coef)
    if len(coef) != 4:
        print("Number of coefficients should be 4!\n")
        exit(-1)
    return lambda x: (lambda y: coef[0] + coef[1] * x + coef[2] * y + coef[3] * x * y)

def interpolating_function(x, y):
    h_x = (b - a) / n
    # h_y = (y_y - y_x) / n
    # I think that checking one dimension is enough
    for i in range(n-1):
        if(x <= a + h_x * (i+1)):
            return interp_range_function(all_coefficients[i])(x)(y)

    # print("len(all_coef) = ", len(all_coefficients))
    # print("all_coefficients: ", all_coefficients)
    return interp_range_function(all_coefficients[n-2])(x)(y)
    # print("Problem with points!")


def interpol_wrapper(X, Y):
    result = []
    print("X len = ", len(X))
    for i in range(len(X)):
        row = []
        for j in range(len(X)):
            # print("appending: ", interpolating_function(X[i][j], Y[i][j]))
            row.append(interpolating_function(X[i][j], Y[i][j]))
        result.append(row)
    return np.array(result)

def bilinear_interpolation(f):
    x = np.arange(a, b, (b-a)/n)
    y = np.arange(a, b, (b-a)/n)
    for i in range(n-1):
        coef = getCoefficients(f, x[i], x[i+1], y[i], y[i+1])
        all_coefficients.append(coef)

    plot_interpolating_function(interpol_wrapper, "InterpolatING function")

    plt.show()

def f3(x, y):
    return np.sin(x) # * np.cos(x)

def f4(x, y):
    return pow(x, y)

def f5(x, y):
    return x * y + 2

def main():
    global a, b, c, d, n
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
        
        print("Time taken to interpolate f(x) = ", f.__name__, " using: ")
    # -----------------------------------------------
        print("- bilinear interpolation:")

        global all_coefficients
        all_coefficients = []

        global all_x, all_y
        all_x = np.arange(a, b, (b-a)/n * distance) # the last arg is step
        all_y = np.arange(c, d, (d-c)/n * distance)


        plot_interpolated_function(f, "InterpolatED function")
        
        # measuring time
        start = time.time()
        bilinear_interpolation(f)
        # end of measuring time
        end = time.time()
        print("time: ", end-start)

        print("\n")


        # print("getCoefficients : ")
        # getCoefficients(f3, a, b, c, d)
    
        # func = interp_range_function([1, -1, 2, 0])(5)(3)
        # print("testing function: ", interp_range_function([1, -1, 2, 0])(5)(3)) # (5)(3))

if __name__== "__main__":
    main()

# a = 1, b = 10, c = 2, d = 10, n = 10