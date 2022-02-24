import csv
import math
#import numpy
import matplotlib.pyplot as plt

list_0_100 = []
list_100_200=[]
list_200_300=[]
list_300up=[]
with open('12.csv', newline='') as csvfile:
  rows = csv.DictReader(csvfile)
  for row in rows:
    i = int(row['累計營業收入-當月累計營收'])
    #print(row['公司名稱'],' ',row['累計營業收入-當月累計營收'])
    if i <1000000:
      list_0_100.append(i)
    elif i>= 1000000 and i<2000000 :
      list_100_200.append(i)
    elif i>= 2000000 and i<3000000:
      list_200_300.append(i)
    else:
      list_300up.append(i)
      
one = float(len(list_0_100))
two = float(len(list_100_200))
three = float(len(list_200_300))
four = float(len(list_300up))

print (f'隨機取一個上市公司他的累積營業收入在0-100萬的機率為{(round((one/(one+two+three+four)),2))*100}%')
print (f'隨機取一個上市公司他的累積營業收入在100-200萬的機率為{(round((two/(one+two+three+four)),2))*100}%')
print (f'隨機取一個上市公司他的累積營業收入在200-300萬的機率為{(round((three/(one+two+three+four)),2))*100}%')
print (f'隨機取一個上市公司他的累積營業收入在 300+萬的機率為{(round((four/(one+two+three+four)),2))*100}%')

xlist = ['0-100','100-200','200-300','300+']
ylist = [(round((one/(one+two+three+four)),2)),(round((two/(one+two+three+four)),2)),(round((three/(one+two+three+four)),2)),(round((four/(one+two+three+four)),2))]
plt.xlim(0,3)
plt.ylim(0,1)
plt.xlabel("x")
plt.ylabel("probability")
plt.bar(xlist,ylist)
plt.show()