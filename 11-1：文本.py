# 打开文本：r 、w 、a
# 1.read方法


def demo1():
    f=open("哈哈.txt","r")
    # read函数后面跟参数，表示读参数个数的字符
    content1=f.read(6)    # 选的属性是"r"，那么就要调用read方法啊
    # read函数后面不跟参数，表示读取整个文本内容
    # content2 = f.read()
    # readline函数表示读取一行
    content3=f.readline()
    content4 = f.readline()
    print(content1)
    # print(content2)
    print(content3)
    print(content4)
    f.close()
    # 小结：read函数读取后是会存储的，readline是接着之前读取内容后继续读取的

# 2.write函数:
# write写一行；    writelines写多行


def demo2():
    """2-1.write写一行，writelines写多行"""

    f=open("哼哼.txt","w")
    # write函数只写一行
    # content1=f.write("的个人格式如个人电饭锅")
    # writelines函数写多行，用列表的格式即可。列表内的每一个元素都表示一行。
    # 若文本中没显示换行，则是write函数中没写换行符\n
    content2=f.writelines(["qqqq\n","bbbb\n","dddd\n","pppp"])
    # print(content1)
    print(content2)
    f.close()
    # 小结：1.write模式下，添加的内容会将原本的文本内容覆盖掉
    #       2.若文本不存在，write模式还可以表示新建文本


# 3.如何让write函数的内容只换一行，而不是两行呢？
def demo3():
    f=open("dd.txt","w")
    content1=f.writelines(["活动经费\n","jenny\n","88888"])
    print(content1)
    f.close()
    g = open("dd.txt","r")
    content2=g.readlines()    # readlines函数结果打印出来的是列表类型的
    # content3=g.read()           # read函数结果打印出来的是文本类型的
    print(content2)
    # print(content3)
    g.close()

def demo4():
    # 要想把readlines函数结果列表类型的按行打印出来的话，可以用前面学到的for循环遍历的方法
    g = open("dd.txt", "r")
    lines=g.readlines()
    print(lines)
    for line in lines:
        print(line)

    # 问题：如何才能让后台打印只跨一行呢？
    # 分析：由于文本内容格式有换行，print也会换一行，所以遍历切片后的显示是换了2行的—用切片的思想
    for line in lines:
        if line[-1]=="\n":     # 程序中有写\n的，就进行切片操作，把程序中的\n切掉，不进行换行，只让print打印换行
            print(line[:-1])    # 左闭右开原则，-1位置的\n不包括在内
        else:                   # 程序中国没有\n的就直接打印
            print(line)



# 4.文本a模式，即在原有文本内容后追加
def demo5():
    f=open("哈哈.txt","a")
    content=f.write("\n房间房间看的反馈的")
    print(content)
    f.close()



# demo1()
# demo2()
# demo3()
demo4()

