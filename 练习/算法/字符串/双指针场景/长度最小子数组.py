"""
长度最小的子数组
题目描述
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度
最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例：
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶：如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

"""
#双指针的思路
#
# def minSubArrayLen(self, s: int, nums: list[int]) -> int:
#     if not nums:
#         return 0
#     n = len(nums)
#     ans = n + 1
#     start, end = 0, 0
#     total = 0
#     while end < n:
#         total += nums[end]
#         while total >= s:
#             ans = min(ans, end - start + 1)
#             total -= nums[start]
#             start += 1
#         end += 1
#     return 0 if ans == n + 1 else ans


# 滑动窗口法，设立两个指针i,j，判断nums[i:j+1]跟s的大小关系来决定i,j的走向


class Solution:
    def minSubArrayLen(self,s,nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        else:
            l = 0
            r = 0
            sum_lr = 0
            length = len(nums)
            min_length = length + 1		#假设最大的长度为数组的长度+1
            while l < length:
                if r < length and sum_lr < s:	#r没超范围，而且子数组的和小于s,快指针
                    sum_lr += nums[r]
                    r += 1
                else:                          #慢指针
                    sum_lr -= nums[l]
                    l += 1
                if sum_lr >= s:		        #更新长度
                    min_length = min(r-l,min_length)
            return min_length
if __name__ == "__main__":
    demo = Solution()
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(demo.minSubArrayLen(s,nums))