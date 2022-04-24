#光滑管
import math
temp = 1 
while temp != 114514 :
    v = float(input("请输水流量："))
    pa = float(input("请输入▲压降："))
    d = 0.021                                           #管内径 单位m
    l = 1.5                                             #管长度1.5m
    u = v/((pow(0.0105,2)*3.1415926)*3600)              #平均流速
    #print("平均流速为：",u)
    p = 998.2                                           #温度20°左右水的密度
    vn = 100.5                                          #20°左右水的黏度x10e(-5)
    Re = float(((d * u * p) / vn) * 100000)
    print("Re为: ",Re)
    blasius = 0.3164/(pow(Re,0.25))
    print("层流的摩擦阻力系数blasius：",blasius)               #输出入blasius   
    mcxs = (2 * d * pa)/(p * l * pow(u,2))
    print("摩擦系数为：",mcxs)
    print()
    temp = int(input("按任意键继续，输入114514终止程序: "))
