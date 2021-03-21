# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:59:13 2021

data analysis

@author: Selim Tasdemir
"""

import pandas as pd, numpy as np

path = r"C:\Users\casper\Desktop\dataset\titanic_dataset.csv"

df = pd.read_csv(path)

print(df.shape)

ilkOnVeri = df.head(10)
sonOnVeri = df.tail(10)

df.info()

bosDeger = df.isnull().sum().sort_values(ascending = False)

bosDeger1 = df['Embarked'].value_counts()

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace = True)

medyanDeger = df['Age'].median()
ortalamaDeger = df['Age'].mean()

df['Age'].fillna(df['Age'].mean(), inplace = True)

df.drop(['Name' , 'PassengerId' , 'Ticket' , 'Cabin'], axis = 1, inplace = True)

bosDeger = df.isnull().sum().sort_values(ascending = False)


















