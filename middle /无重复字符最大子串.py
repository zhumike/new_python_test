# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :无重复字符最大子串
# @Date     :2023/6/20 10:46
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""

"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用一个辅助变量来暂时存储匹配的子串
        ans = ''
        tep = ''
        for i in s:
            # 遍历，若不重复则记录该字符
            if i not in tep:
                tep += i
            # 如果遇到了已经存在的字符，则找到该字符所在位置，删除该字符，并保留该位置之后的子串，并把当前字符加入到最后，完成更新
            else:
                tep = tep[tep.index(i)+1:]
                tep += i
            # 如果是当前最长的，就替换掉之前存储的最长子串
            if len(tep) > len(ans):
                    ans = tep
        return len(ans)

if __name__ == '__main__':
    ls = "pwwkew"
    ob = Solution()
    print(ob.lengthOfLongestSubstring(ls))