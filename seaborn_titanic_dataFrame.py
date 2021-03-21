# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:44:04 2021

seaborn example

@author: Selim Tasdemir
"""
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

path = r"C:\Users\casper\Desktop\dataset\train.csv"

df = pd.read_csv(path)

ilkOnVeri = df.head(10)
sonOnVeri = df.tail(10)

df.info()
print("Değişken türleri : \n",df.dtypes)

print("Toplam Veri: ",df.size)

print("Satır sayısı ve değişken sayısı: ",df.shape)

mat = df.describe().T
print(mat) # toplam medyan standart sapma vb bilgilerin alınması

print("***********Boş Değerlerin Toplamı:\n",df.isnull().sum())

df = df.dropna()

print("**********Boş Değerlerin Toplamı:\n",df.isnull().sum())

#%%        ###### SEABORN İLE VERİ GORSELLEŞTİRME  ######

a = sns.barplot(x="Sex",y="Survived", hue="Sex", data = df);
a.set_title("Cinsiyete gore hayatta kalma dagılımı")

#%%   ###############   PAIR PLOT KULLANIMI ###############

sns.pairplot(data=df);

#%%    ###############   HEATMAP (CORRELATION MATRIX) KULLANIMI ###############

corr = df.corr()
plt.figure(figsize=(12,12))
a = sns.heatmap(corr, vmax=.99, linewidths=0.5, square=True,annot=True, linecolor='r')

#%%             COUNTPLOT (Kategorik değişkenlerin sınıflandırılmasında kullanılır !!!!)

sns.countplot(x=df.Sex)
plt.show()

#%% CATPLOT (kATEGORİK VERİLER İÇİN KULLNAILIR)

sns.catplot(x = "Pclass", kind="count", hue="Sex",palette="Set1",data=df)

#%% boxPLOT (Outlier degerine bakarak yorum yapmamamızı saglar. )

sns.catplot(x="Sex",y="Fare", hue="Sex", data = df, kind="box",sym="")

#%% SCATTER PLOT (İKİ SAYISAL DEĞİŞKEN ARASINDAKI ILIŞKIYI GOSTERIR. )

sns.scatterplot(x="Fare", y="Age", data=df, hue="Sex")
