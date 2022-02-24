import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
with open('cbb21.csv', newline='') as csvfile:

  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)
  lines= len(list(rows))

  # 以迴圈輸出指定欄位
  EFG_list=[]
  for row in rows:
    print(row['EFG_D'])
    EFG_list.append(row['EFG_D'])

# Probability Mass Function
for i in EFG_list(lines):
  if i

frequencies = [ /lines for x in range(1, 8)]
    
#xlist = [] 
#ylist = []
plt.xlim(1, 40)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel("probability")
plt.bar(EFG_list, frequencies)
plt.show()
print(lines)