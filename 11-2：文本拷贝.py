# coding:utf-8
# 原封不动的拷贝一个文件，不能涉及格式转换——因此要用二进制
# 思路分析：
# 1.获取要拷贝的原文件名（老文件）
old_name=input("请输入要复制的文件名：")
# 2.拼写复制后的文件的名字（新文件）
# 2-1.将截取老文件.txt前面部分的文件名，加入[副本]这种格式。因此需要用切片
position=old_name.rfind(".")
# print(position)
# 拼接复制后的文本名儿
# new_name=old_name[:position]+"副本"+".txt"     # 此处考虑的不够全面，文本后缀不一定都是TXT啊，还有可能是PDF等等
# 最好是对.定位做一个判断，如果.的位置>0，那么应截取老文件名.前后面的内容，中间加上“副本”进行拼接
# 如果.的位置不是>0的，那么表示没有.（可能是隐藏了后缀的），这种情况就直接老文件名+副本即可
if position>0:
# 获得老文件名.前面部分内容
    front=old_name[:position]
# 获得老文件名.后面部分内容
    back=old_name[position+1:]
    new_name=front+"副本."+back
else:
    new_name=old_name+"副本"
# 3.打开新老文件
old_file=open(old_name,"rb")  # 要用二进制格式进行拷贝，这样才是完全的复制，不涉及格式转换
new_file=open(new_name,"wb")
# 4.将老文件内容写到新文件里
new_file.writelines(old_file)       # 这两种写法的效果是一样的。不写明.Readlines，其实就是文本的所有内容
# new_file.writelines(old_file.readlines())  # 写了.Readlines，所有行，不就是文本的所有内容嘛
# 5.关闭新老文件
old_file.close()
new_file.close()

