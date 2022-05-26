# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:32:07 2021

@author: Aishwarya
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
train_data=pd.read_csv('train.csv',nrows=10_000_000)
train_data.shape()
train_data.info()
test_data=pd.read_csv('test.csv')
test_data.head()
test_data.info()
train_data.isna().sum()

train_data['Difference_longitude']=np.abs(np.asarray(train_data['pickup_longitude']-train_data['dropoff_longitude']))
train_data['Difference_latitude']=np.abs(np.asarray(train_data['pickup_latitude']-train_data['dropoff_latitude']))


test_data['Difference_longitude']=np.abs(np.asarray(test_data['pickup_longitude']-test_data['dropoff_longitude']))
test_data['Difference_latitude']=np.abs(np.asarray(test_data['pickup_latitude']-test_data['dropoff_latitude']))

print(f'Before Dropping null values: {len(train_data)}')
train_data.dropna(inplace=True)
print(f'After Dropping null values: {len(train_data)}')

plot = train_data[:2000].plot.scatter('Difference_longitude', 'Difference_latitude')

train_data=train_data[(train_data['Difference_longitude']<5.0)&(train_data['Difference_latitude']<5.0)]

ls1=list(train_data['pickup_datetime'])
for i in range(len(ls1)):
    ls1[i]=ls1[i][11:-7:]
train_data['pickuptime']=ls1    



ls1=list(test_data['pickup_datetime'])
for i in range(len(ls1)):
    ls1[i]=ls1[i][11:-7:]
test_data['pickuptime']=ls1  

train_data.head()

ls1=list(train_data['pickup_datetime'])
for i in range(len(ls1)):
    ls1[i]=ls1[i][:-4:]
    ls1[i]=pd.Timestamp(ls1[i])
    ls1[i]=ls1[i].weekday()
train_data['Weekday']=ls1


ls1=list(test_data['pickup_datetime'])
for i in range(len(ls1)):
    ls1[i]=ls1[i][:-4:]
    ls1[i]=pd.Timestamp(ls1[i])
    ls1[i]=ls1[i].weekday()
test_data['Weekday']=ls1
