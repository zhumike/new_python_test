# a = [66.25, 333, 333, 1, 1234.5]
#
# """list的count用法，统计列表中指定字符的个数"""
# print(a.count(333), a.count(66.25), a.count('x'))
#
# """在索引2的地方插入元素"""
# a.insert(2, -1)
# print(a)#  [66.25, 333, -1, 333, 1, 1234.5]
#
# """list末尾添加元素值"""
# a.append(999)
# print(a)#[66.25, 333, -1, 333, 1, 1234.5, 999]
#
# """返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。"""
# print(a.index(333))
#
# """删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。"""
# a.remove(333)
# print(a)
#
# """反转列表元素"""
# a.reverse()
# print(a)
#
# """对列表中的元素进行排序,默认升序"""
# a.sort()
# print(a)
#
#



"""将列表当作队列使用"""
# from collections import deque
#
# queue = deque(["Eric", "John", "Michael"])
# print(queue)
#
# queue.append("Terry")
# queue.append("Graham")
# print(queue)
#
# e1=queue.popleft()
# print(e1)
# #
# queue.popleft()
# print(queue)


"""列表推导式运用"""

# vec = [2, 4, 6]
# vea = [3*x for x in vec]
# print(vea)
# #
# q1=[[x, x**2] for x in vec]
# print(q1)
#
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# Q1=[weapon.strip() for weapon in freshfruit]
# print(Q1)
#
# q3=[3*x for x in vec if x > 3]
# print(q3)


# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
#
# l4=[x*y for x in vec1 for y in vec2]
# print(l4)

"""嵌套列表"""

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12]]
# print(matrix)
# for row in matrix:
#     print(row)
# #反转矩阵
#
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

