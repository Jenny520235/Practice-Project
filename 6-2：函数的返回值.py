"""
def one (a,b):
    ret=a+b
    print(ret)
# 保存函数的执行的结果ret的值
ret=one(24,62)
# 将ret再运用到计算中
my_sum = ret+61
print(my_sum)
# 点评：这种写法是错误的。因为函数内的结果ret是不能获取到的。因此需要引入函数返回值的概念
"""

# 引入函数返回值的概念
# 例1：
def one (a,b):
    ret=a+b
#   此处引入函数返回值
    return ret    # 用return语句去定义函数返回值是ret（ret要是函数里已被定义的形参）
ret=one(36,75)     #上一行代码接收了ret的返回值，此行代码中就可以应用了。将函数one()的结果传给ret（赋值给ret）
my_sum = ret + 61
print(my_sum)


# 例2：
def one (a,b):
    ret=a+b
    return a       # 用return语句去定义函数返回值是a,  a=24, my_sum =24+61
a=one(24,62)
my_sum =a+61
print(my_sum)