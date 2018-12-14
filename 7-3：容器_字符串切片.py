# 知识点1：查找字符串
# 案例：将邮箱中的一部分字符串单独截取出来储存，需要如何操作？
user_email="liulihong@163.com"
#  案列思路分析：首先要了解邮箱的组成：@前面部分是用户名，@后面部分是邮箱域名
# （1）查找字符串中@的位置
# （2）获得字符串中的子串（子串就是字符串中的一部分的意思）
#  第一步查找@的位置需要引入一种方法：find
#  find函数的特点：
#  a.如果能查找到，则返回子串第一次出现的位置
#  b.如果不能查找到，则返回-1
position=user_email.find("@")     # 是字符串的相关操作，字符串在代码中要用""
if position == -1:
    print("未找到@的位置，邮箱不合法！")
else:
    print("@的位置：",position)

# 知识点2：字符串切片（在知识点1基础上拓展）
# 为了获取字符串的一个子串，提供了一种语法叫字符串切片
user_email="liulihong@163.com"
# 之前已查询出了@的位置是9。手动数了几遍，发现@的实际位置是10啊。这儿是不是有问题啊？
# 切片开始位置（起始值），为0或正值时从左往右索引（默认从0开始）。（正数索引）切片的规则是：左闭右开。
# 理解了，这个数数的顺序是跟遍历一样的。第一个字符的下标是从0开始的。所以按这个来理解下面的是没毛病的
print(user_email[0:8])       # 因此本行代码结果中，第8位字母n应该不在结果中啊。讲解：实际从左至右，从0开始数，第8位是g.
# 获得容器元素个数
string_length=len(user_email)
print(string_length)
print(user_email[5:string_length])
# 起始指不写表示从0开始
print(user_email[:4])        # 按讲解第4位的i,所以按左闭右开的原则是OK的
# 结束值不写表示到最后
print(user_email[2:])
print(user_email[:])


# 知识点3：步长
print("*"*30)   # 来个分割线
print(user_email[3:10:2])   # 这里的2就是步长
# 起始值 、结束值、步长都可以是负数
# 起始值为负值时从右向左索引（默认从-1开始），遵循的规则是：右闭左开
print(user_email[-2:-9:-1])
# 字符串逆序
print(user_email[::-1])


# 知识点4：完成邮箱截取的练习—方法1
user_email="niupihonghong@qq.com"
position=user_email.find("@")
if position==-1:
    print("你的邮箱不合法，请重新输入！")
else:
    username=user_email[:position]
    print("邮箱的用户名是：",username)
    houzui=user_email[position+1:]
    print("邮箱的后缀名是：",houzui)


# 知识点4：完成邮箱截取的练习—方法2
# 引入方法.split—拆分的作用，而且能拆分多个
user_email="xiexiaorong@hauen.com"
position=user_email.split("@")
# print(position)
#  增加一个校验步骤，让代码更严谨。（如果有2个及以上的@，邮箱其实是不合法的）
# 统计该邮箱的@字符串个数
char_count=user_email.count("@")
# 对@字符串个数统计后进行判断
if char_count>1:
    print("你输入的邮箱格式有误！")
else:
    print("邮箱名是：",position[0])
    print("邮箱后缀是：",position[1])


