# and   or   not语法
# 应用and   or   not语法简化之前if-分支语句练习的代码
# 获取用户输入的账号和密码：
input_name = input("请输入您的账号：")
input_passport = input("请输入您的密码：")
# 进行if-else判断
if input_name == "admin" and  input_passport == "123456":
    print("欢迎使用亲朋棋牌系统！")
else:
    print("您输入的账号或密码有误，请重新输入")


#  非0为真，0为假。
a=15
b=30
ret = a>b and a or b
print(ret)
# and的优先级高于or。
# 此处先看a>b and a，a>b为假，那么a>b and a即为假
# ret = false or b，那么输出结果为b

ret = a<b and a or b
print(ret)
# 先判断a<b and a，a<b为真，那么a<b and a久要判断a，a=15非0即为真，输出结果是a的值
# 经上一步的判断后，则ret = a or b。再进行判断a or b，a为真，因此ret = a<b and a or b的最终输出值应该是a的值
