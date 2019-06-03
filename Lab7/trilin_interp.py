# Linear interpolation 3D, plotting in 4D as a heatmap
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

distance = 0.01

def plot_interpolated_function(f):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.arange(x_x, x_y, (x_y-x_x)/n * distance) # the last arg is step
    y = np.arange(y_x, y_y, (y_y-y_x)/n * distance)
    z = np.arange(z_x, z_y, (z_y-z_x)/n * distance)
    
    c = f(x,y,z)

    img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
    fig.colorbar(img)

    # added this line
    ax.text2D(0.05, 0.95, "InterpolatED function", transform=ax.transAxes)

    plt.show()


# def plot_interpolating_function(f):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     x = np.arange(x_x, x_y, (x_y-x_x)/n * distance) # the last arg is step
#     y = np.arange(y_x, y_y, (y_y-y_x)/n * distance)
#     z = np.arange(z_x, z_y, (z_y-z_x)/n * distance)
#     # x = np.random.standard_normal(100)
#     # y = np.random.standard_normal(100)
#     # z = np.random.standard_normal(100)
#     c = f(x,y,z) # np.random.standard_normal(100)

#     img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
#     fig.colorbar(img)

#     # added this line
#     ax.text2D(0.05, 0.95, "InterpolatING function", transform=ax.transAxes)

#     plt.show()


def getCoefficients(f, x0, x1, y0, y1, z0, z1):
    row1 = [1.0, x0, y0, z0, x0*y0, x0*z0, y0*z0, x0*y0*z0]
    row2 = [1.0, x1, y0, z0, x1*y0, x1*z0, y0*z0, x1*y0*z0]
    row3 = [1.0, x0, y1, z0, x0*y1, x0*z0, y1*z0, x0*y1*z0]
    row4 = [1.0, x1, y1, z0, x1*y1, x1*z0, y1*z0, x1*y1*z0]
    row5 = [1.0, x0, y0, z1, x0*y0, x0*z1, y0*z1, x0*y0*z1]
    row6 = [1.0, x1, y0, z1, x1*y0, x1*z1, y0*z1, x1*y0*z1]
    row7 = [1.0, x0, y1, z1, x0*y1, x0*z1, y1*z1, x0*y1*z1]
    row8 = [1.0, x1, y1, z1, x1*y1, x1*z1, y1*z1, x1*y1*z1]

    A = []
    A.append(row1)
    A.append(row2)
    A.append(row3)
    A.append(row4)
    A.append(row5)
    A.append(row6)
    A.append(row7)
    A.append(row8)

    print("A = ", A, "\n")

    b = [f(x0, y0, z0), f(x1, y0, z0), f(x0, y1, z0), f(x1, y1, z0), 
         f(x0, y0, z1), f(x1, y0, z1), f(x0, y1, z1), f(x1, y1, z1)]
    
    print("b = ", b, "\n")
    coef = solve(A, b)
    print("coefficients after solving:\n", coef, "\n")
    return coef


def interp_fun_in_volume(coef):
    # print("coef = ", coef)
    if len(coef) != 8:
        print("Number of coefficients should be 8!\n")
        exit(-1)
    return lambda x: (lambda y: (lambda z: coef[0] + coef[1] * x + 
        coef[2] * y + coef[3] * z + coef[4] * x * y + coef[5] * x * z +
        coef[6] * y * z + coef[7] * x * y * z))


def trilinear_interpolation(f):
    
    # measuring time
    start = time.time()
    coef = getCoefficients(f, x_x, x_y, y_x, y_y, z_x, z_y)
    print("value in interpolated function: ", interp_fun_in_volume(coef)(1)(2)(3))

    # plot_interpolating_function(f)
    # end of measuring time
    end = time.time()
    print("time: ", end-start)
    plt.show()

def f3(x, y, z):
    return np.sin(x) * 3 * y + z # * np.cos(x)

def f4(x, y, z):
    return pow(x, y) * z

def f5(x, y, z):
    return x * y + 2 + z


def main():
    global x_x, x_y, y_x, y_y, z_x, z_y, n
    x_x = (float) (input("Give me the left x limit: "))
    x_y = (float) (input("Give me the right x limit: "))
    y_x = (float) (input("Give me the left y limit: "))
    y_y = (float) (input("Give me the right y limit: "))
    z_x = (float) (input("Give me the left z limit: "))
    z_y = (float) (input("Give me the right z limit: "))
    n = (int) (input("Give me the number of interpolation nodes: "))

    # interpolating f3, f4, f5
    for i in range(0, 3):
        if i == 0: f = f3
        elif i == 1: f = f4
        else: f = f5
        
        print("Time taken to interpolate f(x) = ", f.__name__, " using: ")
    # -----------------------------------------------
        print("- trilinear interpolation:")
        plot_interpolated_function(f)
        trilinear_interpolation(f)

        print("\n")
        
if __name__== "__main__":
    main()