"""
给定一个字符串，逐个翻转字符串中的每个单词。

说明：

无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

示例 1：

输入："the sky is blue"
输出："blue is sky the"
示例 2：

输入："  hello world!  "
输出："world! hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入："a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         strs = s.split(' ')
#         res = ''
#         for i in range(len(strs) - 1, -1, -1):
#             if strs[i] != '':
#                 res += strs[i] + ' '
#
#         return res[:-1]

#知识点：1.字符串切分方法的使用 split()方法   2.  列表元素转为字符串，join方法
#3. 字符串strip方法的运用


#方法二
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

if __name__ =="__main__":
    demo = Solution()
    s= "a good   example"
    print(demo.reverseWords(s))