#生成[1,11 )区间上3行5列的随机整数数组
import random
h = 0
for i in range(15):
    t = random.randint(1,11)
    print( t ,end = '    ')
    h = h+1
    if h %3 ==0 :
        print()
#已上传到GitHub 原创