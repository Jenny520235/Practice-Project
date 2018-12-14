my_list=[16,25,78,96,31]
print(my_list)
# 知识点1：查找其中一个元素
# 引入index方法。讲解：如果能查找到该值，即会打印出它所在位置。若不存在则会报错
result=my_list.index(31)   # 傻不傻：当你不晓得怎么打印出它的时候，就说明你改重新定义一个变量来接收这个结果了
print(result)

# 拓展：值经常在变，需要修改的这种情况就可以直接将它定义成一个变量
# 知识点2：修改列表中元素的值
old=25
new=8000
# 思路：先找到要修改的值的位置，然后将其修改
# 查找位置，需进行校验。因为该值不在列表中则会报错
if old in my_list:
    # 先判断值是否在列表中，如果在的话查询它的位置。
    wos=my_list.index(old)
    # 找到old的位置后，对这个位置上的数值进行修改
    my_list[wos]=new
print(my_list)


# 知识点2：将一个列表追加到当前列表的尾部。需引入方法extend
my_list1=[10,20,30,40]
my_list2=[111,222,333,444]
my_list1.extend(my_list2)
print(my_list1)