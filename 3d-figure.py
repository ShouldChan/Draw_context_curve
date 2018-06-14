# -*- coding:utf-8 -*-
# __author__="ada_magicjay"

# ┏┓   ┏┓
# ┏┛┻━━━┛┻┓
# ┃    ☃   ┃
# ┃ ┳┛ ┗┳ ┃
# ┃   ┻    ┃
# ┗━┓     ┏━┛
# ┃     ┗━━━┓
# ┃  神兽保佑  ┣┓
# ┃　永无BUG！ ┏┛
# ┗┓┓┏━┳┓┏┛
# ┃┫┫  ┃┫┫
# ┗┻┛  ┗┻┛

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


fig = plt.figure()
# 表示画空间平面图
ax = fig.add_subplot(1,1,1,projection='3d')  # 一行一列第一个

# 设置坐标轴的宽度 长度为8 每格占2
X = np.arange(1, 8, 2)
Y = np.arange(1, 10, 2)


X,Y = np.meshgrid(X, Y)  # 将坐标向量变为坐标矩阵，列为x的长度，行为y的长度

# 填值 x为4 则每个[]中填4个元素， y为5 则有5个[]
Z = np.array([[0.06,0.07,0.08,0.10],[0.08,0.09,0.10,0.11],[0.15,0.16,0.17,0.18],[0.20,0.21,0.22,0.23],[0.08,0.09,0.10,0.11]])
# 构建平面
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)

# 自行调整设置坐标轴标签的对应坐标轴 主要控制值之间的差值喝上述坐标轴宽度一直即可
ax.set_xticks([0,2,4,6])
ax.set_xticklabels( ('1', '3', '5', '10'))
ax.set_yticks([2,4,6,8,10])
ax.set_yticklabels( ('0.0001', '0.001', '0.01', '0.1','1'))

# 设置坐标轴标签 说明每个坐标轴代表的意思
ax.set_xlabel("top-N", color='r')
ax.set_ylabel("alpha", color='g')
ax.set_zlabel("precision", color='b')
# 设置总标题
plt.title("NYC@Precision")

# 设置z坐标轴高度
ax.set_zlim3d(0, 0.3) # 设置z坐标轴
# 图例可有可不有
fig.colorbar(surf, shrink=0.5, aspect=5) # 图例
# 保存图片到文帝
plt.savefig('3D.jpg')

plt.show()
plt.close()