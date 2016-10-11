# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:31:06 2016

@author: lintinggong
"""

#Overall Comment: Try to organize your assignment in clear format. Express the problems your are trying to solve and then
#                 give detail explanations for the logic and your code.
import pandas as pd 
#we need to import panda first in order to use all the functions from the 
#panda package 
data=pd.read_table('/Users/lintinggong/Downloads/iris.data-2.txt',header=0,sep = ',')
#we need to read the table from our computer first. Use the first row 0 as the 
#header and use ',' to separate the columns. 
print(data)# display the data 
data.head(n=10)
#use panda function to read the first 10 rows 
data.tail(n=10)
#use panda function to read the last 10 rows 
data.describe().transpose()
#use the simple function to get the simple statistis (count, mean, STD, Min, 25%,50%,
#75%, MAX). 
data.hist()
#print the histogram for each of the numeric columns 
dataset=pd.read_table('/Users/lintinggong/Downloads/iris.data-2.txt',header=0,sep = ',')
#we changed the name of the class colum to be class0, because python recongnizes
#class as a function. 
dataset.class0.value_counts().plot(kind='bar')
#Recall the dataset , and then specifically the column
#class0 is that we want to use to make the bar chart. 
#we count the number of times each item appears in that column from 
#the value_counts() command. lastly, we use plot to create the graph
# which we specify to be a bar graph.
