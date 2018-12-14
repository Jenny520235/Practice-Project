"""
return在函数中的作用：
1. 函数返回值的return语句
2. 函数执行到return就会终止（一个函数中可以出现多个return,但有且只有一个return会被会被执行）
"""
def demo(start,end):
    # 以这个练习为例，我们需要对这个函数的参数进行校验，看是否符合代码执行的条件。因此有时候需要进行多个条件的校验
    # 校验条件1：
    # start 和 end都应该是数字
    is_int = isinstance(start,int)
    if not is_int:
        print("start应该是一个数字")
        return
    # 校验条件2：
    if start > end:
        print("start应该小于end的值！")
        return None
    is_int = isinstance(end,int)
    if not is_int:
        print("end应该是一个数字")
        return None
    i=start
    result=0
    while i <=end:
        result += i
        i += 1
    return result
ret=demo(500,100)
print("ret：",ret)
ret=demo("#",100)
print("ret：",ret)