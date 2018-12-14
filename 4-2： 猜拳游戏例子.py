"""
思路分析：
1.获得玩家输入的拳型；
2.显示电脑输入的拳型；
3.比较玩家与电脑拳型，判定输赢
"""

# 获得玩家输入的拳型；
user = int(input("请随机输入一种拳型石头（1）、剪刀（2）、布（3）："))
# 获得电脑输入的拳型；此处还需要导入工具中的函数让它生成随机数
# 如果你不知道为什么是导入random，不知道的问度娘！

import random
computer = random.randint(1,3)
# 比较玩家与电脑拳型，判定输赢
# 情况一：玩家赢
if user==1 and computer==2 or \
    user==2 and computer==3 or \
    user==3 and computer==1:
    print("恭喜您赢啦！")

# if ，while等语句，只要后面是跟有：的，下一行代码需进行缩进。缩进的距离是一个Tab见或4个空格键
# 情况二：平局
if user==computer:
    print("平局")

# 情况三：玩家输
if user==1 and computer==3 or\
    user==2 and computer==1 or\
    user==3 and computer==2:
    print("很遗憾，您输啦！")