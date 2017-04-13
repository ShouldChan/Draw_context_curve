# coding:utf-8

# 带误差线的条形图
import matplotlib.pyplot as plt

# 输入数据
mean_values = [1, 2, 3]
variance = [0.2, 0.3, 0.5]
bar_labels = ['cxj', 'wk', 'success']

# 绘制图形
x_pos = list(range(len(bar_labels)))
plt.bar(x_pos, mean_values, yerr=variance, align='center', alpha=0.5)

plt.grid()

# 设置y轴高度
max_y = max(zip(mean_values, variance))  # return a tuple
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# 设置轴标签和标题
plt.ylabel('variable y')
plt.xticks(x_pos, bar_labels)
plt.title('Bar plot with error bars')

plt.show()

# 保存图片
# plt.savefig('./my_plot.png')
