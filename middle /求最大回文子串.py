# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :求最大回文子串
# @Date     :2023/6/20 11:15
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""

"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""

"""
直接找切片，找到每一个子字符串，然后判断是不是回文字符串，如果是就返回字符串
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s) - 1, 0, -1):
            for j in range(len(s) - i, ):
                str1 = s[j:i + j + 1]#子串
                if str1 == str1[::-1]: #判断是否回文
                    return str1

if __name__ == '__main__':
    ls = "babad"
    ob = Solution()
    print(ob.longestPalindrome(ls))