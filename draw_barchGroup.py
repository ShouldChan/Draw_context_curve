# coding:utf-8
# 条形图群
import matplotlib.pyplot as plt

# 输入数据
green_data = [0.39, 0.36, 0.35, 0.25, 0.238, 0.23, 0.23, 0.23]
blue_data = [0.44, 0.42, 0.36, 0.27, 0.238, 0.23, 0.23, 0.23]
red_data = [0.36, 0.36, 0.35, 0.25, 0.238, 0.23, 0.23, 0.23]
yellow_data = [0.47, 0.42, 0.24, 0.235, 0.238, 0.23, 0.23, 0.23]
labels = ['1', '5', '10', '15', '20', '40', '60', '80', '100']

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

plt.bar([p + width * 3 for p in pos], yellow_data, width,
        alpha=0.5,
        color='y',
        label=labels[3])

# 设置标签和距离
ax.set_ylabel('precision')
ax.set_title('Precision@K')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(labels)

# 设置x，y轴限制
plt.xlim(min(pos) - width, max(pos) + width * 4)
plt.ylim([0, max(green_data + blue_data + red_data + yellow_data) * 1.5])

# 绘制
plt.legend(['RankNet', 'RankBoost', 'ListNet', 'MRTC'], loc='upper left')
plt.grid()
plt.show()
