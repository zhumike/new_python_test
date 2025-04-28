"""
分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案
先将原字符串分割成左右两个部分，然后不管左边的字符串，将右边的字符串进行递归操作。但是在对右边的字符串
进行递归操作之前,需要验证左边的左边的字符串是回文串，然后将左边的字符串和右边字符串的递归结果，进行组合，返回最后结果。


解法一 分治
将大问题分解为小问题，利用小问题的结果，解决当前大问题。

这道题的话，举个例子。

aabb
先考虑在第 1 个位置切割，a | abb
这样我们只需要知道 abb 的所有结果，然后在所有结果的头部把 a 加入
abb 的所有结果就是 [a b b] [a bb]
每个结果头部加入 a，就是 [a a b b] [a a bb]

aabb
再考虑在第 2 个位置切割，aa | bb
这样我们只需要知道 bb 的所有结果，然后在所有结果的头部把 aa 加入
bb 的所有结果就是 [b b] [bb]
每个结果头部加入 aa,就是 [aa b b] [aa bb]

aabb
再考虑在第 3 个位置切割，aab|b
因为 aab 不是回文串，所有直接跳过

aabb
再考虑在第 4 个位置切割，aabb |
因为 aabb 不是回文串，所有直接跳过

最后所有的结果就是所有的加起来
[a a b b] [a a bb] [aa b b] [aa bb]
"""

class Solution:
    def partition(self, s) :
        res = []
        if s == "":
            return [[]]
        if len(s) == 1:
            return [[s]]
        strLenth = len(s)
        for i in range(1,strLenth+1):
            leftres = s[:i]  # 以aab为例，左字符串分别为a，aa，aab
            right = s[i:]
            if self.isPalindrome(leftres):
                rightres = self.partition(right)
                for i in rightres:
                    res.append([leftres]+i)
        return res
    def isPalindrome(self,s):   # 判断是不是回文数
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
