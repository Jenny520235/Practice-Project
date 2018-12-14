# 应用if语句实现分数等级划分的案列
# 思维分析：
"""
1.获取用户输入的分数
2.将用户输入的值由str类型转换成int类型
3.分数等级划分：
（1）90-100  A等级
（2）80-90   B等级
（3）70-80   C等级
（4）60-70   D等级
（5）60以下  E等级
（6）错误输入：>100或负数、小数、中文、符号等
"""

# 获取用户输入的分数
score = input("请输入您的分数：")
# 将用户输入的值由str类型转换成int类型
int_score = int(score)
# 分数等级划分：
if int_score>=90 and int_score <=100:
    print("你太棒了！")
elif int_score>=80 and int_score<90:
    print("良好")
elif int_score>=70 and int_score<=80:
    print("中等")
elif int_score>=60 and int_score<70:
    print("及格")
elif int_score>=0 and int_score<60:
    print("不及格，你完了！")
else:
    print("输入错误！")


# 上面的代码优化+简化版：更简洁明了，代码可读性更强
score = int(input("请输入您的分数："))
# 先定义好分数的范围：0-100之间，输入这个区间以外的值都是错误的。
if score>=0 and score<=100:
    # 在定义的分数区间内划分等级
    if score>=90 and score<=100:
        print("优秀！")
    elif score>=80 and score<90:
        print("良好")
    elif score>=70 and score<80:
        print("中等")
    elif score>=60 and score<70:
        print("及格")
    else:
        print("不及格！")

else:
    print("输入有误，请重新输入！")

