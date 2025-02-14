# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:09:10 2025

@author: adp04
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('alzheimers_prediction_dataset.csv')

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

'''
df['Country']=df['Country'].astype('int64')
df['Age']=df['Age'].astype('int64')
df['Gender']=df['Gender'].astype('int64')
df['Education Level']=df['Education Level'].astype('int64')
df['BMI']=df['BMI'].astype('int64')
df['Physical Activity Level']=df['Physical Activity Level'].astype('int64')
df['Smoking Status']=df['Smoking Status'].astype('int64')
df['Alcohol Consumption']=df['Alcohol Consumption'].astype('int64')
df['Diabetes']=df['Diabetes'].astype('int64')
df['Hypertension']=df['Hypertension'].astype('int64')
df['Cholesterol Level']=df['Cholesterol Level'].astype('int64')
df['Family History of Alzheimer\'s']=df['Family History of Alzheimer\'s'].astype('int64')
df['Cognitive Test Score']=df['Cognitive Test Score'].astype('int64')
df['Depression Level']=df['Depression Level'].astype('int64')
df['Sleep Quality']=df['Sleep Quality'].astype('int64')
df['Dietary Habits']=df['Dietary Habits'].astype('int64')
df['Air Pollution Exposure']=df['Air Pollution Exposure'].astype('int64')
df['Employment Status']=df['Employment Status'].astype('int64')
df['Marital Status']=df['Marital Status'].astype('int64')
df['Generic Risk Factor (APOE-ε4 allele)']=df['Genetic Risk Factor (APOE-ε4 allele)'].astype('int64')
df['Social Engagement Level']=df['Social Engagement Level'].astype('int64')
df['Income Level']=df['Income Level'].astype('int64')
df['Stress Levels']=df['Stress Levels'].astype('int64')
df['Urban vs Rural Living']=df['Urban vs Rural Living'].astype('int64')
df['Alzheimer\'s Diagnosis']=df['Alzheimer\'s Diagnosis'].astype('int64')
'''

print(df.describe().T) #Prints summary statistics of df
print(df.isnull().sum()) #Sums total amount of empty items
print(df.duplicated().sum()) #Sums total amount of duplicates
df.drop_duplicates(inplace=True) #Drops duplicates
print(df.shape) #Same shape, as no duplicates were found or dropped



for i in df['Gender']:
    if df[i]['Gender'] == "Male":
        df[i]['Gender'] = 0 #Males classified as 0
    elif df[i]['Gender'] == "Female":
        df[i]['Gender'] = 1 #Females classified as 1
    else:
        print(df[i]['Gender'])
        
        
print(df['Gender'])
        
        
        
        
        
        
        
        
        
        