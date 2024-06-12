# -*- coding: utf-8 -*-

# homework4 (107 -112年度)
# 政府公開資料網址 https://data.gov.tw/dataset/164265

import pandas as pd

import matplotlib.pyplot as plt

# 原住民族地方文物館參觀人次統計 CSV
url = "https://data.cip.gov.tw/API/v1/dump/datastore/A53000000A-112046-003"

df = pd.read_csv(url)

# 清理資料
df = df.iloc[:,[2,4,6,7]]
df.columns = ["民國年","縣市","月份","人次"]
for i in range(2,3):
    df.iloc[:,i] = pd.to_numeric(df.iloc[:,i] , errors="coerce")

df1 = df.groupby('民國年')['人次'].sum()
df2 = df.groupby('月份')['人次'].sum()
df3 = df.groupby('縣市')['人次'].sum()

city_six_list = ['臺北市','新北市','桃園市','臺中市','臺南市','高雄市']
city_six = df3[city_six_list].sum()
other_city = df3.sum()-city_six
df4 = [city_six,other_city]

plt.figure(figsize=(20,15),dpi=200)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

# 請繪製第一張長條圖，呈現三個年度的參觀總人次
plt.subplot(2,2,1)
plt.title('年度的參觀總人次',fontsize=20) 
plt.xticks(df1.index)
plt.bar(list(df1.index),list(df1))
for i in df1.index:
    plt.text(i,df1[i]-20000,int(df1[i]),ha='center',va='top',color='w')

# 請繪製第二張折線圖，呈現各個月份的總參觀人次
plt.subplot(2,2,2) 
plt.title('各個月份的總參觀人次',fontsize=20)
plt.grid()
plt.xticks(range(1, 13), ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'])
plt.plot(df2,color='orange')
for i in df2.index:
    plt.text(i,df2[i],int(df2[i]),ha='center',va='bottom')

# 請繪製第三張長條圖，繪製各縣市的總參觀人次
plt.subplot(2,2,3)
plt.title('各縣市的總參觀人次',fontsize=20)
plt.bar(list(df3.index),list(df3),color='green')
for i in df3.index:
    if df3[i]<200000:
        plt.text(i,df3[i]+15000,int(df3[i]),ha='center',va='bottom',fontsize=10,rotation=90)
    else:
        plt.text(i,df3[i]-15000,int(df3[i]),ha='center',va='top',fontsize=10,rotation=90,color='w')


# 請繪製第四張圓餅圖，呈現六都與非六都的參觀總人次比例
plt.subplot(2,2,4)
plt.title('六都與非六都的總參觀人數比',fontsize=20)
plt.pie(df4,labels=['六都','非六都'], autopct='%.1f%%')
plt.axis('equal')

plt.savefig('homework4.png')
