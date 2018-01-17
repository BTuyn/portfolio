# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:15:15 2017

@author: Bob
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import seaborn as sns

# makes seaborn default plotter
sns.set()
# read csv file
df = pd.read_csv('C:\\Users\\Bob\\Desktop\\python testfolder\\o2o.csv')

mu = 536.319002
variance = 216.683697
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x,mlab.normpdf(x, mu, sigma))
# title for x-axis
plt.xlabel('CO2 in ppm')
# title for y-axis
plt.ylabel('Probability')
# show plot
plt.show()

def ecdf(df):
    """Compute ECDF for a one-dimensional array of measurements."""
    
    # Number of data points: n
    n=len(df)

    # x-data for the ECDF: x
    x=np.sort(df)
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

# Compute ECDF for data: x_vers, y_vers
x,y = ecdf(df)

# Generate plot
_ = plt.plot(x, y, marker='.', linestyle='none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
