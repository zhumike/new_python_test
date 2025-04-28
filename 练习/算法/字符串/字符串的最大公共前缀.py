"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
思路1：使用python的max（）,min（）函数来比较列表，元组等对象中元素的大小，比较安ansii码值大小比较，以示例1为例，最大的为flower,其次是flow,最后是flight,我们只需比较最大的字符串和最小字符串的公共前缀就是整个数组的公共前缀。
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        s1=min(strs)
        s2=max(strs)
        for i,x in enumerate(s1):
            if x!=s2[i]:
                return s2[:i]
        return s1
if __name__ == "__main__":
    demo = Solution()
    s1 =["dog","acecar","car"]
    print(demo.longestCommonPrefix(s1))
