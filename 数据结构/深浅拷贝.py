# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :深浅拷贝
# @Date     :2025/4/8 09:50
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""
import copy

# a = [1, 2, [3, 4]]
# #深拷贝，拷贝对象是完全复制，修改对象彼此互补影响
# b = copy.deepcopy(a)
#
# print(id(a),id(b))
#
# b[2][0] = 100
# print(a)


#浅拷贝
# import copy
#
# a = [1, 2, [3, 4]]
# b = copy.copy(a)
# b[2][0] = 100
#
# print(a)

import copy

#基本数据类型，深浅拷贝效果一样

a = [1, 2, 3]
#浅拷贝
b = copy.copy(a)

b.append(4)
print(b)
print(a)


# c=copy.deepcopy(a)
# c.append(4)
#
# print(c)
# print(a)



