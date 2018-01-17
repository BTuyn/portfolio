# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:51:27 2017

@author: Bob
"""
# outlier detectie code door te clusteren, er wordt gebruik gemaakt van een trainingsset, 
# validatieset en de "echte" dataset waar naar gekeken wordt.

# imported required libraries and defining functions for reading data,
# mean normalizing features and estimating gaussian distribution.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from numpy import genfromtxt
from scipy.stats import multivariate_normal
from sklearn.metrics import f1_score

def read_dataset(filePath,delimiter=';'):
    return genfromtxt(filePath, delimiter=delimiter)

def feature_normalize(dataset):
    mu = np.mean(dataset,axis=0)
    sigma = np.std(dataset,axis=0)
    return (dataset - mu)/sigma

def estimateGaussian(dataset):
    mu = np.mean(dataset, axis=0)
    sigma = np.cov(dataset.T)
    return mu, sigma
    
def multivariateGaussian(dataset,mu,sigma):
    p = multivariate_normal(mean=mu, cov=sigma)
    return p.pdf(dataset)

# Define a function to find the optimal value for threshold (epsilon)
# that can be used to differentiate between normal and anomalous data points. 
def selectThresholdByCV(probs,gt):
    best_epsilon = 0
    best_f1 = 0
    f = 0
    stepsize = (max(probs) - min(probs)) / 1000;
    epsilons = np.arange(min(probs),max(probs),stepsize)
    for epsilon in np.nditer(epsilons):
        predictions = (probs < epsilon)
        f = f1_score(gt, predictions, average = "binary")
        if f > best_f1:
            best_f1 = f
            best_epsilon = epsilon
    return best_f1, best_epsilon

# tr_data=trainingset, cv_data=validatieset, gt_data= DE echte dataset
tr_data = pd.read_csv('C:\\Users\\Bob\\Desktop\\python testfolder\\D2008jul2013jul2014hour.csv') 
cv_data = pd.read_csv('C:\\Users\\Bob\\Desktop\\python testfolder\\D2008jul2014jul2015hour.csv') 
gt_data = pd.read_csv('C:\\Users\\Bob\\Desktop\\python testfolder\\D2008jul2015jul2016hour.csv')

# 0 = latency, 1= troughput
n_training_samples = tr_data.shape[0]
n_dim = tr_data.shape[1]

print(n_training_samples)
print(n_dim)
plt.figure()
plt.xlabel("Latency (ms)") 
plt.ylabel("Throughput (mb/s)") 
plt.plot(tr_data.iloc[:,0],tr_data.iloc[:,1],"bx")

plt.show()

mu, sigma = estimateGaussian(tr_data)
p = multivariateGaussian(tr_data,mu,sigma)

p_cv = multivariateGaussian(cv_data,mu,sigma)
fscore, ep = selectThresholdByCV(p_cv,gt_data)

outliers = np.where(p < ep)

plt.figure() 
plt.xlabel("Latency (ms)") 
plt.ylabel("Throughput (mb/s)") 
plt.plot(tr_data.iloc[:,0],tr_data.iloc[:,1],"bx")
plt.plot(tr_data.iloc[outliers[0],0],tr_data.iloc[outliers[0],1],"ro") 
plt.show()


# Wat nog moet gebeuren: outliers in eigen csv met bijbehorende x en y waardes
#vervolgens zouden meerdere dimensies kunnen worden toegevoegd of verschillende lijsten worden gemaakt
#die verband tussen twee variabelen laat zien



