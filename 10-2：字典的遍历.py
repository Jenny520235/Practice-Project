# 字典的遍历需要转换，将字典的内容转换成列表格式后在进行遍历
my_dict={'name':"Marry","age":23,"gender":"famle","job":"student"}
# for v in my_dict:       直接用for循环来遍历字典，只有键，没有值
#     print(v)
# 将键转化成列表格式，有专门的转化方法keys
key_list=list(my_dict.keys())   # 将转化后的键列表定义为key_list
# 这还不算真正的列表格式，因此还需要转化类型。如以前学的将字符串转换为int类型。同理
print(key_list)

# 同上的思路，也可以将键值转化成列表格式
value_list=list(my_dict.values())   # 也是要将其进行类型转换
print(value_list)

# 现已获得了键、值的列表，但是是2个分开的列表，如何合并成一个列表呢？
# 专用方法items（项目），将键、值列表合并为一个键值对列表
# 直接使用items方法即可将字典转换为键值对列表（上述获得键列表、值列表是为了让你了解）
key_value_list=list(my_dict.items())
print(key_value_list)

# 字典已转换为键值对列表（其实是元组），即可进行遍历了
# 方法1：for循环遍历
for val in key_value_list:
    # print(val)  #这样得到的是列表里的键值对
#   如果想将列表中的每个元素遍历出来的话，则将上一步遍历出来的键值对再根据索引打印出来
    print("key:",val[0],"value:",val[1])


# 方法2：while循环遍历
i=0
while i<len(key_value_list):
    # print(key_value_list[i])   #这种方式获得的是列表的键值对
    # 通过上一步的理解，再将键、值取出来就很容易了
    print("key:",key_value_list[i][0],"value:",key_value_list[i][1])
    i+=1

