import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits
#from mpl_toolkits.mplot3D import axes3d as ax
import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from matplotlib import interactive

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = pd.read_csv("data_two_variables.csv")
X1 = data.iloc[:,0]
X2 = data.iloc[:,1]
Y = data.iloc[:,2]

L = 0.001
epochs = 10000
num = float(len(X1))

m1, m2, m3 = 0.0,0.0,0.0

for i in range(epochs):
	Y_pred = m1 * X1 + m2 * X2 + m3
	D_m1 = (-2/num) * sum(X1 * (Y - Y_pred))
	D_m2 = (-2/num) * sum(X2 * (Y - Y_pred))
	D_m3 = (-2/num) * sum(Y - Y_pred)
	m1 = m1 - L * D_m1
	m2 = m2 - L * D_m2
	m3 = m3 - L * D_m3

Y_pred = m1 * X1 + m2 * X2 + m3
ax.scatter(X1, X2, Y, c='b')
ax.scatter(X1, X2, Y_pred, c='r')
fig.show()

#test = input()
plt.show()