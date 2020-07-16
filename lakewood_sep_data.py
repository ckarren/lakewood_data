#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:25:26 2020

@author: cade
"""
import pandas as pd 
import os 


#the csv only had data every-other line. to skip every-other line when importing csv
def logic(index):
    if index % 2 == 0:
       return False
    return True

data = pd.read_csv('consmption_2019_hourly.csv', skiprows= lambda x: logic(x), index_col=[0])   
df = pd.DataFrame(data)
df.index =  pd.to_datetime(df.index, infer_datetime_format=True)    #convert index to datetime type

#create list of data using groupby method 
result = [group[1] for group in df.groupby(df.index.date)]  

#path to save csvs 
output_path = '/home/cade/Documents/Research/ABM/dynamic_pricing/py_files+data/'

#export to csv
for index, dataset in enumerate(result):        
    filepath = os.path.join(output_path, 'dataset_'+str(index)+'c.csv')
    dataset.to_csv(filepath)
