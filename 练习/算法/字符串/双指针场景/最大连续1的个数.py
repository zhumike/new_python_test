"""
最大连续1的个数
给定一个二进制数组， 计算其中最大连续 1 的个数。

示例：
输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
 

提示：
输入的数组只包含 0 和 1 。
输入数组的长度是正整数，且不超过 10,000。
"""

# 思路：用一个变量记录当前连续1的个数，一个变量记录当前最大连续1的个数，
# 遇到1时，当前连续1的个数加1，否则当前连续1的个数归零。
#知识点  max函数的综合运用，双指针思维的运用，一个变量用来保存当前连续1的个数，另外一个变量用来保存最大1的个数
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        one_length = 0  # 当前连续1的个数
        max_length = 0  # 当前最大连续1的个数
        for i in nums:
            if i == 1:
                one_length += 1
            else:
                one_length = 0
            max_length = max(max_length, one_length)
        return max_length
