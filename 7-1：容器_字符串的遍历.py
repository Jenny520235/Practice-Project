# 知识点1：如何定义字符串：
# 字符串一般是用一对单引号或双引号来定义，多行字符串是用一对三引号来定义
my_str='hello'
print(my_str)
my_str="hello"
print(my_str)
my_str="""
dsfks
fssfsk
nfsdjkfsk
"""
print(my_str)


# 知识点2：容器字符串的遍历（有2种方法）
# 遍历：不重复的访问容器中的每一个元素
# 容器的遍历分正负索引，正负索引都支持
my_str='hello'
print(my_str[0])
print(my_str[3])
print(my_str[-5])
print(my_str[-1])
# 方法1：使用while循环进行遍历
i=0
while i<5:
    print(my_str[i])
    i+=1

# 方法2：使用for循环进行遍历
for a in my_str:
    print(a)

