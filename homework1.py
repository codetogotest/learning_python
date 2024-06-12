# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:38:15 2024

@author: Ala
"""

# Homework1
# matrix-1

import numpy as np

# 1.請用亂數種子123，隨機產生㇐維、⾧度為15的矩陣，數字介於5~15 之間、列印輸出
np1 = np.random.RandomState(123).randint(5,16,size=15)
print("隨機正整數:",np1)

# 2.轉成3*5 的矩陣並列印出來
np2 = np1.reshape(3,5)
print("X矩陣內容:")
print(np2)

# 3. 印出矩陣最大值
print("最大:", np.max(np2))

# 4. 印出矩陣最小值
print("最小:", np.min(np2))

# matrix-2
# 5. 印出矩陣所有數字總和
print("總和:", np.sum(np2))

# 6. 印出3*5 矩陣的4 個角落的元素內容，輸出成2*2 矩陣
np3 = np2[np.ix_([0,2], [0,4])]
print("四個角落元素:")
print(np3)