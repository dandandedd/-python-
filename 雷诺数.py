#层流管
import math
temp = 1 
while temp != 0 :
    v = float(input("请输入体积："))
    t = float(input("请输入时间："))
    pa = float(input("请输入压降：")) - 0.16
    l = 1.5
    d = 0.0032                  #管内径 单位m
    u = ((v/t)*0.000001)/(0.0016*0.0016*3.1415926)                     #平均流速
    #print("平均流速为：",u)
    p = 998.2                   #温度20°左右水的密度
    vn = 100.5*0.00001                  #20°左右水的黏度x10（-5）
    Re = (d * u * p)/vn
    print("Re为: ",Re)
    cl = 64/Re
    print("层流的摩擦阻力系数 入 理论：",cl)
    clsj = (2 * d * pa * 1000)/(p * l * pow(u,2))
    print("入实际为：",clsj)
    print()
    temp = int(input("按任意键继续，输入114514终止"))
    
