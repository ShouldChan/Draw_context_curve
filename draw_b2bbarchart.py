# coding:utf-8

# 带误差的背对背条形图
from matplotlib import pyplot as plt
import numpy as np

# 输入数据
X1 = np.array([1, 2, 3])
X2 = np.array([2, 2, 3])

bar_labels = ['bar 1', 'bar 2', 'bar 3']

fig = plt.figure(figsize=(8, 6))

# 绘制
y_pos = np.arange(len(X1))
y_pos = [x for x in y_pos]
plt.yticks(y_pos, bar_labels, fontsize=10)

plt.barh(y_pos, X1,
         align='center', alpha=0.4, color='g')

# 我们简单的取反，画第二个条形图
plt.barh(y_pos, -X2,
         align='center', alpha=0.4, color='b')

# 标签
plt.xlabel('measurement x')
t = plt.title('Bar plot with standard deviation')
plt.ylim([-1, len(X1) + 0.1])
plt.xlim([-max(X2) - 1, max(X1) + 1])
plt.grid()

plt.show()