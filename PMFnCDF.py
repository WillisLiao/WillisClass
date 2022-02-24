import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
with open('cbb21.csv', newline='') as csvfile:

  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)

  # 以迴圈輸出指定欄位
  for row in rows:
    print(row['G'], row['EFG_D'])

# Probability Mass Function
die_choice = row['G']

die_list = row['EFG_D']
frequencies = [ sum(die_list==x)/times for x in range(1, 40)]
#xlist = [] 
#ylist = []
plt.xlim(1, 40)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel("probability")
plt.bar(die_choice, frequencies)
plt.show()