
"""按value值进行排序?"""
# d= {'a':24,'g':52,'i':12,'k':33}
# d2=sorted(d.items(),key=lambda x:x[1])
# print(d2)
# d3 = {i[0]:i[1] for i in d2}
# print(d3)
# print(d3['a'])

"""反转字符串"""
# print("aStr"[::-1])

""".将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
"""
# str1 = "k:1|k1:2|k2:3|k3:4"
# def str2dict(str1):
	# dict1 = {}
	# for iterms in str1.split('|'):
	# 	key,value = iterms.split(':')
	# 	dict1[key] = value
	# return dict1
#字典推导式
# d = {k:int(v) for t in str1.split("|") for k, v in (t.split(":"),)}
# print(d)


"""按alist中元素的age由大到小排序"""
# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# ali=sorted(alist,key=lambda x:x['age'],reverse=True)
# print(ali)
#
#

# print([x*11 for x in range(10)])

"""给定两个列表，怎么找出他们相同的元素和不同的元素？
"""

# list1 = [1,2,3]
# list2 = [3,4,5]
# set1 = set(list1)
# set2 = set(list2)
# print(set1 & set2)
# print(set1 ^ set2)

"""实现删除list里面的重复元素
"""
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)
