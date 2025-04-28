# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :series7
# @Date     :2023/5/14 11:39
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""
#给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

#滑动窗口解法
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         occ = set()
#         n = len(s)
#         right, ans = 0, 0
#         for left in range(n):
#             while right < n and s[right] not in occ:
#                 occ.add(s[right])
#                 right += 1
#             if len(occ) > ans:
#                 ans = len(occ)
#             occ.remove(s[left])
#         return ans
#
# print(Solution().lengthOfLongestSubstring("ABCASSDERT"))


#解法二
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        s1 = ''
        num = []
        for el in s:
            if el not in s1:
                s1 += el
            else:
                num.append(len(s1))  # 记录长度
                index = s1.find(el)  # 找到存在的重复字符下标
                s1 += el  # 先添加元素
                s1 = s1[index + 1:]  # 更新窗口
        return max(max(num, default=0), len(s1))  # default=0，列表是空的时候
print(Solution().lengthOfLongestSubstring("ABCASSDERT"))


#解法三，滑动窗口

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        left=0
        right=1
        max_length=1
        while right<len(s):
            current_str=s[left:right]
            if s[right] not in current_str:
                right+=1
                max_length=max(max_length,right-left)
            else:
                right+=1
                left=current_str.index(s[right])+left+1
        return max_length