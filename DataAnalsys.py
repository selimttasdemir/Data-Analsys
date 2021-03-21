# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:31:15 2021

data analysis

@author: Selim TASDEMIR
"""
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

path=r"C:\Users\casper\Desktop\dataset\temps.csv"

data = pd.read_csv(path)

print(data.head())
print(data.dtypes)
print(data.info())

dagilimDegerleri = data.describe()

print(data.describe())
print(data.shape)

print(data.isnull().sum())










