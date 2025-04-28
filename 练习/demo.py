# # import os
# # f=os.listdir('e:/codeindex')
# # print(f)
#
# # l1 = [1,2,3,4,5,6,7,8]
# # print(l1[-1])
# # for i in range(10):
# #     print(i)
# # dict1 = {"name1":"hehehe","classname":"good"}
# # print(dict1["name1"])
# #
# # if "classname" in dict1:
# #     print("pass")
#
# # set1 = {1,2,3,4,5}
# #
# # dp = [[0] * 2 for _ in range(5)]
# # print(dp)
#
# # res = list()
# # li =[1,2,3,4]
# # res.append(li[1])
# # print(res)
#
# # for str in '437':
# #     print(int(str))
#
# dp = [[0] * 2 for _ in range(5)]
# print(dp)

res = list()
li =[1,2,3,4]
res.append(li[1])
print(res)
res.extend([7,8])
print(res)
res.append(11)
print(res)
#
# import bisect
#
# L = [1, 3, 3, 6, 8, 12, 15]
# x = 3
# #
# # x_insert_point = bisect.bisect_left(L, x)
# # # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１
# # print(x_insert_point)
#
#
# x_insert_point = bisect.bisect_right(L,x)
# print(x_insert_point)
# #在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回右侧位置３