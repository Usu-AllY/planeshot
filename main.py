qipan=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]   #10*10棋盘
zhenxing=[
    [0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,1,1,1,1,1],
    [0,0,1,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,1,1,1,0],
    [1,1,1,2,0,2,0,0,0,0],
    [1,0,1,1,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]   #飞机阵型
print("游戏规则为：10*10棋盘内有三架飞机，空地为0，机身为1，机头为2，击毁三个机头为胜")
print("当前棋盘为：")
print(qipan[0])
print(qipan[1])
print(qipan[2])
print(qipan[3])
print(qipan[4])
print(qipan[5])
print(qipan[6])
print(qipan[7])
print(qipan[8])
print(qipan[9]) #打印棋盘
n=0
step=0
while n<3:
    step=step+1
    hang=int(input("请输入目标纵坐标（正整数1-10）："))   #行
    lie=int(input("请输入目标横坐标（正整数1-10）："))    #列
    qipan[hang-1][lie-1]=zhenxing[hang-1][lie-1]    #为解决常规坐标与列表的冲突故-1
    print("当前棋盘为")
    print(qipan[0])
    print(qipan[1])
    print(qipan[2])
    print(qipan[3])
    print(qipan[4])
    print(qipan[5])
    print(qipan[6])
    print(qipan[7])
    print(qipan[8])
    print(qipan[9]) #打印棋盘
    if zhenxing[hang-1][lie-1]==2:
        n=n+1
        print("摧毁飞机")
    elif zhenxing[hang-1][lie-1]==1:
        print("击中飞机")
    else:
        print("目标为空")
print("您已摧毁所有飞机")
print("您使用步数为：",step)


