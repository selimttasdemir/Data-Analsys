# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:35:53 2021

data analysis

@author: Selim Tasdemir
"""

import matplotlib.pyplot as plt , pandas as pd

data = pd.read_csv(r"C:\Users\casper\Desktop\dataset\ev_satislari.csv")

ilkBes = data.head()
sonBes = data.tail()

dataHead_100 = data.head(100)

plt.figure(figsize=(15,6))

plt.plot(dataHead_100.datesold,dataHead_100.price,
         color="blue",
         linestyle="-",
         linewidth=3,
         marker="*",
         markersize=10,
         markerfacecolor="red")

plt.plot(dataHead_100.datesold,dataHead_100.bedrooms,
         color="green",
         linestyle="-",
         linewidth=3,
         marker="*",
         markersize=10,
         markerfacecolor="black")

plt.xticks(rotation=90)

plt.title("Yıllara Göre Ev Fiyatları")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")

grafik = plt.show()



































