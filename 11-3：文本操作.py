#-*- coding:utf-8 -*-
# 1.涉及文本的重命名、创建和删除、获得文件的当前目录、获得文件当前目录的列表、切换文件目录位置
# 首先要导入OS方法
import os
def demo1():
    """文件重命名和文件删除"""
    os.rename("开心就好","gxp.txt")
    os.remove("perfect副本.txt")


def demo2():
    """创建和删除文件目录"""
    # os.mkdir("intresting.txt")
    os.mkdir("romantic")
    os.rmdir("intresting.txt")

def demo3():
    """获得文件当前目录的列表"""
    content=os.listdir()
    print(content)

def demo4():
    """获得文件的当前目录和切换工作目录位置"""
    # 方法1：直接把文件夹创建在期望的位置（写绝对路径）—用创建文件夹的方式
    # 方法2：找到要切换的文件夹，修改文件夹的位置
    cwd=os.getcwd()    # 这样原来是没打印，得定义个变量去接收
    print(cwd)         # cwd的全称：current working directory，即当前工作目录的意思。os的操作都是默认在当前目录下操作的。
    # 切换当前工作目录到桌面路径
    os.chdir("C:\\Users\甜甜\Desktop")
    os.mkdir("888")    # 如何通过python编译器在桌面创建一个文件夹？那就得先把当前操作路径切换到桌面目录去，然后再测创建文件夹不就OK了嘛
# demo1()
# demo2()    # 文件夹是不会重复新建的
demo3()
demo4()