# 难得再写这么多注释了，直接写成函数，要用就调用
def demo1():             # python里尽量不要用test来定义函数、取名等，不然无法运行
    """1.关于字典的定义 — 用的大括号"""
    # 键和值之间用：隔开。 键和值组成对，每对之间用，隔开
    my_dict={"name":"jenny","age":"26","gender":"女"}
    # key,即关键字。 value，值。键是唯一的，不能重复。值可以重复
    print(my_dict["gender"])
    print(my_dict["name"])
demo1()


def demo2():
    """2.字典不支持索引，也不支持切片"""
    my_dict={"name":"jenny","age":"26","gender":"女"}
    # print(my_dict[1])
    # print(my_dict[0:])
demo2()


def demo3():
    """3.获得字典的值"""
    my_dict={"name":"linda","grade":"senior2","score":99}
    print(my_dict["grade"])    # 这不是索引，是根据关键字查找获取值的
    # 使用只看哈这种方式访问字典中的元素没如果键不存在则会报错，程序终止。
    # print(my_dict["hobby"])
    # 使用get方法，如果key不存在默认返回None，也可以指定默认返回值。
    print(my_dict.get("hobby"))   # 键hobby不存在，默认返回值是None
    print(my_dict.get("age","年龄是女生的秘密啦"))   # 指定默认值
demo3()


def demo4():
    """4.字典的新增和修改"""
    my_dict={'name':"john","age":28,"gender":"man","job":"manager"}
    print(my_dict)
    # 如果key存在的话，则是修改
    my_dict["age"]=18   # age是字典里原有的，即此处则为修改
    # 如果key不存在的话，则是添加
    my_dict["hobby"]="read"  # hobby是字典里没有的元素，则此处为新增
    print(my_dict)
demo4()


# 5.字典的删除
my_dict={'name':"Marry","age":23,"gender":"famle","job":"student"}
#  del 即delete，删除。 一般删除的是键值对
del my_dict["name"]
print(my_dict)

# 清空字典—clear方法
my_dict.clear()
print(my_dict)


# 附：del的作用

# del 还可以删除变量
a=10
print(a)
del a    # 删除变量a后，由于变量a不存在了，第59行代码会报错
# print(a)

# del 删除列表中的元素
my_list=["aaa",50,0.55]
del my_list[0]
print(my_list)
