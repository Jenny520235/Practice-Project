# 知识点1：了解列表的定义
# 如何定义一个列表
my_list=[]               # 这种是空列表
my_list=[10,20,30]       # 数字列表
my_list=["hello","good","prety"]       # 字符串类型的列表

# 知识点2：列表的遍历
# 方法1：while循环进行遍历
my_list=["hello","good","prety"]
index=0
while index<len(my_list):
    print(my_list[index])
    index+=1

# 方法2：for循环遍历
for ha in my_list:
    print(ha)

# 练习2：复杂的嵌套式遍历—想要获得里面每个列表的值
my_list=[[10,20,30],["good","morning","bests"],[3.14,7.68,9.25]]

# 方法1：while循环进行遍历
# 第一步：先遍历my_list这个总的列表，获得里面的3个列表元素
a=0
while a<len(my_list):
    # 第二步：再对里面的列表进行遍历，获得内部列表的每个元素
    b=0
    while b<len(my_list[a]):
        print(my_list[a][b])
        b+=1
    # print(my_list[a])
    a+=1

# 方法2：for循环进行遍历
for val in my_list:
    # print(val)   先遍历my_list这个总的列表，获得里面的3个列表
    for do in val:   # 再从子列表里遍历出其中的元素
        print(do)