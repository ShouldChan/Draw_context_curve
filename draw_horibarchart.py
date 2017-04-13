# coding:utf-8
from matplotlib import pyplot as plt
import numpy as np

# 输入数据
mean_values = [1, 2, 3]
std_dev = [0.2, 0.4, 0.5]
bar_labels = ['bar 1', 'bar 2', 'bar 3']

fig = plt.figure(figsize=(8, 6))

# 绘制条形图
y_pos = np.arange(len(mean_values))
y_pos = [x for x in y_pos]
plt.yticks(y_pos, bar_labels, fontsize=10)
plt.barh(y_pos, mean_values, xerr=std_dev,
         align='center', alpha=0.4, color='g')

# 标签
plt.xlabel('measurement x')
t = plt.title('Bar plot with standard deviation')
plt.ylim([-1, len(mean_values) + 0.5])
plt.xlim([0, 4])
plt.grid()

plt.show()