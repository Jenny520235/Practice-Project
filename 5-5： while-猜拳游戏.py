# 获得玩家输入的操作：
# 若没按游戏规则输入，输入其他则退出游戏
# 在此处加上while循环
while True:
    operation=int(input("请输入您的拳型：0(剪刀)、1(石头)、2（布）、3（退出游戏）:"))
    import random
    manipulation=random.randint(0,2)
    # 判断玩家与电脑AI的拳型
    # 情况一：玩家赢
    if (operation==0 and manipulation==2)or (operation==1 and manipulation==0) or (operation==2 and manipulation==1):
        print("恭喜您赢啦！")
    #情况二：玩家输
    elif (operation==0 and manipulation==1) or (operation==1 and manipulation==2) or (operation==2 and manipulation==0):
        print("很遗憾你输啦")
    # 情况三：平局
    elif (operation==manipulation):
        print("平局")
    elif(operation==3):
        print("退出游戏")
        break
    else:
        print("输入有误，请重新输入!")