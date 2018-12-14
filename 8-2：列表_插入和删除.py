# 创建一个空列表
my_list=[]

# 追加值— append，即在列表元素最后追加.且只能一个值一个值的追加。因为括号内只能填一个参数
my_list.append(12)
my_list.append(65)
my_list.append(87)
my_list.append(41)
my_list.append(20)
my_list.append(32)
my_list.append(19)

# 插入值—insert,在指定位置插入值。因此它有两个值，一个值指明位置，一个值是插入的数值
my_list.insert(1,20)
my_list.insert(3,30)
print(my_list)

# 删除列表—pop方法(位置删除)
# 不给它参数的话表示默认删除列表最后的那个元素.
my_list.pop()
print(my_list)
# 给予参数的话，就参数就表示指明要删除的位置
my_list.pop(2)
print(my_list)

# 删除列表—remove方法（值删除）
# 指定要删除的值
my_list.remove(41)
print(my_list)
# remove只能删除列表中第一次出现的值 （列表里有多个同样的值20）
my_list.remove(20)
print(my_list)

# 清空列表的值—clear
my_list.clear()
# 列表里的元素已被清空
print(my_list)
# 查出列表长度为0
print(len(my_list))

