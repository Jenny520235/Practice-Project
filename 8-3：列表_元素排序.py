# 知识点1：如何在列表里产生随机数
# 需求:创建一个包含10个随机数的列表
# 第一步：创建一个空列表
my_list=[]
# 第二步：产生10个数字 — 用while循环生成10个数字
i=0
while i<10:    # i包含了0的，从0开始数到9刚好是10个数字
    # 第三步：要产生随机数，需引入函数random
    import random
    random_number=random.randint(1,100)  # 定义随机数的范围1—100
    # print(random_number)
    # 第四步：将生成的10随机数放入列表里—由于之前是空列表，没顺序要求，采用追加的方式append
    my_list.append(random_number)  # 看来追加也得放在while循环中，这样列表才能加入10个值。
    i+=1                           # 在while循环外的话，列表内只有一个值
print(my_list)


# 知识点2：对列表里的元素进行排序
# 引入排序方法sort.默认是按升序排序的（由小到大）.
# 因为sort里面的参数reverse（颠倒的意思）默认值是false，即不颠倒—升序
my_list.sort()
print(my_list)
# 如何让列表里的元素值按降序排列呢？ 将sort里的参数reverse=true即可
my_list.sort(reverse=True)
print(my_list)

# 逆序—把列表元素颠倒顺序，不会进行数值大小的排列。跟my_list[::-1]是一个效果的
# 调用方法reverse（颠倒），即把元素颠倒过来排列
my_list.reverse()
print(my_list)