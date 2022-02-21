import numpy as np
import matplotlib.pyplot as plt
data = np.array([[166, 58.7],
                 [176, 75.7], 
                 [171, 62.1], 
                 [173, 70.4], 
                 [169, 60.1]])
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#設定ax散佈圖
ax.scatter(data[:,0], data[:,1], color = 'red')
#設定圖例
ax.legend(['Data'])
#設定散佈圖名稱
ax.set_title('Sample_1')
x = np.linspace(166, 176)
y = []
for i in x:
    y.append(-245.9362+1.82068*i)
ax.plot(x, y, color='blue')
plt.show()