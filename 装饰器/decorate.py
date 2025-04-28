#函数的嵌套

#
# def hi(name="yasoob"):
#     print("now you are inside the hi() function")
#
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     print(greet())
#     print(welcome())
#     print("now you are back in the hi() function")
#
#
# if __name__ == '__main__':
#     hi()

#从函数中返回函数

# def hi(name="yasoob"):
# #     def greet():
# #         return "now you are in the greet() function"
# #
# #     def welcome():
# #         return "now you are in the welcome() function"
# #
# #     if name == "yasoob":
# #         return greet
# #     else:
# #         return welcome
# #
# # if __name__ == '__main__':
# #     a = hi("sd")
# #     print(a)
# #     print(a())

#装饰器范例
# from functools import wraps
#
# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# @decorator_name
# def func():
#     return ("Function is running")
#
# if __name__ == '__main__':
#
#     can_run = True
#     print(func())
# # Output: Function is running
#
#     can_run = False
#     print(func())
# # Output: Function will not run

#装饰器日志的应用

# from functools import wraps
#
#
# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#     return with_logging
#
#
# @logit
# def addition_func(x):
#     """Do some math."""
#     return x + x
# if __name__ == '__main__':
#
#     result = addition_func(4)
# # Output: addition_func was called


#
"""
装饰器的使用场景
函数执行时间的统计
输出日志信息
1.装饰器实现已有函数执行时间的统计
"""
# import time
# #
# # # 装饰器函数
# def get_time(func):
#     def inner():
#         begin = time.time()
#         func()
#         end = time.time()
#         print("函数执行花费%f秒" % (end-begin))
#     return inner
#
# @get_time
# def func1():
#     for i in range(100000):
#         print(i)
# if __name__ == '__main__':
#     func1()


"""1.装饰带有参数的函数"""

#添加输出日志的功能
# def logging(fn):
#     def inner(num1, num2):
#         print("--正在努力计算--")
#         fn(num1, num2)
#         print("--计算结束--")
#     return inner
#
# # 使用装饰器装饰函数
# @logging
# def sum_num(a, b):
#     result = a + b
#     print(result)
# if __name__ == '__main__':
#
#     sum_num(1, 2)

# """2.装饰带有返回值的函数"""
#添加输出日志的功能
def logging(fn):
    def inner(num1, num2):
        print("--正在努力计算--")
        result = fn(num1, num2)
        return result
    return inner

#使用装饰器装饰函数
@logging
def sum_num(a, b):
    result = a + b
    return result
if __name__ == '__main__':

    result = sum_num(1, 2)
    print(result)

"""3.装饰带有不定长参数的函数"""

# 添加输出日志的功能
# def logging(fn):
#     def inner(*args, **kwargs):
#         print("--正在努力计算--")
#         fn(*args, **kwargs)
#         print("--结束努力计算--")
#     return inner
#
# # 使用语法糖装饰函数
# @logging
# def sum_num(*args, **kwargs):
#     result = 0
#     for value in args:
#         result += value
#
#     for value in kwargs.values():
#         result += value
#
#     print(result)
# if __name__ == '__main__':
#     sum_num(1, 2, a=10,b=3)


"""通用装饰器的语法格式"""
    # 通用装饰器
    # def logging(fn):
#     #     def inner(*args, **kwargs):
#     #         print("--正在努力计算--")
#     #         result = fn(*args, **kwargs)
#     #         return result
#     #
#     #     return inner


# """多装饰器的运用，就近原则修饰"""
# def make_div(func):
#     """对被装饰的函数的返回值 div标签"""
#     def inner(*args, **kwargs):
#         return "<div>" + func() + "</div>"
#     return inner
#
# def make_p(func):
#     """对被装饰的函数的返回值 p标签"""
#     def inner(*args, **kwargs):
#         return "<p>" + func() + "</p>"
#     return inner
#
#
# # 装饰过程: 1 content = make_p(content) 2 content = make_div(content)
# # content = make_div(make_p(content))
# @make_div
# @make_p
# def content():
#     return "人生苦短"
# if __name__ == '__main__':
#     result = content()
#     print(result)
#  #结果 <div><p>人生苦短</p></div>


"""带有参数的装饰器"""

# 添加输出日志的功能
# def logging(flag):
#
#     def decorator(fn):
#         def inner(num1, num2):
#             if flag == "+":
#                 print("--正在努力加法计算--")
#             elif flag == "-":
#                 print("--正在努力减法计算--")
#             result = fn(num1, num2)
#             return result
#         return inner
#
#     # 返回装饰器
#     return decorator


# 使用装饰器装饰函数
# @logging("+")
# def add(a, b):
#     result = a + b
#     return result
#
#
# @logging("-")
# def sub(a, b):
#     result = a - b
#     return result
#
# if __name__ == '__main__':
#     result = add(1, 2)
#     print(result)
#
#     result = sub(1, 2)
#     print(result)
#     # --正在努力加法计算 - -
#     # 3
#     # --正在努力减法计算 - -
#     # -1


#类装饰器
#就是通过定义一个类来装饰函数。
# class Check(object):
#     def __init__(self, fn):
#         # 初始化操作在此完成
#         self.__fn = fn
#
#     # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
#     def __call__(self, *args, **kwargs):
#         # 添加装饰功能
#         print("请先登陆...")
#         self.__fn()
#
#
# @Check
# def comment():
#     print("发表评论")
# if __name__ == '__main__':
#     comment()