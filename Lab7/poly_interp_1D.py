import numpy as np
from scipy.linalg import solve
import matplotlib
import matplotlib.pyplot as plt
import time

distance = 0.1 # between points - to be able to plot precisely

def f5(x):
    return 5 * np.sin(x)

def f6(x):
    return 6 * np.exp(x)

def f7(x):
    return x * np.cos(x)

def gen(max_pow):
    powers = list(range(max_pow))
    desc_powers = powers[::-1]
    # print(desc_powers)
    for p in desc_powers:
        yield p

# solving A * coef = b, where coef is a vector of coefficients
def getCoefficients(x, f):
    A = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(x[i]**j)
        A.append(row[::-1])
    # print("A = ", A, "\n")

    b = [fx for fx in list(f(x) for x in x)]
    # print("b = ", b, "\n")
    coef = solve(A, b)
    # print("coefficients after solving:\n", coef, "\n")
    return coef


def poly_elem(a, n):
    # print("a = ", a, " n = ", n)
    return lambda x : a * (x ** n)

def polynomial(x):
    poly = 0.0
    for a, p in zip(coef, gen(N)):
        poly += poly_elem(a, p)(x)
    return poly
  
def plot_graph(x, f1, f2, file_name):
    plt.plot(x, f1(x), 'r')
    plt.plot(x, f2(x), 'b')
    plt.savefig(file_name)
    plt.show()

def main():
    a = int(input("Give me left limit: "))
    b = int(input("Give me right limit: "))
    global N
    N = int(input("Give me number of interpolation points: "))
    nodes = np.linspace(a, b, N) # interpolation nodes
    all_nodes = np.arange(nodes[0], nodes[N-1], distance)
    
    # polynomial interpolation
    start = time.time()
    global coef
    coef = getCoefficients(nodes, f5)
    end = time.time()
    print("time = ", end - start)
    plot_graph(all_nodes, f5, polynomial, "poly_f5.png")

    start = time.time()
    coef = getCoefficients(nodes, f6)
    end = time.time()
    print("time = ", end - start)
    plot_graph(all_nodes, f6, polynomial, "poly_f6.png")


    start = time.time()
    coef = getCoefficients(nodes, f7)
    end = time.time()
    print("time = ", end - start)
    plot_graph(all_nodes, f7, polynomial, "poly_f7.png")

    # efekt Rungego przy np. a = 1, b = 30, N = 15

if __name__== "__main__":
    main()