# coding:utf-8

#带填充模式的条形图  很美丽

import matplotlib.pyplot as plt

patterns = ('-', '+', 'x', '\\', '*', 'o', '0', '.')

fig = plt.gca()

# 输入数据
mean_values = range(1, len(patterns) + 1)

# 画条
x_pos = list(range(len(mean_values)))
bars = plt.bar(x_pos,
               mean_values,
               align='center',
               color='white',
               )

# 设置填充模式
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# 设置标签
fig.axes.get_yaxis().set_visible(False)
plt.ylim([0, max(mean_values) * 1.1])
plt.xticks(x_pos, patterns)

plt.show()
