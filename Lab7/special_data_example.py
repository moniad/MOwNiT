import numpy as np
from scipy.linalg import solve
import matplotlib
import matplotlib.pyplot as plt

distance = 0.1 # between points - to be able to plot precisely
def f5(x):
    return 5 * np.sin(x)

def f6(x):
    return 6 * x

def gen(max_pow):
    powers = list(range(max_pow))
    desc_powers = powers[::-1]
    # print(desc_powers)
    for p in desc_powers:
        yield p

def getCoefficients(x, N, f):
    A = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(x[i]**j)
        A.append(row[::-1])
    print("A = ", A, "\n")

    b = [fx for fx in list(f(x) for x in x)]

# ----------

    b = [0, 2, 3, 5, 1, 2]

# ---------
    print("b = ", b, "\n")
    coef = solve(A, b)
    print("coefficients after solving:\n", coef, "\n")
    return coef

def plot_graph(x, f1, f2, file_name):
    # plt.plot(x, f1(x), 'r')
    plt.plot(x, f2(x), 'b')
    plt.savefig(file_name)
    plt.show()

# ----------



x = [2, 3, 6, 7, 8, 10]



# -------------

# a = int(input("Give me left limit: "))
# b = int(input("Give me right limit: "))
# N = int(input("Give me number of interpolation points: "))
# # x = np.arange(a, b, (b-a)/N)
# x = np.linspace(a, b, N)

N = 6


# ------------
print("x = ", x)
print("xlenth: ", len(x))

global rev_coef
coef = getCoefficients(x, N, f5)
# rev_coeff = coef[::-1]
# print("reversed coefficients: ", rev_coeff, "\n")
# # print("pairs (coef, x): ", [(c,x) for c, x in zip(coef[::-1], x)], "\n")
print("(coef, pow): ", [(c,p) for c, p in zip(coef, gen(N))], "\n")


def poly_elem(a, n):
    print("a = ", a, " n = ", n)
    return lambda x : a * (x ** n)

def polynomial(x):
    poly = 0.0
    for a, p in zip(coef, gen(N)):
        poly += poly_elem(a, p)(x)
    return poly

all_x = np.arange(x[0], x[N-1], distance)
print("all_x = ", all_x)
plot_graph(all_x, f5, polynomial, "test.png")
