"""
存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""

"""高级用法  set方法解决"""
class Solution:
    def containsDuplicate(self,nums):
        return len(nums) != len(set(nums))







"""
常规方法
"""
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == 1:
            return False
        d = {}
        for i in nums:
            if i in d:
                print(i)
                return True
            d[i] = 0
            print(d[i])
        return False
