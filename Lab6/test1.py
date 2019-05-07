# polynomial interpolation

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)


# generate points used to plot
x_plot = np.linspace(0, 10, 100)
x = x_plot
y = f(x)

# create matrix versions of these arrays
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

color = 'gold'
lw = 2

data = []

p1 = go.Scatter(x=x_plot, y=f(x_plot), 
                mode='lines',
                line=dict(color='cornflowerblue', width=lw),
                name="ground truth")

p2 = go.Scatter(x=x, y=y,
                mode='markers',
                marker=dict(color='navy',
                            line=dict(color='black', width=1)),
                name="training points")
data.append(p1)
data.append(p2)

degree = 5

model = make_pipeline(PolynomialFeatures(degree), Ridge())
model.fit(X, y)
y_plot = model.predict(X_plot)
p3 = go.Scatter(x=x_plot, y=y_plot, 
                mode='lines',
                line=dict(color=color, width=lw),
                name="degree %d" % degree)
data.append(p3)

layout = go.Layout(xaxis=dict(zeroline=False),
                   yaxis=dict(zeroline=False))
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename = 'polynomial interpolation')