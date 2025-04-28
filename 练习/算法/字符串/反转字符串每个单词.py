"""
反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
"""

#1.字符串split方法的使用   数组转化为字符串  join方法使用
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = [item[::-1] for item in s.split(" ")]
        return " ".join(ans)
