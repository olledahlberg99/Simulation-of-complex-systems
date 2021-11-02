import numpy as np
import matplotlib.pyplot as plt


a = [11, 3, 7, 76, 189, 398, 4, 45733, 11, 38, 233, 27, 37147, 40, 4, 6, 12, 173, 26, 31278, 2, 64, 26, 111, 33, 830, 19639, 15074, 1, 13, 6, 6, 22168, 
3, 159, 16300, 5, 3, 22, 419, 3266, 56, 10965, 3, 10697, 10, 3, 8210, 6, 4738, 2, 1, 18555, 1, 23, 10749, 6, 70, 547, 251, 28507, 40, 3, 31673, 3269, 3, 13, 3623, 1031, 4, 43, 10, 29284, 1, 165, 4, 27, 34, 42764, 2, 99, 26, 13867, 17, 2, 15308, 26, 1, 1, 1597, 8, 251, 32233, 1042, 18, 7, 22, 41, 293, 38057, 2592, 6, 7, 12, 20, 33, 59, 31074, 65, 5, 249, 23, 28, 288, 78, 100, 1211, 15905, 16, 69, 18597, 2, 1550, 115, 11, 30, 1, 73, 36627, 1, 1512, 1, 3, 8, 9, 1514, 5, 29, 1, 30626, 57, 3, 14, 801, 560, 100, 19035, 2724, 15327, 5, 33, 1, 9, 2, 7, 26042, 13034, 8, 14, 1, 134, 4171, 38360, 2, 2, 21, 30, 724, 4076, 3253, 22882, 4, 8, 1802, 59, 5, 1, 14505, 62, 1, 15265, 7886, 30, 3, 5, 500, 4256, 36279, 295, 11, 102, 22, 8571, 3, 22939, 49, 18, 16, 1265, 10, 200, 8060, 2, 30232, 1, 5, 370, 85, 33482, 2092, 4, 3, 14, 15, 3439, 216, 1, 10522, 23230, 1, 6, 11, 72, 7, 15186, 24168, 9, 1, 54, 129, 41, 1589, 286, 9, 42185, 18, 78, 37, 4093, 35933, 4, 2, 4, 101, 1, 68, 177, 18, 40161, 3, 2, 5, 3, 105, 34, 19, 20, 41554, 4, 13, 1, 101, 9, 13, 17, 20, 7, 21, 46193, 4, 336, 244, 3, 44625, 1, 30804, 29, 4, 8, 133, 409, 3, 31713, 53, 5166, 1, 2208, 15480, 150, 6029, 2, 79, 2, 3, 8803, 378, 5079, 8, 9946, 178, 418, 28, 4, 2, 6, 8, 11, 14222, 1562, 16, 31410, 49, 12297, 2, 12, 552, 31, 21688, 1, 135, 585, 4, 380, 2, 117, 642, 23600, 12165, 26, 21, 182, 20, 632, 18479, 3741, 2999, 7215, 1225, 1, 124, 38, 4, 9, 2, 1124, 5045, 14, 1, 10256, 26, 28231, 4, 8, 30, 3, 30, 108, 4074, 29, 2845, 12, 10536, 2, 3131, 2, 1, 1320, 754, 9, 203, 27, 18185, 5, 8274, 7, 17322, 25, 2021, 3, 323, 6, 17906, 3, 34, 124, 4899, 18793, 37, 1, 14, 17, 72, 268, 16808, 31, 20030, 12233, 6227, 10, 14, 158, 109, 21701, 4644, 1, 8830, 1, 29, 1, 32405, 53, 22, 1, 38, 12771, 2583, 168, 17, 21657, 
13, 50, 109, 14, 282, 38938, 78, 3, 867, 2881, 8, 114, 28051, 5, 945, 7, 30, 3, 2985, 19, 2, 40794, 1, 4109, 46, 856, 3399, 22863, 3394, 1, 1, 39380, 10069, 926, 17920, 5, 5, 6, 15, 6, 4, 3, 57, 14349, 40, 1, 5984, 6, 79, 37539, 1, 2, 732, 2, 26, 48, 167, 12337, 129, 27334, 1, 11, 14, 7, 7, 24, 
21, 542, 206, 10851, 174, 42, 17945, 3562, 5, 11, 1, 5, 12839, 874, 1, 27524, 2, 12467, 8, 3, 1445, 12, 3514, 3059, 22235, 34, 12397, 29, 5, 36, 81, 32, 6352, 14903, 114, 6, 40, 16, 3465, 26124, 8627, 1, 5742, 91, 4, 32482, 4, 11, 3, 2, 6427, 2, 6, 5, 31806, 10, 14, 4, 37, 12, 13, 6, 30, 7, 121, 10162, 9230, 19982, 7, 1, 21, 4, 36, 380, 91, 1310, 26151, 1372, 3898, 1, 9, 2213, 7, 18369, 12088, 5, 9, 2, 24, 5537, 30390, 824, 3, 1, 194, 9, 21, 58, 39575, 13, 1, 20, 24, 5, 7, 13, 24155, 714, 18, 5928, 62, 7719, 37, 59, 6788, 20250, 1, 2872, 198, 6356, 5, 10735, 1547, 17747, 1, 90, 131, 58, 6, 1, 93, 13953, 12345, 3, 11670, 6, 526, 20775, 15468, 58, 2, 88, 7784, 11, 16088, 21, 278, 4329, 1, 5873, 7, 7, 2021, 357, 94, 9652, 1, 5, 2, 2, 6, 36559, 1, 5, 8, 233, 887, 42924, 2, 11, 38, 211, 1409, 613, 37231, 3, 9, 63, 34039, 74, 64, 654, 55, 56, 25, 30302, 38, 983, 11, 1311, 20, 809, 
37079, 1, 1148, 755, 293, 3, 39108, 9, 2, 3, 2, 5, 2, 3, 9, 22, 1, 36684, 2, 1, 47, 774, 60, 7653, 77, 29515, 5244, 4, 7, 8, 38, 921, 38580, 2, 7, 10938, 31099, 7, 1, 4, 41, 15, 1395, 28260, 7, 3, 7, 6224, 818, 1, 11035, 16819, 1, 17, 98, 1, 48, 37917, 1666, 319, 2, 53, 221, 1872, 303, 1044, 6395, 52, 35348, 2, 1, 960, 2165, 7, 6, 32, 6, 162, 35, 32574, 18, 25, 470, 4, 320, 5, 36946, 181, 2, 31, 31, 2, 14, 90, 54, 4, 2218, 2502, 4, 27667, 50, 14, 9, 5818, 4, 1, 37562, 5, 8, 2, 118, 28, 671, 23160, 10874, 91, 3730, 14145, 333, 73, 460, 83, 10122, 1, 2308, 3, 7, 1, 1912, 1442, 9, 26167, 
233, 35, 7483, 12, 4925, 24960, 1, 5952, 4, 9, 12, 3663, 18, 22, 28, 74, 714, 35, 1, 27584, 3897, 244, 1, 18, 5, 478, 26318]

plt.hist(a, bins = 100) 
plt.title("Forest fire histogram")
plt.show()