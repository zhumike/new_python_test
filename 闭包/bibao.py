# print_msg是外围函数
# def print_msg():
#     msg = "I'm closure"
#
#     # printer是嵌套函数
#     def printer():
#         print(msg)
#
#     return printer
# if __name__ == '__main__':
#
# # 这里获得的就是一个闭包
#     closure = print_msg()
# # 输出 I'm closure
#     closure()
# coding='uft-8'
"""闭包的特殊用途：
    1.可以在不修改现有功能源码的前提下，增加新功能
    日志功能（统计访问事件，访问功能，写到日志文件中），权限验证（下载之前验证当前账户是否为会员）
    开闭原则：开放：添加功能（可以）
            关闭：修改源代码（不可以）
"""
# import time
# #定义一个记录日志的函数：将访问时间和访问的函数名写入文件中（log.txt）
# def writeLog(func):
#     try:
#         file = open('log.txt','a')
#         #写入相关数据信息（访问的函数名，访问时间）
#         #写入访问的函数名
#         file.write(func.__name__)
#         file.write('\t')
#         #写入访问时间
#         file.write(time.asctime())
#         #换行
#         file.write('\n')
#     except Exception as e:
#         print(e.args)
#     finally:
#         #关闭文件
#         file.close()
# #闭包
# def funcOut(func):
#     def funcIn():
#         #新增功能
#         writeLog(func)
#         func()
#     return funcIn
#
#
# def func1():
#     print('我是功能1')
# def func2():
#     print('我是功能2')
#
#
# if __name__ == '__main__':
# #闭包调用
#     func1 = funcOut(func1)
#     func2 = funcOut(func2)
#
#     func1()
#     func2()



#闭包案例 根据配置信息使用闭包实现不同人的对话信息，例如对话:
#闭包的作用
"""闭包可以保存外部函数内的变量，不会随着外部函数调用完而销毁。
注意点:
由于闭包引用了外部函数的变量，则外部函数的变量没有及时释放，消耗内存。
闭包还可以提高代码的可重用性，不需要再手动定义额外的功能函数。
"""

# 外部函数
def config_name(name):
    # 内部函数
    def say_info(info):
        print(name + ": " + info)
    return say_info

if __name__ == '__main__':

    #闭包实例
    tom = config_name("Tom")

    tom("你好!")
    tom("你好, 在吗?")

    #闭包实例
    jerry = config_name("jerry")


    jerry("不在, 不和玩!")