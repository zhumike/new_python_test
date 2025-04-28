# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :整数反转
# @Date     :2023/6/20 16:42
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""

"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        # 定义res作为最终返回的的结果，初始为0
        res = 0
        # 定义index作为最终结果正负的标签，1为负，0为正
        index = 0
        # 若x为负，取绝对值，并让index = 1
        if x < 0:
            index = 1
            x = -x
        # 定义num_reverse作为反转之后的列表，反转之后的数字每一位对应其中的一个元素
        num_reverse = []
        # while循环，获得x的每一位数字倒序，存入num_reverse列表中
        while int(x/10) != 0:
            num_reverse.append(x%10)
            x = int(x/10)
        num_reverse.append(x)
        # 列表转换为数字时每一位数字需要乘10的digit次方
        digit = len(num_reverse) - 1
        for i in range(len(num_reverse)):
            res = res + num_reverse[i]*10**digit
            digit = digit - 1
        # 结果正负判断
        if index == 1:
            res = res * -1
        # 结果溢出判断
        if res < -1*2**31 or res >= 2**31:
            return 0
        # 返回结果
        return res

if __name__ == '__main__':
    ls = 123
    ob = Solution()
    print(ob.reverse(ls))