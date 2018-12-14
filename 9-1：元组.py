# 知识点1：如何一个定义元组？用小括号
my_tuple=(10,20,30)      # “元组”的英语单词：tuple

# 元组里的元素数据不支持修改!

# my_tuple[1]=888  # 将元组里的下标为1位置上的元素20修改值为888
 # print(my_tuple)     报错提示“ 'tuple' object does not support item assignment”—元组不支持修改

# 元组也是序列容器，因此也支持下标索引、切片、遍历等

# 查询
pos=my_tuple.index(30)  # 查询元素30这个值是在改元组的哪个下标位置上
print(pos)

# 切片
vol=my_tuple[1:]
print(vol)

# 遍历
for a in my_tuple:
    print(a)

# 元组里只有一个元素的，后面要加个，    不过在我这个Python编译器里好像不需要
my_tuple=(10)
print(my_tuple)

# 元组可以嵌套
my_tuple=((666,888),(999,777))
print(my_tuple)