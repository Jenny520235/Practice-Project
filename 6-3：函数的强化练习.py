"""
练习1：编写一个函数用于计算从start开始到end结束的所有数字的累加和。

不知道如何下手时，先写出基础功能，再在其基础上复杂化
之前练习过计算1—100之间的累加和，这就是其的中心思想，主体功能
i=1
result=0
while i<=100:
    result=i+result         也可以写成：result += i
    i+=1
print(result)
 再找出它的形参，再改成函数即可.i是要可变的，result也是可变的，即这两个就是形参
 """
def demo(start,end):
    i=start
    result=0
    while i <=end:
        result += i
        i += 1
    return result
# 定义一个新的变量来保存函数的返回值
ret=demo(14,29)
print("ret：",ret)
ret=demo(0,100)
print("ret：",ret)


"""
练习2：编写一个函数，能根据传入的运算符进行相应的加减乘除运算。
思路：先写一个最基本的主体,如加法运算。再在其基础上作分析
def demo1():
a=10          # a不能写死
b=20          # b不能写死
result=a+b    #   由于这里的运算符不能写死成“+”号，即将它定义成operator，需要根据输入来判断用什么运算法。即要用到if语句
return result
"""
def my_caculator(left,right,operator):
    a=left
    b=right
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    else:
        print("你输入的运算符有误，请重新输入")
        result = None  # none 在python中表示无意义的值
    return result  #因为该函数有返回值，需给返回值一个结果。如不给结果的话，就会报错。
result = my_caculator(24,38,"*")
print(result)
result = my_caculator(953,287,"-")
print(result)
result = my_caculator(719,84552,"+")
print(result)
result = my_caculator(86,24,"/")
print(result)
result = my_caculator(89,25,"@")
print(result)






