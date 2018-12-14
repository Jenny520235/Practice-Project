"""
编写系统的强化练习：
需求：
1.按学生学号进行统计，涉及学生姓名，语数外3科的成绩
2.该系统也要有增删改查功能
"""

# 步骤1：定义该管理系统的储存容器
students={}
# 下面的函数都涉及到学号判断是否存在的问题，因此将系统储存容器的key值全部取出定义为一个变量，方便后续判断
students_number = students.keys()  # 不能用list(students.keys()），为什么呢？

# 步骤2：定义系统涉及的功能函数
def menu():
    """1.系统菜单"""
    # 要把该菜单放入系统操作循环里。因此可以将其定义成函数，再在while循环里调用即可
    print("*"*10+"欢迎进入合江中学学生成绩管理系统"+"*"*10)
    print("系统菜单说明：请根据以下选项进行您需要的操作")
    print("1.输入1进行添加学生信息的操作")
    print("2.输入2进行删除学生信息的操作")
    print("3.输入3进行修改学生信息的操作")
    print("4.输入4进行查看学生信息的操作")
    print("5.输入5进行退出管理系统的操作")
    print("*"*50)

# 步骤4：while循环中的系统操作具体功能细化，以函数的形式表达出来，然后在while循环中调用即可
def add():
    """2.添加学生信息"""
    number=input("请输入要添加的学生学号：")
    # 判断输入的学号储存系统是否存在
    # 2-1.存在则提示错误.还要涉及到获取储存容器的key值
    if number in students_number:
        print("该学号已存在，添加失败！")
        return   # 函数中终止后续代码执行用return
    else:
        # 2-2.不存在则进行添加内容操作
        s_name=input("请输入要添加的学生姓名：")
        s_Chinese=input("请输入要添加的学生语文成绩：")
        s_math=input("请输入要添加的学生数学成绩：")
        s_English=input("请输入要添加的学生英语成绩:")
        print("学号为%s的学生信息已添加成功！"%number)
        # 将获得的数据录入储存容器里
        # 储存格式是：{"number":{"name":xxx,"chinese":xxx,"math":xxx,"English":xxx}}
        # 先拼value的值，即{"name":xxx,"chinese":xxx,"math":xxx,"English":xxx}
        student_info={'name':s_name,"chinese":s_Chinese,"math":s_math,"English":s_English}
        students[number]=student_info
        print(students)


def remove():
    """3.删除学生信息"""
    number=input("请输入要删除的学生学号：")
    # 判断该学号是否存在
    # 3-1.如果存在，则进行删除操作，删除完成后给予提示
    if number in students_number:
        del students[number]
        print("学号为%s的学生信息已删除！"%number)
    else:
        print("该学号不存在，删除失败！")
        return


def revise():
    """4.修改学生信息"""
    number = input("请输入要修改的学生学号：")
    # 判断该学号是否存在
    # 3-1.如果存在，则进行删除操作，删除完成后给予提示
    if number not in students_number:
        print("该学号不存在，修改失败！")
        return
    else:
        # 先将要修改的学号对应的学生信息一一显示，然后让用户进行修改操作
        new_name=input("该学生的姓名是：%s,现修改为："%students[number]["name"])   # 点评：这儿要用students[number]["name"]，不能是students[1]["name"]
        new_chinese=input("该学生的语文成绩是：%s,现修改为："%students[number]["chinese"])
        new_math = input("该学生的数学成绩是：%s,现修改为：" % students[number]["math"])
        new_English= input("该学生的英语成绩是：%s,现修改为：" % students[number]["English"])
        # 将修改后的数据录入储存容器。用户直接回车表示不修改，因此需要判断
        if new_name !="":
            students[number]["name"]=new_name
        if new_chinese !="":
            students[number]["chinese"]=new_chinese
        if new_math !="":
            students[number]["math"]=new_math
        if new_English !="":
            students[number]["English"]=new_English
        print("学号为%s的学生信息已修改成功！"%number)


def check():
    """5.查看学生信息"""
    # 要想查看容器的数据，最快捷的方式就是遍历啊
    # for student in students:   点评：字典的遍历是需要先将其转换成列表的！
    for student in students.items():
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s"%(student[0], student[1]["name"], student[1]["chinese"], student[1]["math"], student[1]["English"]))
        # 少了一个反括号就导致整个系统报错了，还是要仔细啊！

    # 看来还是没掌握啊
    # print("%s\t%s\t%s\t%s\t%s",%(students[number],students[number]["name"]),students[number]["chinese"],students[number]["math"],students[number]["English"])


# 步骤3：搭建系统操作的while循环框架
while True:
    menu()  #  调用系统菜单函数
    # 根据用户输入的操作指令进行系统流程
    operate = input("请输入您的要选择的操作编号：")

    if operate=="1":
        add()
    elif operate=="2":
        remove()
    elif operate=="3":
        revise()
    elif operate=="4":
        check()
    elif operate=="5":
        print("您已退出合江中学学生成绩管理系统！")
        break
    else:
        print("您的输入有误，请重新输入！")
