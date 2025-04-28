# 字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
# 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
# 一对大括号创建一个空的字典：{}。

tel = {'jack': 4098, 'sape': 4139}

l1=list(tel.keys())
print(l1)

#构造函数 dict() 直接从键值对"元组列表"中构建字典。如果有固定的模式，列表推导式指定特定的键值对

dt=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dt)

# 字典推导可以用来创建任意键和值的表达式词典
dt2={x: x**2 for x in (2, 4, 6)}
print(dt2)

#关键字参数构造字段
dt3=dict(sape=4139, guido=4127, jack=4098)
print(dt3)


#遍历字典，在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print("{}键的值是:{}".format(k,v))
#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)