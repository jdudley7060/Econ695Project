#!/usr/bin/env python
# coding: utf-8

# In[31]:


import os
import pandas as pd

### combine all state files into one dataset ###

# set working directory for finding files
os.chdir('/Users/jacobdudley/Desktop/test/CropScape')

# grab all files in CropScape folder
cwd = os.path.abspath('') 
files = os.listdir(cwd)

# make dataframe with all csv files
df_crop = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        df_crop = df_crop.append(pd.read_csv(file)) 

# clean up columns
df_crop = df_crop.drop(columns=['Value'])
df_crop = df_crop.rename(columns={'  Acreage':'Acreage', ' Category':'Category', ' Count':'Count'})


# In[32]:


### merge our datasets ###

# set working directory for finding files
os.chdir('/Users/jacobdudley/Desktop/test')

# pull in other datasets to combine
df_aqi = pd.read_csv('annual_aqi_by_county_2020.csv')
df_co2 = pd.read_csv('C02_data.csv', header=2)

# drop columns not needed
df_co2 = df_co2.drop(columns=['Commercial_share','Electric_share','Residential_share','Industrial_share','Transportation_share'])

# merge datasets into one
df1 = pd.merge(df_crop, df_aqi, how='inner', left_on='State', right_on='State')
df2 = pd.merge(df1, df_co2, how='inner', left_on='State', right_on='State')

# save combined dataset to excel file
df2.to_csv("crop_aqi_co2_combined.csv", index = False)