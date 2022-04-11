import random
   
# 创建并初始化二维列表
matrix = []
for i in range(88):
    matrix.append([])
    for j in range(88):
        matrix[i].append(random.randint(0, 1024))