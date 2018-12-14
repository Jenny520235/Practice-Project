# 员工管理系统简易版V1.0
"""
1.展示系统列表内容；
2.新增一个员工信息；
3.修改一个员工信息；
4.删除一个员工信息；
5.退出系统；
"""
# 抬头
print("欢迎进入亲朋员工管理系统！")
print("*"*10 +"亲朋员工管理系统" +"*"*10)
# 从这个位置加入while循环
while True:
    # 分割线
    print("*"*35)
    # 展示系统列表内容；
    print("1.展示所有员工信息；")
    print("2.新增一个员工信息；")
    print("3.修改一个员工信息；")
    print("4.删除一个员工信息；")
    print("5.退出员工管理系统；")
    # 分割线
    print("*"*35)
    # 保存用户输入操作
    operation=int(input("请输入您的操作:"))
    if operation==1:
        print("张三，男，26岁")
        print("李四，女，19岁")
        print("王子，男，42岁")
    elif operation==2:
        # new_woker=input("请输入要新增员工的信息(输入格式按姓名，性别，年龄依次输入):")
        # print("新增员工的信息是：",new_woker)
        name=input("请输入新增员工的姓名：")
        gender=input("请输入新增员工的性别：")
        age=input("请输入新增员工的年龄：")
        print("新员工%s已添加到亲朋员工系统！" %name)
    elif operation==3:
        new=input("请输入要修改员工的信息(输入格式按姓名，性别，年龄依次输入):")
        print("修改后的员工信息是：",new)
    elif operation==4:
        delete=input("请输入你要删除的员工名字：")
        print("%s的员工信息已删除！"%delete)
    elif operation==5:
        print("您已退出亲朋员工管理系统，欢迎下次使用！")
        break
    else:
        print("您的输入有误，请重新输入！")
# 点评：一个简易的系统已完成，但却只能使用一次。因此需要用到while循环



