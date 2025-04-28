
"""单例模式的实现"""
# def singleton(cls):
#     instances = {}
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#             return instances[cls]
#         return wrapper
#
# @singleton
# class Foo(object):
#     pass
# foo1 = Foo()
# foo2 = Foo()
# print(foo1 is foo2)


"""设计实现遍历目录与子目录，抓取.pyc文件"""
#需要debug
# import os
# def pick(obj):
#     if obj.endswith(".pyc"):
#         print(obj)
# def scan_path(ph):
#     file_list = os.listdir(ph)
#     for obj in file_list:
#         if os.path.isfile(obj):
#             pick(obj)
#         elif os.path.isdir(obj):
#             scan_path(obj)
# if __name__ =='__main__':
#     path = 'e:/codeindex/zhu/no1'
#     scan_path(path)
"""实现列表解析，可用于快速实现列表的删除"""
# a=[1,2,3,4,5,6,7,8]
# b = [i for i in a if i>5]
# print(b)

# a=[1,2,3,4,5,6,7,8]
# b = filter(lambda x: x>5,a)
# print(list(b))

"""求出列表所有奇数并构造新列表"""
# a = [1,2,3,4,5,6,7,8,9,10]
# res = [ i for i in a if i%2==1]
# print(res)

"""用一行python代码写出1+2+3+10248
"""
# from functools import reduce
# #1.使用sum内置求和函数
# num = sum([1,2,3,10248])
# print(num)
# #2.reduce 函数
# num1 = reduce(lambda x,y :x+y,[1,2,3,10248])
# print(num1)


""".字符串
方法一： 利用
转换成 123 ，不使用内置api，"""
# def atoi(s):
#     num = 0
#     for v in s:
#         for j in range(10):
#             if v == str(j):
#                 num = num * 10 + j
#     return num
# num = atoi("1233")
# print(num)

"""给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答
案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] =
2+7 =9,所以返回[0,1]"""

# class Solution(object):
# def twoSum(self, nums, target):
#     for i in range(len(nums)):
#         num = target - nums[i]
#         if num in nums[i+1:]:
#             return [i, nums.index(num,i+1)]


#哈希表  使用哈希表，可以将寻找 target - x 的时间复杂度降低到从
#这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然
# 后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashmap = {}
#         for index, num in enumerate(nums):
#             another_num = target - num
#             if another_num in hashmap:
#                 return [hashmap[another_num], index]
#             hashmap[num] = index
#         return None

"""该列表只包含满足以下条件的值，元素为原始列表中偶数切片"""
# list_data = [1,2,5,8,10,3,18,6,20]
# res = [x for x in list_data[::2] if x %2 ==0]
# print(res)

"""找出数组第2大的数字
"""
# def find_second_large_num(num_list):
#     tmp_list = sorted(num_list)
#     print("方法一\nSecond_large_num is :", tmp_list[-2])


"""闭包的应用"""
# def multi():
#     return [lambda x : i*x for i in range(4)]
# print([m(3) for m in multi()])

"""统计一段字符串中字符出现的次数"""
# def count_str(str_data):
#     dict_str = {}
#     for i in str_data:
#         #键值加1
#         dict_str[i] = dict_str.get(i, 0) + 1
#     return dict_str
# dict_str = count_str("AAABBCCAC")
# print(dict_str)
# str_count_data = ""
# for k, v in dict_str.items():
#     str_count_data += k + str(v)
# print(str_count_data)

""""写一个函数找出一个整数数组中，第二大的数"""
# def find_second_large_num(num_list):
#     one = num_list[0]
#     two = num_list[0]
#     for i in range(1, len(num_list)):
#         if num_list[i] > one:
#             two = one
#             one = num_list[i]
#         elif num_list[i] > two:
#             two = num_list[i]
#     print("第二个大的数是 :", two)
# num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
#
# find_second_large_num(num_list)

"""手写一个判断时间装饰器"""
# import datetime
# class TimeException(Exception):
#     def init (self, exception_info):
#         super(). init ()
#         self.info = exception_info
#     def str (self):
#         return self.info
# def timecheck(func):
#     def wrapper(*args, **kwargs):
#         if datetime.datetime.now().year == 2020:
#             func(*args, **kwargs)
#         else:
#             raise TimeException("函数已过时")
#     return wrapper
# @timecheck
# def test(name):
#     print("Hello {}, 2020 Happy".format(name))
# if __name__ == "__main__":
#     test("backbp")
"""带参数的装饰器"""
# def new_func(func):
#     def wrappedfun(username, passwd):
#         if username == 'root' and passwd == '123456789':
#             print('通过认证')
#             print('开始执行附加功能')
#             return func()
#         else:
#             print('用户名或密码错误')
#             return
#     return wrappedfun
# @new_func
# def origin():
#     print('开始执行函数')
# origin('root','123456789')

"""hasattr(object,name)函数:
判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True，否
则返回False。"""
# class function_demo(object):
#     name = 'demo'
#     def run(self):
#         return "hello function"
# functiondemo = function_demo()
# res = hasattr(functiondemo, "name") # 判断对象是否有name属性， True
# print(res)
# res = hasattr(functiondemo, "run") # 判断对象是否有run方法， True
# print(res)
# res = hasattr(functiondemo, "age") # 判断对象是否有age属性， False
# print(res)

"""getattr(object, name[,default])函数：
获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。注
意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后面
添加括号()."""
#
# functiondemo = function_demo()
# s1=getattr(functiondemo, "name")# 获取name属性，存在就打印出来 --- demo
# print(s1)
# s2=getattr(functiondemo, "run") # 获取run 方法，存在打印出方法的内存地址
# print(s2)
# # s3=getattr(functiondemo, "age") # 获取不存在的属性，报错
# # print(s3)
# s4=getattr(functiondemo, "age", 18)# 获取不存在的属性，返回一个默认值
# print(s4)

# """给对象的属性赋值，若属性不存在，先创建再赋值"""
# class function_demo(object):
#     name = "demo"
#     def run(self):
#         return "hello function"
# functiondemo = function_demo()
# res = hasattr(functiondemo, "age") # 判断age属性是否存在， False
# print(res)
# setattr(functiondemo, "age", 18) # 对age属性进行赋值，无返回值
# res1 = hasattr(functiondemo, "age") # 再次判断属性是否存在， True
# print(res1)


"""手写一个单例模式"""
"""应用场景：
单例模式应用的场景一般发现在以下条件下：
资源共享的情况下，避免由于资源操作时导致的性能或损耗等，如日志文件，应用配置。
控制资源的情况下，方便资源之间的互相通信。如线程池等， 1,网站的计数器 2,应用配置 3.多线程池 4
数据库配置 数据库连接池 5.应用程序的日志应用..."""
#
#
# class A(object):
#     _instance = None
#     def _new_(cls,*args,**kwargs):
#         if cls._instance is None:
#             cls._instance = object._new_(cls)
#             return cls._instance
#         else:
#             return cls._instance



"""装饰器的理解：装饰器本质上是一个callableobject ，它可以让其他函数在不需要做任何代码变动的前提下增加额外功
能，装饰器的返回值也是一个函数对象。"""
# import time
# from functools import wraps
#
# def timeit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.clock()
#         ret = func(*args, **kwargs)
#         end = time.clock()
#         print('used:%d'%(end-start))
#         return ret
#     return wrapper
# @timeit
# def foo(n1,n2):
#     print(n1+n2)
# if __name__ == "__main__":
#      a = foo("s1","s2")

#
# N =100
# print ([[x for x in range(1,100)] [i:i+3] for i in range(0,100,3)])
# # for i in range(0,100,3):
# #     print(i)
#
# s=[1,2,3,4,5,6,7]
# print(s[0:3])
# import re
#
# s1='_aai0efe00'
# res=re.findall('^[a-zA-Z_]?[a-zA-Z0-9_]{1,}\d$',s1)
# print(res)


"""进程"""

# import os
# from multiprocessing import Process
# import time
# def pro_func(name,age,**kwargs):
#     for i in range(4):
#         print("子进程正在运行中， name=%s,age=%d,pid=%d"%(name,age,os.getpid()))
#         print(kwargs)
#         time.sleep(0.2)
# if __name__ == "__main__":
# #创建Process对象
#     p = Process(target=pro_func,args=('小明',18),kwargs={'m':20})
# #启动进程
#     p.start()
#     time.sleep(1)
# #1秒钟之后，立刻结束子进程
#     p.terminate()
#     p.join()

"""线程同步"""
import threading
import time
# def thread():
#     time.sleep(2)
#     print("子线程结束")
# def main():
#     t1 = threading.Thread(target=thread)
#     t1.start()
#     print('---主线程--结束')
# if __name__ == "__main__":
#     main()
"""线程同步 setDaemon（True) """

# import threading
# import time
# def thread():
#     time.sleep(2)
#     print("子线程结束")
# def main():
#     t1 = threading.Thread(target=thread)
#     t1.setDaemon(True)  # 设置子线程守护主线程
#     t1.start()
#     print('---主线程--结束')
# if __name__ == "__main__":
#     main()