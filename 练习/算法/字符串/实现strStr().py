"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""

#思路
#
# 1、如果待查找子串为空，返回0；
#
# 2、如果大字符串的长度小于待查找子串的长度，返回-1；
#
# 3、计算需要编译的字符串下标位置：l = l1 - l2 + 1； 
#
# 4、从下标0到下标l遍历长字符串，截取与待查找子串长度相同的子字符串，判断内容是否与待查找子串相同，相同返回下标i；
#
# 5、默认找不到匹配的子串，返回-1。


#知识点：1.list下标遍历的方法 list[i:i+n]

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:     #子串为空，返回为0
            return 0
        l1 = len(haystack) #取母串的长度
        l2 = len(needle)    #取子串的长度
        if l1 < l2:        #母串小于子串，返回-1
            return -1
        l = l1 - l2 + 1     #设置需要遍历的次数
        for i in range(l):
            if haystack[i:i + l2] == needle:
                return i
if __name__ == "__main__":
    demo = Solution()
    l1 = "hello"
    l2 = "llo"
    print(demo.strStr(l1,l2))
