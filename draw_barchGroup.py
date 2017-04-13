# coding:utf-8
# 条形图群
import matplotlib.pyplot as plt

# 输入数据
green_data = [1, 2, 3]
blue_data = [3, 2, 1]
red_data = [2, 3, 3]
labels = ['group 1', 'group 2', 'group 3']

# 设置条形图的位置和宽度
pos = list(range(len(green_data)))
width = 0.2

# 绘制
fig, ax = plt.subplots(figsize=(8, 6))

plt.bar(pos, green_data, width,
        alpha=0.5,
        color='g',
        label=labels[0])

plt.bar([p + width for p in pos], blue_data, width,
        alpha=0.5,
        color='b',
        label=labels[1])

plt.bar([p + width * 2 for p in pos], red_data, width,
        alpha=0.5,
        color='r',
        label=labels[2])

# 设置标签和距离
ax.set_ylabel('y-value')
ax.set_title('Grouped bar plot')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(labels)

# 设置x，y轴限制
plt.xlim(min(pos) - width, max(pos) + width * 4)
plt.ylim([0, max(green_data + blue_data + red_data) * 1.5])

# 绘制
plt.legend(['green', 'blue', 'red'], loc='upper left')
plt.grid()
plt.show()