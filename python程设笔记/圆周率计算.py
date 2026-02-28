# 蒙特卡洛方法估算圆周率π
from random import random
from math import sqrt
from time import perf_counter

DARTS = 10000000  # 总投掷次数（100万次）
hits = 0.0           # 命中单位圆内的次数
start = perf_counter()

for i in range(1, DARTS + 1):
    x, y = random(), random()  # 生成0~1之间的随机坐标(x,y)
    dist = sqrt(x**2 + y**2)   # 计算点到原点的距离
    if dist <= 1.0:            # 判断是否在单位圆内
        hits = hits + 1

pi = 4 * (hits / DARTS)        # 估算圆周率π
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter() - start))