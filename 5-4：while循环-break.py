# break关键字
# break关键字在while循环中的作用：终止循环
# 练习1：while循环的示例
index=1
while index<=5:
    if index==4:     # 增加要求：当index=2时，终止循环
        break
    print("*"* index)
    index+=1

# 拓展：while循环里还能嵌套while循环，一般常用的是2层while循环嵌套。

# 示例：while循环嵌套
a=1
while a<=4:
    b=0
    while b<=5:
        if b==3:
           break     # 增加要求：当b=2时，终止循环(break关键字在while循环中的应用)
           #continue   # 跳过本层循环里的本次循环
        print(b)
        b+=1
    a+=1
"""
c=0
while c<=3:
    d=0
    if c == 2:
        break  # 增加要求：当d==3时，跳过循环(continue关键字在while循环中的应用)
        # continue
    while d<=4:
        print(d )
        d +=1
    c+=1
"""
