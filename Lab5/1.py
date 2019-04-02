# Numeral integration
import math
import numpy as np
import time
from scipy import integrate

# def have_dif_sign(f_x, f_y):
#     return f_x < 0 and f_y > 0 or f_x > 0 and f_y < 0

def adaptive_quadrature(f, a, b, n):
    return integrate.quadrature(f, a, b)

def rectangle_rule(f, a, b, n):
    h = (b-a)/n
    x_i = a
    sum = 0.0
    for _ in range(0, n+1):
        f_x_i = f(x_i)
        if f_x_i == -500.0:
            print("Infinite integral")
            return
            # x_i_temp = x_i - 0.1 # hope it's enough
            # f_x_i = f(x_i_temp)

        sum += math.fabs(f_x_i) * h
        x_i += h
        # print("next: ", x_next, " prev: ", x_prev)
    return sum

def trapezoidal_rule(f, a, b, n):
    h = (b-a)/n
    x_prev = a
    x_next = x_prev
    sum = 0.0
    for _ in range(0, n+1):
        x_prev = x_next
        x_next += h
        # print("next: ", x_next, " prev: ", x_prev)
        f_x_prev = f(x_prev) # I think that case below won't happen
        if f_x_prev == -500:
            print("Infinite integral")
            return
        #     x_next_temp = x_next - 0.1
        #     f_x_prev = f(x_next_temp)

        f_x_next = f(x_next)
        if f_x_next == -500.0:
            # x_next_temp = x_next - 0.1
            # f_x_next = f(x_next_temp)
            print("Infinite integral")
            return

        sum += (math.fabs(f_x_next) + math.fabs(f_x_prev)) * h / 2
    return sum

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
    return math.pow(x, 2) * np.exp(-x) * math.sin(x)

def f4(x):
    return pow(2, x)

def f5(x):
    return 5.0

def main():
    a = (float) (input("Give me the left limit: "))
    b = (float) (input("Give me the right limit: "))
    n = (int) (input("Give me the number of ranges: "))

    print("Time taken to integrate using: ")
# -----------------------------------------------
    print("- trapezoidal rule:")
    start = time.time()
    # integrating f1, f2, f3, f4, f5 using trapezoidal and rectangle rule
    print("result - f5: ", trapezoidal_rule(f5, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- rectangle rule: ")
    start = time.time()
    print("result - f5: ", rectangle_rule(f5, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- adaptive quadrature: ")
    start = time.time()
    print("result: - f5 ", adaptive_quadrature(f5, a, b, n))
    end = time.time()
    print("time: ", end-start)
    print("\n")
# -----------------------------------------------
    print("- trapezoidal rule:")
    start = time.time()
    print("result: - f1 ", trapezoidal_rule(f1, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- rectangle rule: ")
    start = time.time()
    print("result: - f1 ", rectangle_rule(f1, a, b, n))
    end = time.time()
    print("time: ", end-start)

    # print("- adaptive quadrature: ")
    # start = time.time()
    # print("result: - f1 ", adaptive_quadrature(f1, a, b, n))
    # end = time.time()
    # print("time: ", end-start)
    print("\n")
# -----------------------------------------------
    print("- trapezoidal rule:")
    start = time.time()
    print("result: - f2 ", trapezoidal_rule(f2, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- rectangle rule: ")
    start = time.time()
    print("result: - f2 ", rectangle_rule(f2, a, b, n))
    end = time.time()
    print("time: ", end-start)

    # print("- adaptive quadrature: ")
    # start = time.time()
    # print("result: - f2 ", adaptive_quadrature(f2, a, b, n))
    # end = time.time()
    # print("time: ", end-start)
    print("\n")
# -----------------------------------------------
    print("- trapezoidal rule:")
    start = time.time()
    print("result: - f3 ", trapezoidal_rule(f3, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- rectangle rule: ")
    start = time.time()
    print("result: - f3 ", rectangle_rule(f3, a, b, n))
    end = time.time()
    print("time: ", end-start)

    # print("- adaptive quadrature: ")
    # start = time.time()
    # print("result: - f3 ", adaptive_quadrature(f3, a, b, n))
    # end = time.time()
    # print("time: ", end-start)
    print("\n")
# -----------------------------------------------
    print("- trapezoidal rule:")
    start = time.time()
    print("result: - f4 ", trapezoidal_rule(f4, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- rectangle rule: ")
    start = time.time()
    print("result: - f4 ", rectangle_rule(f4, a, b, n))
    end = time.time()
    print("time: ", end-start)

    print("- adaptive quadrature: ")
    start = time.time()
    print("result: - f4 ", adaptive_quadrature(f4, a, b, n))
    end = time.time()
    print("time: ", end-start)
    print("\n")
    
    print("Na logikę - całkowanie prostokątami powinno wyjść mniejsze, a nie takie 2 razy za duże :/")

if __name__== "__main__":
    main()