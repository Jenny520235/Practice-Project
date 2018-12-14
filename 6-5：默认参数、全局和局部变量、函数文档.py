#  知识点1: 函数的缺省参数（默认参数）

# 情况一：函数中只有一个参数
def my_function(num=1314):    # 也可以将num设置一个默认参数，调用函数时没有额外赋值的话就认为是调用的默认参数
    print(num)
# my_function()   不填入位置参数直接引用函数会报错。因为该函数是有一个位置参数的
my_function()
my_function(1021)  # 调用函数是有专门赋值，就会使用专用的赋值。
my_function()      # 上面对num设置了一个默认值1314，没有额外赋值的情况下就认为使用默认值1314

# 情况二：函数中有多个参数

def practice(a,b=65,c=98):   # 如果在这里替其中的某个形参设置默认值，请观察后面的函数引用看效果并得出结论。
    ret=a+b+c
    return ret
#  practice()   上述函数有个位置参数，直接调用不赋值会报错
ret=practice(14,35,98)    # 这种写法是常规的写法
print(ret)
ret=practice(74)
print(ret)

# 知识点2：函数的局部变量和全局变量
# 2-1：函数的局部变量，即在函数内部定义的变量
# 例如下列示例
def my_practice(left,right):
    a=left       # 此函数中的a=left, b=right就是局部变量。只存在于函数内部的，不能在函数外部使用。
    b=right
    result =a+b
    return result
result=my_practice(32,56)
print(result)

# 2-2：全局变量，即在函数外部定义的变量
g_number=69
def my_function():
    print(g_number)
my_function()
my_function()

my_number=698
def my_function():
    my_number=100       # 变量要先定义再使用
    print(my_number)    # 为什么打印显示的是函数内部这个变量的值呢？   就近原则！
my_function()
print(my_number)     #这里的结果打印显示的是函数外部变量的值，698


# 知识点3：函数文档
g_number=69
def my_function():
    """函数文档的内容.
    
    :示例加法
    ：示例减法
    ：反正就是多些点文档备注吧
    """     # Ctrl+Q即可显示函数文档内容。
    print(g_number)
my_function()



