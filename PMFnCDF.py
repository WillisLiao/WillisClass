import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

list0_10 = []
list10_20 = []
list20_30 = []
list30_40 = []
list40_50 = []
list50_60 = []

df = pd.read_csv('cbb21.csv')
print(df.head) 


with open('cbb21.csv', newline='') as csvfile:
  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)
  
  #row_count = sum(1 for row in rows)  # rows is your csv.reader
  #print(row_count)
  # 以迴圈輸出指定欄位
  for row in rows:
    i = float(row['EFG_D'])
    print(i)
    if 0<i<=10:
      list0_10.append(i)
      print(list0_10)
    elif 10<i<=20:
      list10_20.append(i)
    elif 20<i<=30:
      list20_30.append(i)
    elif 30<i<=40:
      list30_40.append(i)
    elif 40<i<=50:
      list40_50.append(i)
    elif 50<i:
      list50_60.append(i)


# Probability Mass Function
x = ["0~10", "10~20", "20~30", "30~40", "40~50", "50~60"]
#EFG_prob = [len(list0_10)/row_count,
#              len(list10_20)/row_count,
#              len(list20_30)/row_count, 
#              len(list30_40)/row_count,
#              len(list40_50)/row_count,
#              len(list50_60)/row_count]

plt.xlim(0, 6)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel("probability")
#plt.bar(x, EFG_prob)
plt.show()

print(list0_10, list10_20, list20_30, list30_40, list40_50, list50_60)

    


