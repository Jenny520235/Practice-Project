# 练习题目：一个学校，有3个办公室，现在又8位老师等待工位分配。请编写程序完成随机分配
"""
思路分析:
1.一个学校是一个列表容器，里面再套3个办公室列表，再将老师分随机配进3个办公室
"""
# 定义一个学校的空列表：
school=[[],[],[]]
# 定义一个列表来保存老师
teacher_list=[]
# 将8个老师进行编号，若命名为老师1、老师2...以此类推，可以看出格式：“老师”后面的后缀数值增大了。
# 因此可以使用while循环

"""
方法1：

i=1
while i<9:
    # 将老师编号
    teacher_name=("老师"+str(i))  # i是数字类型的，“老师”是字符串类型的。两者不能自己相加，因此需要转换
    # 将老师随机放入老师列表里
    teacher_list.append(teacher_name)
    i+=1
print(teacher_list)
"""

import random
# 方法2：写成一个函数
def creat_techer():
    # 这个是在函数的内部。这个函数的结果，在函数外部是不能使用的
    i = 1
    while i < 9:
        teacher_name = ("老师" + str(i))
        teacher_list.append(teacher_name)
        i += 1
    # 因此需要把函数的结果return给一个变量，方便在函数外部调用该结果；
    return teacher_list
teachers_list=creat_techer()   #teachers_list是一个列表变量，用于接收函数create_teacher的返回结果
print(teachers_list)


"""
思路：
1.将3个办公室随机放入学校列表里；
2.再将老师放入办公室列表里；
3.先遍历学校列表，获得3个随机的办公室列表，再对办公室列表里的老师进行遍历。这样就能实现需求了
"""

# 在学校列表里对办公室进行随机标号（涉及随机数，要引入函数random)

# 分配老师
for teacher in teachers_list:   # 对老师列表进行遍历，把老师一个个取出来
    # 对3个办公室进行随机标号
    office_number=random.randint(0,2)   # 这儿的随机数居然必须要从0开始，否则会报错
    # 给老师随机分配办公室
    school[office_number].append(teacher)

# 先遍历学校列表，获得3个随机的办公室列表，再对办公室列表里的老师进行遍历。
for office in school:
    # 从办公室列表刷选老师这个for循环遍历的一个
    for person in office:
        print(person,end=" ")  # end里面留个空格，打印也会有空格
    print()



