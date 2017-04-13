# coding:utf-8
# 叠加条形图
import matplotlib.pyplot as plt

blue_data = [100, 120, 140]
red_data = [150, 120, 190]
green_data = [80, 70, 90]

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

bar_width = 0.5

# positions of the left bar-boundaries
bar_l = [i + 1 for i in range(len(blue_data))]

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i + (bar_width / 2) for i in bar_l]

###################
## Absolute count
###################

ax1.bar(bar_l, blue_data, width=bar_width,
        label='blue data', alpha=0.5, color='b')
ax1.bar(bar_l, red_data, width=bar_width,
        bottom=blue_data, label='red data', alpha=0.5, color='r')
ax1.bar(bar_l, green_data, width=bar_width,
        bottom=[i + j for i, j in zip(blue_data, red_data)], label='green data', alpha=0.5, color='g')

plt.sca(ax1)
plt.xticks(tick_pos, ['category 1', 'category 2', 'category 3'])

ax1.set_ylabel("Count")
ax1.set_xlabel("")
plt.legend(loc='upper left')
plt.xlim([min(tick_pos) - bar_width, max(tick_pos) + bar_width])
plt.grid()

# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

############
## Percent
############

totals = [i + j + k for i, j, k in zip(blue_data, red_data, green_data)]
blue_rel = [i / j * 100 for i, j in zip(blue_data, totals)]
red_rel = [i / j * 100 for i, j in zip(red_data, totals)]
green_rel = [i / j * 100 for i, j in zip(green_data, totals)]

ax2.bar(bar_l, blue_rel,
        label='blue data', alpha=0.5, color='b', width=bar_width
        )
ax2.bar(bar_l, red_rel,
        bottom=blue_rel, label='red data', alpha=0.5, color='r', width=bar_width
        )
ax2.bar(bar_l, green_rel,
        bottom=[i + j for i, j in zip(blue_rel, red_rel)],
        label='green data', alpha=0.5, color='g', width=bar_width
        )

plt.sca(ax2)
plt.xticks(tick_pos, ['category 1', 'category 2', 'category 3'])
ax2.set_ylabel("Percentage")
ax2.set_xlabel("")

plt.xlim([min(tick_pos) - bar_width, max(tick_pos) + bar_width])
plt.grid()

# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()