"""
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

"""


"""高级做法 
#find（）找到字符第一次出现的索引，rfind（）找到字符最后一次出现的索引，如果
# 这两个值相等且不等于-1说明该字符只出现一次，将所有只出现一次的字母
# 索引放入列表中，返回其中的最小值


a.字符串的find()方法   b.列表  min（）方法
"""

class Solution:
    def firstUniqChar(self, s):
        tmp = s
        tmp = [tmp.find(i) for i in s if tmp.find(i) == tmp.rfind(i) and tmp.find(i) != -1]
        if tmp:
            return min(tmp)
        else:
            return -1