# coding:utf-8
# 带颜色色差的条形图  很实用
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm

# 输入数据
mean_values = range(10, 18)
x_pos = range(len(mean_values))

# 创建 colormap
cmap1 = cm.ScalarMappable(col.Normalize(min(mean_values), max(mean_values), cm.hot))
cmap2 = cm.ScalarMappable(col.Normalize(0, 20, cm.hot))

# 画条
plt.subplot(121)
plt.bar(x_pos, mean_values, align='center', alpha=0.5, color=cmap1.to_rgba(mean_values))
plt.ylim(0, max(mean_values) * 1.1)

plt.subplot(122)
plt.bar(x_pos, mean_values, align='center', alpha=0.5, color=cmap2.to_rgba(mean_values))
plt.ylim(0, max(mean_values) * 1.1)

plt.show()