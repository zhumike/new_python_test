

# a = [12,13,14,12,12,14,13,12,14,15]
# print(a.count(14))


# li = [5,6,7,9,-1,4,67,89,100,34,12]
# print(li[:-4:-1])
# #
# print(li[:4])
# print(li[4:])
# print(li[4::-1])
# print(li[-1:-4:-1])
# print(li[-4:])
# print(li[::-1])
# print(li[-1:-4])   #输出[]
# print(li[-2:])
# print(li[2:4])


# a = [20,10,40,30]
# a.sort()
# print(a)
#
# b= [20,10,40,30]
# c=sorted(b)
# print(c)
#
# e = [5,2,3,1,5,4]
# f = sorted(e,reverse=True)#降序
# print(f)


"""深浅拷贝"""


# 浅拷贝
li = [1,2,3]
li2 = li.copy()
print(id(li)==id(li2))
li2[0]=100
print(li)


#https://zhuanlan.zhihu.com/p/20062426831
#浅拷贝
# import copy
# li = [[1,2],[3,4]]
# li2 = copy.copy(li)
# print(id(li)==id(li2))
# li2[0][0]=80
# print(li)
#
#
# #深  不会影响原对象的值
# li = [[1,2],[3,4]]
# li2 = copy.deepcopy(li)
# li2[0][0] = 666
# print(li)
# print(li2)

#字典使用

# a = {'name':'陈丽','age':18,'job':'teacher'}
# c = dict(name='张伟',age=19)
# print(c)

#zip函数创建字典
# x = ['name','age','job']
# y = ['陈丽','18','teacher']
# e = dict(zip(x,y))
# print(e)

#用 fromkeys 创建'值为空'的字典
# h = dict.fromkeys(['name','age','job'])
# print(h)

#用 items 获取‘所有的键值对’
# print(a.items())
# for i in a.items():
#     print(i)

#列出所得有‘键’:keys,列出所得有‘值’:values
# a1=a.keys()
# print(a1)
# a2=a.values()
# print(a2)

#字典更新update
# b = dict([('job','Python'),('weight',75),('height',170)])
# print(b)
# a.update(b)
# print(a)

# a = {'name1':'陈丽','name2':'黄伟','name3':'阿亮','name4':'荣哥'}
# q,b,c,d=a.keys()
# print(q)
# l,m,n,o = a.values()
# print(l)
# print(type(l))

#格式化输出

# print('{1}-{0}'.format(1,2))

#集合
"""集合的作用
1 去重:把一个列表变成集合，就自动去重了。
2 关系测试:测试两组数据之前的交集、差集、并集等关系。
特征：
1、集合使用 set 表示;
2、集合也使用{ }表示，与字典不同的是:字典中存储的是键值对，集合中存储
的是单一的元素;
3、注意 1:x = { }表示的是空字典，不表示集合; 4、注意 2:x = set()可以创建空集合;
4.集合中的元素----无序性
"""
# x={1,2,3,4,6,8,12}
# x.add(23)
# x.remove(1)
# print(x)
#
# y=x.pop()
# print(y)

#返回当前集合的差集
# a1 = {1,6,8}
# a2 = {6,9,10}
# df = a1.difference(a2)
# print(df)

#返回两个集合的交集
# s = {1,2,3}
# t = {2,3,4}
# n=s.intersection(t)
# print(n)

#返回两个集合的并集
# s = {1,2,3}
# t = {2,3,4}
# n1=s.union(t)
# print(n1)

#返回集合的对称差集
# s = {1,2,3}
# t = {2,3,4}
# n2=s.symmetric_difference(t)
# print(n2)

#isdisjoint():判断当前集合与参数集合，是否交集为空;是返回 True， 否返回 False
# s = {1,2,3}
# t = {2,3,4}
# u = {4,5,6}
#
# print(s.isdisjoint(t))
# print(s.isdisjoint(u))


#issubset():判断当前集合是否为参数集合的子集;是返回 True，否 返回 False
# s = {1,2,3}
# t = {2,3,4}
# u = {1,2,3,4,5,6}
# print(s.issubset(t))
# print(s.issubset(u))

#in:判断某个元素是否在集合中
# s = {1,2,3,4}
# t=5 in s
# print(t)

#返回两个集合的交集
# s = {1, 2, 3, 4, 5}
# t = {4, 5, 6, 7}
# q=s & t
# print(q)

# #集合推导式
# s = {i for i in range(10)}
# print(s)

#元组
# tuple2 = ('5', '4', '8')
# #求最大值
# t1=max(tuple2)
# print(t1)
# #求最小值
# t2=min(tuple2)
# print(t2)