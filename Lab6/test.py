import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy import interpolate
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import time
plotly.tools.set_credentials_file(username='moniad', api_key='uBGLg0vf0VvXFSyD261T')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')

def f3(x, y):
    return np.sin(x) * np.cos(x)

def f4(x, y):
    return pow(x, y)

def f5(x, y):
    return x * y + 2

def spline_interpolation(f, a, b, n):
    start = time.time()
        
    x = np.arange(a, b, 1e-2)
    y = np.arange(a, b, 1e-2)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(xx) * np.cos(yy)
    f = interpolate.interp2d(x, y, z, kind='cubic')

    xnew = np.arange(a, b, (b-a)/n)
    ynew = np.arange(a, b, (b-a)/n)
    znew = f(xnew, ynew)

    trace1 = go.Scatter3d(
        x=x,
        y=y,
        z=z[0, :],
        name='Data',
        marker = dict(
            size = 0
        )
    )

    trace2 = go.Scatter3d(
        x=ynew,
        y=xnew,
        z=znew[0, :],
        marker=dict(
            size=3,
        ),
        name='Linear Interpolated Data'
    )

    layout = go.Layout(
        title='Interpolation and Extrapolation in 2D',
        scene=dict(
                camera= dict(
                    up=dict(x=0, y=0, z=1),
                    center=dict(x=0, y=0, z=0),
                    eye=dict(x=1, y=-1, z=0)
                )
        )
    )

    data = [trace1, trace2]

    # end of measuring time
    end = time.time()
    print("time: ", end-start)

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename = 'graph')

def main():
    a = (float) (input("Give me the left x limit: "))
    b = (float) (input("Give me the right x limit: "))
    # c = (float) (input("Give me the left y limit: "))
    # d = (float) (input("Give me the right y limit: "))
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
        spline_interpolation(f, a, b, n)
        print("\n")

if __name__== "__main__":
    main()