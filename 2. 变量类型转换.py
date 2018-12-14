# 其实从我做名片的 那个练习就发现了变量类型需要转换的问题。
# 变量类型转换的练习：
# 应用input函数完成计算器计算程序的练习：
number1=input("请输入第一个数字:")
number2=input("请输入第二个数字:")
#  同时查询number1、number2的输出结果是什么类型的？
print(type(number1),type(number2))
# 查询到number1 、number2的输出结果的字符串。那么要进行后面的计算器运算，就必须要把字符串类型转换成数字类型。
number1_int = int(number1)
number2_int = int(number2)
result = number1_int + number2_int
print("%d+%d=%d" %(number1_int,number2_int,result))

