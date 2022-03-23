#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pyodbc
import sys
import cmd
import numpy as np
from openpyxl import load_workbook
from fuzzywuzzy import fuzz

filepath1 = 'ioCurrents.csv'
df = (pd.read_csv(filepath1)
       .rename(columns={
               "ï»¿sensor" : "sensor",
               "etc…" : "etc"
                       }
              )
       .rename(columns=lambda x : x.replace('Unnamed: ','Col_')
                                   .replace(' ','_')
                                   .strip())
     )
	 

df.head(10)

df.dtypes

def sensorsearch (sensors, df):

    return ["select * from table.name where sensor = {} and y_high = {}"
                .format(v,
                        df.loc[df['sensor'] == v]['y_high'].values[0])
                for v in sensors]

sensorsearch (sensors = (1,2,4,6),df = df)



[OUT]


['select * from table.name where sensor = 1 and y_high = nan',
 'select * from table.name where sensor = 2 and y_high = 30.0',
 'select * from table.name where sensor = 4 and y_high = 30.0',
 'select * from table.name where sensor = 6 and y_high = nan']

