# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 02:21:45 2024

@author: Ala
"""

import matplotlib.pyplot as plt
import pandas as pd
url = 'https://data.cip.gov.tw/API/v1/dump/datastore/A53000000A-112046-003'
df=pd.read_csv(url)


#####資料處理######

df['場館']=df['場館'].str.replace('台灣原','花蓮縣')
df['縣市']=df['場館'].str[:3]
df['年度']=df['民國年'].str[:3]
#df = df.drop('縣市別代碼', axis=1)

for i in range(4,5):  ##有幾欄不是數字
    df.iloc[:,i]=pd.to_numeric(df.iloc[:,i], errors="coerce")
    
#df=df.iloc[:,1:] ##刪除多於行列
#for i in range(4,5):  ##有幾欄不是數字
#    df.iloc[:,i]=pd.to_numeric(df.iloc[:,i], errors="coerce")


#年度參觀總人次

df1= df.groupby('年度').sum()
df1= df1.sum(axis=1)  #每年


#各月分總參觀人數

df2=df.sum(axis=0) #每月
df2=df2[4:5] #去除非數字欄位


#各縣市總參觀人數

df3=df.groupby('縣市').sum().sum(axis=1)


#六都與非六都 總參觀人數

list1=['臺北市','新北市','桃園市','臺中市','臺南市','高雄市']
sixCapital=df3[list1].sum()
other=df3.sum()-sixCapital
df4=[sixCapital,other]
mark=['六都','非六都']


#####作圖#####

        

plt.figure(figsize=(15,10),dpi=200)
plt.rcParams['font.sans-serif']='Microsoft JhengHei'


#左上長條圖

plt.subplot(2,2,1) 
plt.xticks([107,108,109,110])
plt.title('年度總參觀人次',fontsize=14)
plt.xlabel('民國年度')
plt.ylabel('觀光人次')
for i in df1.index:
    plt.text(i,df1[i]-20000,int(df1[i]),ha='center',va='top',color='w')
plt.bar(list(df1.index),list(df1))


#右上折線圖

plt.subplot(2,2,2) 
plt.title('各月份總參觀人次',fontsize=14)
plt.grid()
plt.ylim(50000,450000)
for i in df2.index:
    plt.text(i,df2[i],int(df2[i]),ha='center',va='bottom')
plt.plot(df2,color='orange')


#左下長條圖

plt.subplot(2,2,3) 
plt.title('各縣市總參觀人次',fontsize=14)
plt.xticks(fontsize=6)
for i in df3.index:
    if df3[i]<200000:
        plt.text(i,df3[i]+10000,int(df3[i]),ha='center',va='bottom',fontsize=8,rotation=90)
    else:
        plt.text(i,df3[i]-10000,int(df3[i]),ha='center',va='top',fontsize=8,rotation=90,color='w')
plt.bar(list(df3.index),list(df3),color='green')


#右下圓餅圖

plt.subplot(2,2,4) 
plt.title('六都與非六都總參觀人數比',fontsize=14)
plt.pie(df4,labels=mark,autopct='%.1f%%')
plt.savefig('homework4')