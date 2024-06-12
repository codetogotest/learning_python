# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:38:28 2024

@author: Ala
"""

# Homework3

import pandas as pd

# 讀取 CSV 文件
df = pd.read_csv('3-3read.csv', encoding='utf-8')

# 1. 印出以遞減方式居住縣市的病例人數
print(df.groupby('居住縣市')['居住縣市'].count().sort_values(ascending = False))

# 2. 印出以遞減方式感染國家病例人數最多的五個國家
print(df.groupby('感染國家')['感染國家'].count().sort_values(ascending = False).head(5))

# 3. 印出台北市各區的病例人數
print(df[df['居住縣市']=='台北市'].groupby('居住鄉鎮')['居住鄉鎮'].count())

# 4. 印出資料中台北市最新的發病日期
print('發病日:',df['發病日'].max())