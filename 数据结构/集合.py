#集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = set('abracadabra')
b = set('alacazam')


print(a - b)                              # 在 a 中的字母，但不在 b 中
#{'r', 'd', 'b'}

print(a | b)                            # 在 a 或 b 中的字母
#{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}


print(a & b)                             # 在 a 和 b 中都有的字母
#{'a', 'c'}

print(a ^ b)                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
#{'r', 'd', 'b', 'm', 'z', 'l'}