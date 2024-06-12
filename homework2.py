# -*- coding: utf-8 -*-

import matplotlib as mpl

mpl.use('Agg')



import matplotlib.pyplot as plt



labels = ["Jun", "Jul", "Aug", "Sep"]

sizes = [20, 30, 40, 10]

# 圓餅圖顏色

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']



# 長條圖 位置

plt.subplot(1, 2, 1)

xticks = range(0, len(labels))

# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）

plt.xticks(xticks, labels)

plt.bar(labels, sizes, color="blue")



# 圓餅圖 位置

plt.subplot(1, 2, 2)

# 圓餅圖以labels為圖標，sizes為各項所占百分比

# 圓餅圖colors為各項顏色，突顯「Aug」

# 圓餅圖顯示各項百分比到小數點第1位

explode = (0, 0, 0.1, 0)

plt.pie(sizes, explode=explode, labels=labels,

        colors=colors, autopct='%1.1f%%')

# 長寬比為1:1

plt.axis('equal')

plt.show()

#plt.savefig('chart.png')

#plt.close()