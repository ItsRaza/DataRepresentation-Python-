import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df=pd.read_csv('OLX_Car_Data_CSV.csv', delimiter=',', encoding = "ISO-8859-1")
#print(df.columns)
#print(df.dtypes)
#print(df.describe())
#print(df.describe(include="all"))
#print(df.info)
missing=df.isnull()
#print(missing.head(10))

#replacing null Kms and null years with avgKMs and avgYears
'''
avg_KmDriven=df["KMs Driven"].astype("float").mean() 
df["KMs Driven"].replace(np.nan,avg_KmDriven,inplace=True)
avg_Year=df["Year"].astype("float").mean()
df["Year"].replace(np.nan,avg_Year,inplace=True)
print(df.describe())

'''
#dropping the null values
df.dropna(axis=0,inplace=True)
df.reset_index(drop=True,inplace=True)
df.replace("",np.nan,inplace=True)
#print(df.head(10))

'''Data Visualization'''
#print(df["Fuel"].value_counts())


#Fuel VS Price Bar Graph

'''
var = df.groupby('Fuel').Price.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Fuel')
ax1.set_ylabel('Price')
ax1.set_title("Fuel Vs Price")
var.plot(kind='bar')
fig.show()
input("press ENTER")
'''
#Condition VS Price Graph

'''
#print(df["Condition"].value_counts())
var = df.groupby('Condition').Price.sum() 
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Condition Of Car')
ax1.set_ylabel('Increase In price')
ax1.set_title("Condition Vs Price")
var.plot(kind='bar')
fig.show()
input()
'''
#Brand VS price

'''
#print(df["Brand"].value_counts())
var = df.groupby('Brand').Price.sum() 
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Brands')
ax1.set_ylabel('Increase In price')
ax1.set_title("Brand Vs Price")
var.plot(kind='bar')
fig.show()
input()
'''
#Model VS Price

'''
#print(df["Model"].value_counts())
var = df.groupby('Model').Price.sum() 
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Model')
ax1.set_ylabel('Increase In price')
ax1.set_title("Model Vs Price")
var.plot(kind='line')
fig.show()
input()
'''
#Year VS Price

'''
var = df.groupby('Year').Price.sum() 
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Increase In price')
ax1.set_title("Year Vs Price")
var.plot(kind='line')
fig.show()
input()
'''
#Year VS condition

var = df.groupby('Condition').Year.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Condition')
ax1.set_ylabel('Year')
ax1.set_title("Year Vs Condition")
var.plot(kind='line')
fig.show()
input()