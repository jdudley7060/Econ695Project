#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import DataFrame, Series
from sklearn import linear_model
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import statsmodels.api as sm

def sexy_graph(x_variable, y_variable, data_frame, Graph_Title): #graphing function
    
    #import the neccesary modules
    
 

    style.use('ggplot') #use ggplot for graph creation
    plt.rcParams['figure.figsize'] = (20,10) #set the parmeters for the size of the graph
    sb.scatterplot(x_variable, y_variable, data = data_frame, c=data_frame.State.astype("category").cat.codes, s = 200, linewidth = 3)
    #graph the variables ussing seabon, and set the color of to be the state
    plt.title(Graph_Title, color = 'black', fontsize = 18)# add a title to the graph
    
    def label_point(x,y, val, ax): #function for labeling each point with the state
        a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1) # concat each varaible to a dictionary
    
        for i, point in a.iterrows(): # loop through each dictionary and assign a value to each state
            ax.text(point['x']+.02, point['y'], str(point['val']))  

    label_point(data_frame.Acreage, data_frame.Industrial_share, data_frame.State, plt.gca()) #run the function on the current graph axes
    
    try:
        plt.savefig(item+".png") # save it as a scatter plot
    except:
        plt.savefig(item.replace("/","_")+".png")

    return plt.show() #return the graph


# In[ ]:


df = pd.read_csv("crop_aqi_co2_combined.csv") #read in the excel file
df


# In[ ]:


#sum of the total number of data points that we are working with
sum(df["Count"])



# In[ ]:


corn_df = df[df["Category"] == " Corn"] #create a corn df for each state

X = corn_df[['Average of Median AQI', 'Commercial', 'Electric Power', 'Residential', "Industrial", "Transportation"]]
#set independent variables as Median AQI, commerical, electric, residential, industrial, and transportation emissions
y= corn_df['Acreage']
#set dependent variable as
regr = linear_model.LinearRegression() #run a linear regression
regr.fit(X,y) #fit the x and y variables to the regression

regr.coef_
#find the summary statistics for the fitted regression 
lr = sm.OLS(y,X).fit()
predict = lr.predict()
(lr.summary())


# In[ ]:


corn_df = df[df["Category"] == " Corn"]

X = corn_df[['Average of Median AQI', 'Commercial', 'Electric Power', 'Residential', "Industrial", "Transportation"]]
#set independent variables as Median AQI, commerical, electric, residential, industrial, and transportation emissions
y= corn_df['Acreage']

regr = linear_model.LinearRegression()
regr.fit(X,y)#fit the x and y variables to the regression

regr.coef_
#find the summary statistics for the fitted regression 
lr = sm.OLS(y,X).fit()
predict = lr.predict()
(lr.summary())


# In[ ]:


soybeans_df = df[df["Category"] == " Soybeans"]

X = soybeans_df[['Average of Median AQI', 'Commercial', 'Electric Power', 'Residential', "Industrial", "Transportation"]]
#set independent variables as Median AQI, commerical, electric, residential, industrial, and transportation emissions
y= soybeans_df['Acreage']

regr = linear_model.LinearRegression()
regr.fit(X,y)#fit the x and y variables to the regression

regr.coef_
#find the summary statistics for the fitted regression 
lr = sm.OLS(y,X).fit()
predict = lr.predict()
(lr.summary())


# In[ ]:

barley_df = df[df["Category"] == " Barley"] #create a data frame for barley for each state

X = barley_df[['Average of Median AQI', 'Commercial', 'Electric Power', 'Residential', "Industrial", "Transportation"]]
#set independent variables as Median AQI, commerical, electric, residential, industrial, and transportation emissions
y= barley_df['Acreage']

regr = linear_model.LinearRegression()
regr.fit(X,y)#fit the x and y variables to the regression

regr.coef_ 
#find the summary statistics for the fitted regression 
lr = sm.OLS(y,X).fit()
predict = lr.predict()
(lr.summary())


# In[ ]:


oats_df = df[df["Category"] == " Oats"]

X = oats_df[['Average of Median AQI', 'Commercial', 'Electric Power', 'Residential', "Industrial", "Transportation"]]
#set independent variables as Median AQI, commerical, electric, residential, industrial, and transportation emissions
y= oats_df['Acreage']
#set dependent variable as acreage of oats
regr = linear_model.LinearRegression() #run a linear regression 
regr.fit(X,y) #fit the x and y variables to the regression

regr.coef_ 


#find the summary statistics for the fitted regression 
lr = sm.OLS(y,X).fit()
predict = lr.predict()
(lr.summary())


# In[ ]:


var= (['Acreage', 'Average of Median AQI', 'Commercial', 'Electric Power', 'Residential', "Industrial", "Transportation" ])
g_var = corn_df[var]
g=sb.pairplot(g_var) #run a pair plot to see all the relationships between the varaibles
g


# In[ ]:


#make scatter plot with the statiscally signifigant varaibles 

#corn- transportation
#Soybeans -Electric Power
#soybeans - Transportation
#Oats - Industrial


# In[ ]:


style.use('ggplot') #use ggplot for graph creation
plt.rcParams['figure.figsize'] = (20,10) #set the parmeters for the size of the graph
sb.scatterplot("Transportation", "Acreage", data = corn_df, c=corn_df.State.astype("category").cat.codes, s = 200, linewidth = 3)
#graph the variables using seaborn, and set the color of to be the state
plt.title("Relationship between Corn Acreage and Transportation Emissions per State", color = 'black', fontsize = 18)# add a title to the graph

plt.savefig("transportion.png") # save it as a scatter plot


(plt.show()) #return the graph


# In[ ]:


style.use('ggplot') #use ggplot for graph creation
plt.rcParams['figure.figsize'] = (20,10) #set the parmeters for the size of the graph
sb.scatterplot("Electric Power", "Acreage", data = soybeans_df, c=soybeans_df.State.astype("category").cat.codes, s = 200, linewidth = 3)
#graph the variables using seaborn, and set the color of to be the state
plt.title("Relationship between Soybean Acreage and Electric Power Emissions per State", color = 'black', fontsize = 18)# add a title to the graph

plt.savefig("transportion.png") # save it as a scatter plot


(plt.show()) #return the graph


# In[ ]:


style.use('ggplot') #use ggplot for graph creation
plt.rcParams['figure.figsize'] = (20,10) #set the parmeters for the size of the graph
sb.scatterplot("Transportation", "Acreage", data = soybeans_df, c=soybeans_df.State.astype("category").cat.codes, s = 200, linewidth = 3)
#graph the variables using seaborn, and set the color of to be the state
plt.title("Relationship between Soybean Acreage and Transportation Emissions per State", color = 'black', fontsize = 18)# add a title to the graph

plt.savefig("transportion.png") # save it as a scatter plot


(plt.show()) #return the graph


# In[ ]:


style.use('ggplot') #use ggplot for graph creation
plt.rcParams['figure.figsize'] = (20,10) #set the parmeters for the size of the graph
sb.scatterplot("Industrial", "Acreage", data = oats_df, c=oats_df.State.astype("category").cat.codes, s = 200, linewidth = 3)
#graph the variables using seaborn, and set the color of to be the state
plt.title("Relationship between Oat Acreage and Industrial Emissions per State", color = 'black', fontsize = 18)# add a title to the graph

plt.savefig("transportion.png") # save it as a scatter plot


(plt.show()) #return the graph


# In[ ]: