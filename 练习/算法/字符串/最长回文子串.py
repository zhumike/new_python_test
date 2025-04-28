"""
最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
"""
#从回文子串的中心考虑，先假设List中每一个点ii都有回文子串，接下来验证l[ii-1]
# 和 l[ii+1]是否相同，如果相同就继续验证l[ii-2]和 l[ii+2]。对比所有结果，
# 返回最大的子串。

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = list(s)
        length = len(l)
        if length == 0:
            return ""
        if length == 1:
            return s
        temp = []
        result = []
        i = 0
        ii = 0
        j = 1
        flag = True
        while ii < length:
            i = ii - 1
            j = ii + 1
            while j < length and l[ii] == l[j]:
                j = j + 1
                temp = l[ii:j]
            while (i >= 0 and j <= length - 1 and l[i] == l[j]):
                temp = l[i:j + 1]
                i = i - 1
                j = j + 1
            if len(temp) > len(result):
                result = temp
            ii = ii + 1
        if len(result) == 0:
            return l[0]
        return "".join(result)
if __name__ == "__main__":
    s = "babad"
    demo = Solution()
    print(demo.longestPalindrome(s))



