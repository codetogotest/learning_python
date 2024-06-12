# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 01:25:33 2024

@author: Ala
"""

import pandas as pd

import matplotlib.pyplot as plt   



url = 'https://data.cip.gov.tw/API/v1/dump/datastore/A53000000A-112046-003'



df = pd.read_csv(url)



for i in range(4,16):

    if df.iloc[:,i].dtype == 'object':

        df.iloc[:,i] = df.iloc[:,i].str.replace(',','')   #字串的轉換

        df.iloc[:,i] = pd.to_numeric(df.iloc[:,i],errors='coerce') #無法轉成數字的就替換成NaN

        

df = df.fillna(0)   #用 0 替換所有 NaN 元素        

  

      

df1=df.['民國年'].groupby('民國年').sum()   # 第2~最後的欄位以'年度'為單位加總



s=[]   #列表,df1每年的所有欄位總和

for i in range(len(df1)):

    s.append(df1.iloc[i,:].sum())

    

plt.figure(figsize=(15,10), dpi=300)

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'





plt.subplot(2,2,1)

plt.bar(df1.index, s)

for i in range(len(df1)):   #資料標籤

    plt.text(df1.index[i], s[i]-120000, int(s[i]), ha='center', color='w' ,fontsize=12)

    

plt.xticks(df1.index, fontsize=10)   # X軸只呈現df1.index

plt.title('年度的參觀總人次',fontsize=16)





plt.subplot(2,2,2)

m = df1.sum()   #以欄來加總

plt.plot(df1.columns, m, color='#ff8000')

for i in range(len(m)):

    plt.text(m.index[i], m.iloc[i]+2000, int(m.iloc[i]), ha='center', color='k', fontsize=8)



plt.xticks(m.index, fontsize=10)   

plt.grid()

plt.title('各個月份的總參觀人次',fontsize=16)





plt.subplot(2,2,3)

df['縣市']=df['場館'].str[:3].replace('台灣原','花蓮縣')   #新增欄位

c=df.iloc[:,4:].groupby('縣市').sum().T

cs=c.sum()

plt.bar(cs.index, cs, color='g')

plt.xticks(cs.index, fontsize=7)



for i in range(len(cs)):

    if cs.iloc[i]<500000:

        plt.text(i, cs.iloc[i]+20000, int(cs.iloc[i]), ha='center', rotation=90, color='k', fontsize=8)



    else:

        plt.text(i, cs.iloc[i]-150000, int(cs.iloc[i]), ha='center', rotation=90, color='w', fontsize=8)



plt.title('各縣市的總參觀人次',fontsize=16)





plt.subplot(2,2,4)

c1=cs['新北市']+cs['臺北市']+cs['桃園市']+cs['臺中市']+cs['臺南市']+cs['高雄市']

c2=['六都', '非六都']

plt.pie([c1, cs.sum()-c1], autopct='%2.1f%%', labels=c2)

plt.title('六都與非六都的參觀總人次比例', fontsize=16)





plt.savefig('文物館統計.png')