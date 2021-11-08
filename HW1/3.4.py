#15 10000runs
import numpy as np
import matplotlib.pyplot as plt
N = 16

a = [8, 3, 4, 3, 3, 137, 1, 3, 1, 6, 6, 1, 81, 11, 69, 2, 2, 1, 11, 6, 14, 4, 77, 10, 9, 6, 7, 18, 2, 12, 16, 20, 58, 6, 11, 
92, 8, 19, 18, 137, 2, 5, 10, 6, 59, 42, 3, 18, 35, 10, 63, 3, 10, 29, 50, 1, 25, 16, 3, 32, 31, 9, 3, 54, 5, 1, 27, 1, 57, 8, 46, 82, 1, 1, 25, 1, 18, 19, 22, 2, 50, 26, 2, 14, 4, 21, 65, 1, 1, 4, 2, 63, 7, 44, 17, 63, 2, 12, 5, 1, 7, 2, 135, 3, 3, 3, 22, 16, 12, 18, 2, 1, 83, 24, 1, 6, 20, 62, 2, 2, 1, 1, 15, 29, 17, 27, 3, 1, 8, 29, 1, 10, 13, 80, 10, 3, 38, 3, 13, 42, 26, 13, 22, 29, 7, 82, 47, 7, 10, 1, 6, 1, 15, 27, 24, 1, 20, 23, 4, 2, 6, 1, 13, 71, 6, 30, 34, 26, 3, 8, 70, 123, 1, 4, 3, 5, 33, 74, 1, 5, 6, 103, 4, 23, 1, 2, 1, 2, 7, 1, 112, 1, 11, 7, 56, 8, 1, 7, 4, 7, 61, 25, 14, 2, 4, 19, 4, 2, 84, 7, 2, 14, 26, 6, 2, 11, 90, 77, 1, 21, 3, 12, 9, 1, 4, 1, 28, 6, 21, 62, 2, 2, 12, 2, 6, 99, 21, 13, 1, 46, 1, 55, 40, 24, 10, 60, 31, 1, 1, 7, 30, 4, 28, 27, 95, 1, 77, 56, 3, 38, 33, 2, 44, 28, 9, 3, 47, 29, 60, 21, 82, 2, 57, 27, 2, 3, 57, 3, 3, 38, 21, 1, 5, 5, 10, 34, 3, 1, 18, 3, 3, 27, 89, 3, 21, 4, 18, 6, 1, 1, 11, 102, 9, 21, 6, 49, 3, 1, 5, 2, 72, 2, 4, 21, 128, 3, 2, 76, 10, 13, 82, 12, 1, 1, 2, 22, 5, 10, 22, 9, 112, 1, 35, 96, 6, 5, 2, 8, 62, 8, 19, 31, 40, 4, 105, 12, 4, 21, 1, 1, 44, 33, 3, 15, 56, 7, 1, 9, 1, 2, 95, 42, 1, 6, 57, 10, 10, 10, 117, 1, 1, 37, 3, 23, 1, 3, 11, 1, 13, 69, 7, 28, 3, 1, 13, 4, 13, 18, 21, 92, 12, 2, 1, 6, 4, 20, 27, 127, 9, 1, 26, 47, 20, 1, 3, 3, 4, 3, 10, 105, 20, 1, 5, 110, 2, 18, 26, 4, 1, 132, 9, 4, 11, 29, 1, 35, 9, 8, 87, 1, 5, 9, 11, 57, 49, 4, 1, 42, 11, 30, 3, 92, 9, 3, 1, 38, 6, 52, 7, 61, 12, 1, 43, 12, 5, 48, 1, 3, 18, 54, 8, 75, 1, 8, 14, 45, 1, 21, 3, 117, 8, 13, 105, 3, 1, 31, 33, 66, 
1, 11, 1, 7, 5, 23, 56, 5, 5, 1, 27, 23, 76, 1, 12, 26, 4, 41, 38, 15, 1, 117, 2, 16, 38, 2, 105, 9, 1, 11, 4, 1, 1, 26, 
5, 7, 4, 25, 54, 44, 13, 9, 1, 15, 1, 85, 20, 10, 59, 1, 1, 49, 65, 7, 1, 16, 4, 3, 7, 2, 41, 8, 40, 7, 8, 12, 7, 41, 9, 
39, 13, 7, 49, 1, 27, 1, 4, 78, 55, 4, 3, 1, 2, 60, 1, 2, 18, 19, 95, 22, 33, 28, 10, 67, 35, 7, 26, 1, 7, 15, 7, 3, 7, 9, 11, 95, 7, 39, 16, 15, 2, 20, 14, 7, 31, 42, 1, 16, 23, 4, 1, 110, 1, 2, 15, 30, 5, 28, 39, 1, 2, 56, 10, 2, 5, 18, 3, 
3, 46, 21, 19, 1, 10, 70, 1, 11, 89, 11, 5, 5, 111, 13, 14, 6, 14, 16, 18, 22, 3, 4, 2, 18, 82, 3, 13, 1, 16, 95, 22, 1, 
3, 14, 2, 12, 68, 1, 25, 5, 48, 43, 70, 3, 1, 1, 13, 17, 6, 62, 27, 5, 1, 1, 1, 6, 56, 2, 52, 2, 2, 59, 1, 12, 7, 32, 29, 90, 51, 2, 1, 21, 2, 51, 98, 4, 12, 19, 61, 1, 18, 3, 2, 1, 17, 5, 6, 27, 7, 8, 1, 39, 1, 1, 22, 4, 14, 81, 12, 2, 20, 3, 9, 4, 10, 87, 2]


C = []
for i in range(len(a)):
    C.append((len(a)-i)/len(a))
    a[i] = a[i]/(N**2)
a.sort()

plt.scatter(a,C)
plt.show()

Clog = []
alog = []
for i in range(len(a)):
    Clog.append(np.log10(C[i]))
    alog.append(np.log10(a[i]))

plt.scatter(alog,Clog)
plt.show()


