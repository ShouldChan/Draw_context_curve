# coding:utf-8
# 带标签的条形图
'''
from matplotlib import pyplot as plt
import numpy as np

data = range(200, 225, 5)

bar_labels = ['a', 'b', 'c', 'd', 'e']

fig = plt.figure(figsize=(10, 8))

# 画图
y_pos = np.arange(len(data))
plt.yticks(y_pos, bar_labels, fontsize=16)
bars = plt.barh(y_pos, data,
                align='center', alpha=0.4, color='g')

# 注释

for b, d in zip(bars, data):
    plt.text(b.get_width() + b.get_width() * 0.08, b.get_y() + b.get_height() / 2,
             '{0:.2%}'.format(d / min(data)),
             ha='center', va='bottom', fontsize=12)

plt.xlabel('X axis label', fontsize=14)
plt.ylabel('Y axis label', fontsize=14)
t = plt.title('Bar plot with plot labels/text', fontsize=18)
plt.ylim([-1, len(data) + 0.5])
plt.vlines(min(data), -1, len(data) + 0.5, linestyles='dashed')
plt.grid()

plt.show()
'''

import matplotlib.pyplot as plt

# 输入数据
mean_values = [1, 2, 3]
variance = [0.2, 0.3, 0.5]
bar_labels = ['bar 1', 'bar 2', 'bar 3']

# 画条
x_pos = list(range(len(bar_labels)))
rects = plt.bar(x_pos, mean_values, align='center', alpha=0.5)


# 标签
def autolabel(rects):
    for ii, rect in enumerate(rects):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.02 * height, '%s' % (mean_values[ii]),
                 ha='center', va='bottom')


autolabel(rects)

# 设置y轴高度
max_y = max(zip(mean_values, variance))  # returns a tuple, here: (3, 5)
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# 设置标题
plt.ylabel('variable y')
plt.xticks(x_pos, bar_labels)
plt.title('Bar plot with labels')

plt.show()
# plt.savefig('./my_plot.png')