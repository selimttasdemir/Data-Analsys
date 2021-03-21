# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:31:55 2021

data analysis

@author: Selim Tasdemir
"""

import matplotlib.pyplot as plt , pandas as pd

data = pd.read_csv(r"C:\Users\casper\Desktop\dataset\iris.csv")

info = data.info
ilkBes = data.head()
sonBes = data.tail()
