"""
思路：
1.要确定好容器，列表嵌套列表还是字典嵌套字典？
由于该系统需要通过编号来进行筛选和修改等操作，所以只好是使用字典，将编号设为key即可
2.搭建好框架
（1）先要有系统操作菜单
（2）根据菜单选择操作，进入相应的系统功能（添加、修改、删除、查看员工信息等功能，以及推出系统）
3.细化具体内容
（1）系统是一个可以重复使用的，所以要用while循环
（2）每个系统功能里，要判断输入是否符合要求、实现功能等，会写很多代码，因此建议用外部定义函数的思想
"""
# 这个系统菜单是每次操作后都要见到的提示菜单，因此应放在主循环里

# 定义一个字典容器来储存员工信息
staff_sys={}    # 这样难道不算外部变量？怎么报错说它是局部变量呢？

# 将员工编号（key）转化为key列表。作为外部变量，方便后面使用


def menu():
    """ 显示系统菜单"""
    print("*" * 20 + "维京人员工管理系统" + "*" * 20)
    print("请根据您的需要选择您要进行的操作：")
    print("1.输入1表示进行添加员工操作")
    print("2.输入2表示进行修改员工操作")
    print("3.输入3表示进行删除员工操作")
    print("4.输入4表示进行查看员工操作")
    print("5.输入5表示进行退出系统操作")
    print("*" * 58)


# 1.添加员工信息的函数
def add():
    all_numbers = list(staff_sys.keys())
    number=input("请输入要添加的员工编号：")
    # 此处还要判断输入的编号是否已存在，因为编号作为员工存储里的key，是不能重复的
    # 1-1.如果输入的员工编号已存在，不能继续添加了并且提示“该编号已存在，添加失败”
    # 要判断员工编号是否重复，首先要去员工字典里去比对。那么就要获得员工字典里的key列表

    if number in all_numbers:
        print("该员工编号已存在，添加失败，请重试！")
        return  # 停止执行后续代码,函数中用return。
    # 1-2.如果输入的员工编号不存在，则进行后续添加操作
    staff_name = input("请输入要添加的员工的姓名：")
    staff_gender = input("请输入要添加的员工的性别：")
    staff_salary = input("请输入要添加的员工的工资：")
    print("新增员工%s已加入维京人管理系统！"%staff_name)
    # 此处就可以看出我占位符这一章节没学好！

    # 1-3：将员工信息保存在字典中:
    # 1-3-1：将员工编号作为键，剩下信息作为值.先将输入的员工信息拼接成字典
    # 1-3-2：格式内容：1001：{"name":"xxx","gender":"xxx","salary":"xxx"}


    staff_info={"name":staff_name,"gender":staff_gender,"salary":staff_salary}



   #  1 - 4：将员工信息添加到员工系统储存里
   #  员工系统储存格式内容：1001：{"name": "xxx", "gender": "xxx", "salary": "xxx"}

    staff_sys[number]=staff_info       # number是键，staff_info(员工信息）是值，组成的键值对

# 问题：如何将新增的信息加入staff_sys里？



# 2.修改员工信息的函数
def revis():
    # 2-1.要修改员工的信息，首先要先获得它以前的信息，如何从字典容器中获得？
    # 是通过员工编号来查找数据的，编号是key，因此还涉及判断编号是否重复。通过之前学的字典的遍历，来获取相应的数据
    number=input("请输入要修改的员工编号：")
    all_numbers = list(staff_sys.keys())
    if number not in all_numbers:
        print("该员工编号不存在，请重试！")
        return
    # 2-2.先显示出原始的内容，再做修改。（直接回车表示不修改）
    # 展示出该编号的原始内容。关于字典特性：针对已有的信息就是修改；没有的内容就是添加。
    # all_numbers[0] = input("该编号的员工姓名为%s，现将改为：" % all_numbers[0])
    # all_numbers[0] = input(" ")
    new_name=input("该员工的姓名是：%s，现将修改为："%staff_sys[number]["name"])
    new_gender = input("该员工的性别是：%s，现将修改为：" % staff_sys[number]["gender"])
    new_salary = input("该员工的薪资是：%s，现将修改为：" % staff_sys[number]["salary"])

    # 直接回车表示不修改，需进行判断.将修改的信息录入储存系统
    # 点评：此处存在问题，按回车后原始数据都不存在了。变成空的了—找到原因了，是因为我理解的空是要在“”内按空格的。其实是直接“”就行了
    if new_name !="":
        staff_sys[number]["name"]=new_name
    if new_gender !="":
        staff_sys[number]["gender"] = new_gender
    if new_salary !="":
        staff_sys[number]["salary"] = new_salary
    print("员工编号为%s的信息修改成功！"%number)

    # 点评：1.难道之前报错是由于我使用了if、elif、else语句？
    # 2.还有不能把all_numbers = list(staff_sys.keys())放在函数外面作为全局变量么？
    # 3.不能在函数中使用""""""作为注释么？



# 3.删除员工信息的函数
def amputate():
    # 3-1.要求输入要删除的员工编号
    all_numbers = list(staff_sys.keys())
    number = input("请输入要删除的员工编号：")
    # 3-2.判断输入的编号，该系统储存里是否存在
    if number in all_numbers:
        del staff_sys[number]
        # 3-3.根据编号进行删除，并提示删除成功
        print("编号为%s的员工信息已删除！"%number)
    else:
        print("该员工编号不存在，请重试！")
        return

# 4.查看员工信息的函数
def check():
   # 4-1.选择“查看”指令后，展示系统里的所有员工信息.打印键值对就是员工的信息了
   #  print({"staff_sys[staff_number]":"staff_info"})
   # 4-2.其实就是对存储容器字典的遍历
    for empolyee in staff_sys.items():
        # staff_sys = {"number": {"name": staff[0], "gender": staff[1], "salary": staff[2]}}
        # 点评：这种思路错误点在于对存储容器的理解还是不到位，是字典嵌套字典。编号作为key，value信息全都放在了字典里
        # 遍历的时候我们是以最外层的字典往内的，因此先找到key和value，在进value那个字典里找键值对
         print("%s\t%s\t%s\t%s" %(empolyee[0],empolyee[1]["name"],empolyee[1]["gender"],empolyee[1]["salary"]))

    # 点评：\t相当于tab键，记得是往左的斜杠，别搞反了


while True:

    # 系统菜单展示也可以写成函数,调用就行了
    menu()

    # 系统的功能。选择操作指令:
    operate=(input("请输入您选择的操作序号："))      # 输入操作指令后没反应，原来问题出在这儿了。类型不一样，无法执行后续操作
    if operate =="1":
        # 将这里面的具体内容写成函数，在此调用就行
        # 添加员工信息
        add()
        print(staff_sys)   # 打印员工信息
    elif operate=="2":
        # 修改员工信息—调用函数
        revis()
        print(staff_sys)
    elif operate=="3":
        # 调用函数
        amputate()
        print(staff_sys)
    elif operate=="4":
        check()

    elif operate=="5":
        print("您已退出维京人员工管理系统！")
        break    # 退出系统了，当然也得退出这个循环了啊
    else:
        print("你输入的操作指令有误，请重新输入！")










