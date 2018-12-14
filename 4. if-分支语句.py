# if和else语句，其实跟之前学C#是的语法是一样的.
# 获取用户输入的账号；
name = input("请输入您的账号:")
# 获取用户输入的密码；
PS =input("请输入您的密码：")
#  练习:正确的密码。此练习还涉及到变量类型的转换。1.要么将PS获取到的内容转换成int类型； 2.要么将passport赋值成字符串类型；
# 这就是此处passport的赋值"123456"为什么要加引号的原因
# 正确的账号
user_name = "admin"
# 正确的密码
possport = "123456"
# if分支语句的应用：若用户输入的密码是123456，则登录成功。输入的不是123456则提示
# 判断获取到的账号与正确的账号是否一致；
if name == user_name:
 #    如果账号正确，再判断密码是否正确；
 if PS == possport:
  print("欢迎进入亲朋棋牌系统")
 else:
    print("您输入的账号或密码有误，请重新输入")
else:
 print("账号或密码错误，请重新输入")
# 点评：代码14-21行，涉及if判断语句的嵌套。python编译器对if-else的缩进要求很严格。
# 里面判断密码是否正确的if-else代码块和外面的if-else代码块存在缩进。要明显的区分出来。两组if-else全部靠最左边的话，会出现报错。

# and   or   not语法
# 应用and   or   not语法简化上面的代码
# 获取用户输入的账号和密码：
input_name = input("请输入您的账号：")
input_passport = input("请输入您的密码：")
# 进行if-else判断
if input_name == "admin" and  input_passport == "123456":
    print("欢迎使用亲朋棋牌系统！")
else:
    print("您输入的账号或密码有误，请重新输入")
