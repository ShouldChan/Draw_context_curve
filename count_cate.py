# coding: utf-8

import time

data_dir = "./data/"
t = time.time()

# 1.将地点分类中的‘，’去除
# with open(data_dir + "TKY_category.txt", "r") as fopen:
#     lines = fopen.readlines()
#     cate_data = []
#     for line in lines:
#         data = line.strip().split('\t')
#         id, venue = int(data[0]), data[1]
#         if venue.find(',') != -1:
#             new_venue = venue.replace(',', ' ')
#         cate_data.append([id, new_venue])
#         print new_venue
#     print "update ',' ok..."
#
# with open(data_dir + "TKY_category_1.txt", "w") as fwrite:
#     for [id, new_venue] in cate_data:
#         fwrite.write(str(id) + "\t" + str(new_venue) + "\n")
#     print id, "\t", new_venue

# 2.整合签到最多的几种大分类
# with open(data_dir + "TKY_train0.txt", "r") as fopen:
#     lines = fopen.readlines()
#     count_cate = []
#     for line in lines:
#         data = line.strip().split('\t')
#         venue, weektime = data[3], data[7].strip().split(' ')
#         weekday = weektime[0]
#         timeofday = weektime[3].rstrip().split(':')
#         hour = timeofday[0]
#         # print hour
#         # print weekday
#         if (venue.find('Nightlife') != -1 or venue.find('Theater') != -1) and hour == '21':
#             count_cate.append([id, venue])
#             # print venue
# print "count_cate checkins: %d Elapsed....." % len(count_cate), time.time() - t

# 3.统计各分类的签到概率（shop,restaurant,school,nightlife）
# shop_list = [5665, 5132, 4995, 5110, 4842, 7340, 7930]
# rest_list = [6010, 5742, 5780, 5815, 6396, 6830, 6335]
# school_list = [2096, 2091, 2046, 2211, 1756, 1460, 1310]
# night_list = [6292, 5488, 5493, 5700, 5922, 8458, 8559]
# shop_prop = []
# rest_prop = []
# school_prop = []
# night_prop = []
# for ss in shop_list:
#     pss = (1.0 * ss) / (1.0 * sum(shop_list))
#     # print pp
#     shop_prop.append(pss)
# print shop_prop
#
# for rr in rest_list:
#     prr = (1.0 * rr) / (1.0 * sum(rest_list))
#     # print pp
#     rest_prop.append(prr)
# print rest_prop
#
# for sh in school_list:
#     psh = (1.0 * sh) / (1.0 * sum(school_list))
#     # print pp
#     school_prop.append(psh)
# print school_prop
#
# for ni in night_list:
#     pni = (1.0 * ni) / (1.0 * sum(night_list))
#     # print pp
#     night_prop.append(pni)
# print night_prop
#
# # 4.统计timeofday_probability
# shop_time = [76, 36, 52, 124, 301, 687, 1399, 1008, 1083, 1483, 2296, 2246, 2572, 3125, 3551, 4081, 4926, 4552, 3198,
#              1994, 1170, 637, 287, 128]
# rest_time = [145, 109, 61, 144, 233, 506, 553, 397, 336, 1554, 5351, 4005, 2379, 1509, 1338, 2023, 3994, 5588, 4994,
#              3657, 2171, 1108, 511, 212]
# school_time = [13, 14, 5, 28, 119, 279, 1205, 909, 1073, 599, 1332, 1068, 1096, 779, 1007, 827, 848, 729, 416, 293, 150,
#                117, 44, 20]
# night_time = [251, 537, 359, 393, 393, 142, 74, 25, 16, 13, 8, 4, 5, 13, 24, 57, 96, 135, 128, 209, 235, 200, 254, 298]
# shop_time_prob = []
# rest_time_prob = []
# school_time_prob = []
# night_time_prob = []
#
# for ss_ti in shop_time:
#     pss_ti = (1.0 * ss_ti) / (1.0 * sum(shop_time))
#     # print pp
#     shop_time_prob.append(pss_ti)
# print shop_time_prob
#
# for rr_ti in rest_time:
#     prr_ti = (1.0 * rr_ti) / (1.0 * sum(rest_time))
#     # print pp
#     rest_time_prob.append(prr_ti)
# print rest_time_prob
#
# for sh_ti in school_time:
#     psh_ti = (1.0 * sh_ti) / (1.0 * sum(school_time))
#     # print pp
#     school_time_prob.append(psh_ti)
# print school_time_prob
#
# for ni_ti in night_time:
#     pni_ti = (1.0 * ni_ti) / (1.0 * sum(night_time))
#     # print pp
#     night_time_prob.append(pni_ti)
# print night_time_prob

# 4.draw_category_process筛选next poi
with open(data_dir+"TKY_train2","r") as fcate_4_1:
    lines = fcate_4_1.readlines()
    poi_data = []
    for line in lines:
        data = line.strip().split('\t')
        venue, weektime = data[3], data[7].strip().split(' ')
        weekday = weektime[0]
        timeofday = weektime[3].rstrip().split(':')
        hour = timeofday[0]
print "count_cate checkins: %d Elapsed....." % len(count_cate), time.time() - t
