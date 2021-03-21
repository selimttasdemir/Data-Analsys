# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:35:49 2021

seaborn lib. start...

@author: Selim Tasdemir
"""

import seaborn as sns, matplotlib.pyplot as plt

yas = [30,26,45,26,25,20,40,33,28,30]
kilo = [80,75,70,78,90,66,75,100,82,90]

sns.scatterplot(x=yas,y=kilo)
plt.show()

#%%
cinsiyet = ["erkek","kadın","erkek","kadın","kadın","kadın",
            "erkek","kadın","erkek","kadın","erkek","kadın",
            "kadın","kadın","erkek","kadın","erkek","kadın",
            "erkek","kadın","kadın","kadın","erkek","kadın"]

sns.countplot(x=cinsiyet)
plt.show()
