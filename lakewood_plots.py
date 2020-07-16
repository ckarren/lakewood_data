#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:37:00 2020

@author: cade
"""
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('dataset_224.csv', index_col=0)   #individual csv file corresponding to single day of data
df = pd.DataFrame(data)


df2 = df.copy() #make copy of dataframe
df2['average'] = df.mean(numeric_only=True, axis=1) #create column of average use
df2['total'] = df.sum(axis=1)   #create column of cumulative use


x1 = df2['average']
x2 = df2['total']

fig, ax1 = plt.subplots()   
ax1.plot(range(len(df2)),x2)    
ax1.set(xlabel="time (hours)", ylabel="volume (cf)")


plt.show()