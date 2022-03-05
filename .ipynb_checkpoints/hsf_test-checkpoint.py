import csv
import math
from re import L
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
from sympy import E


df = pd.read_csv('cbb21.csv')
df1 = pd.DataFrame(df, columns = ["EFG_D"]) # 指定欄標籤名稱
row_count = df1.shape[0]
a = df1.query("EFG_D > 40 and EFG_D <= 44").shape[0]
b = df1.query("EFG_D > 44 and EFG_D <= 48").shape[0]
c = df1.query("EFG_D > 48 and EFG_D <= 52").shape[0]
d = df1.query("EFG_D > 52 and EFG_D <= 56").shape[0]
e = df1.query("EFG_D > 56 and EFG_D <= 60").shape[0]
f = df1.query("EFG_D > 60 ").shape[0]



# Probability Mass Function
x = ["40~44", "44~48", "48~52", "52~56", "56~60", ">60"]
EFG_prob = [a/row_count, b/row_count, c/row_count, d/row_count, e/row_count, f/row_count ]

plt.xlim(0, 6)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel("probability")
plt.bar(x, EFG_prob)
plt.show()








