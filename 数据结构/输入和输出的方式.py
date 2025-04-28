import os
# # format()
# 中使用了"关键字参数", 那么它们的值会指向使用该名字的参数
# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
#
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
#
# #针对字典的格式化输出，使用**table
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))


# # 打开一个文件
# f = open("./tmp/foo.txt", "w")
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好的!!\n" )
# # 关闭打开的文件
# f.close()
# print(os.getcwd())#返回当前工作目录

# f = open("./tmp/foo.txt", "r")
# str = f.read()
# print(str)
# # 关闭打开的文件
# f.close()

# 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# f.readline()
# 打开一个文件
# f = open("/tmp/foo.txt", "r")
#
# str = f.readline()
# print(str)
#
# # 关闭打开的文件
# f.close()

#f.readlines()
# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
# 打开一个文件
# f = open("/tmp/foo.txt", "r")
# str = f.readlines()
# print(str)
# print(str[0])
# # 关闭打开的文件
# f.close()


#迭代一个文件对象然后读取每行:
#
# f = open("/tmp/foo.txt", "r")
#
# for line in f:
#     print(line, end='')#为末尾end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串，其实这也是一个语法要求，表示这个语句没结束。
# # 关闭打开的文件
# f.close()



#  f.write  将 string 写入到文件中, 然后返回写入的字符数。
# 打开一个文件
# f = open("/tmp/foo.txt", "w")
# num = f.write( "Python是一个非常好的语言。\n是的，的确非常好!!\n" )
# print(num)
# # 关闭打开的文件
# f.close()

'''
有一个数据list of dict如下
a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]
写入到本地一个txt文件，内容格式如下：
yoyo1,123456
yoyo2,123456
yoyo3,123456
'''
a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]
with open('./tmp/a.txt','w+') as f:
    for i in a:
        for key ,value in i.items():   #字典items() 方法以列表返回可遍历的(键, 值) 元组数组。
            f.write("{},{} {}".format(key,value,'\n'))   #
with open('./tmp/a.txt','r') as f:
    print(f.read())