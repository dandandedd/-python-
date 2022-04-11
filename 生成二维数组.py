#生成一个4*5的二维数组
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(4):
        matrix[i].append(input("请输入数字"))
print(matrix)