# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :字符串转化为整数
# @Date     :2023/6/20 17:14
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s, ans, flag = s.lstrip(), 0, 1
        if s == "": return 0
        if   s[0] == '+': s = s[1:]
        elif s[0] == '-': flag, s = -1, s[1:]
        for c in s:
            if c.isdigit(): ans = ans * 10 + int(c)
            else: break
        ans *= flag
        return min(max(ans, - 1 << 31), (1 << 31) - 1)

if __name__ == '__main__':
    ls = "42"
    ob = Solution()
    print(ob.myAtoi(ls))