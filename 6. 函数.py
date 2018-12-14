"""
1.函数的定义：

def 函数名（）：
    代码
    
"""

# 函数的好处：减少代码冗余，减少维护量。功能的封装，降低学习成本，提升开发速度。

# 函数练习demo 1如下：
# 1.先定义一个函数：
def practice():
    i=1
    while i<=3:
        print("&"*i)
        i+=1

# 可在定义函数后的任意位置调用函数（且可以多次调用）：
practice()
practice()

# 函数练习demo 2如下：
def my_name():    #之前把函数名定义为test，不能执行。应该是test比较特殊，不能用于命名
    a=10
    b=20
    c=a+b
    print("a+b=",c)

my_name()
my_name()
my_name()