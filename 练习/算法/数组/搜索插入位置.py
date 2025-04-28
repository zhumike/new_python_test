'''搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1


示例 3:

输入: [1,3,5,6], 7
输出: 4


示例 4:

输入: [1,3,5,6], 0
输出: 0
'''


# class Solution {
# public int searchInsert(int[] nums, int target) {
# /* 如果目标值小于等于索引值，则取代索引值位置 /
# for (int i = 0 ; i < nums.length; i++){
# if (nums[i] >= target)
# return i;
# }
# / 当所有的索引值均小于目标值，则目标值插在末尾 */
# return nums.length;
# }
# }

#知识点    enumerate函数的综合运用
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #enumerate()函数会输出下标和对象
        for i,num in enumerate(nums):#没超过列表边界
            if target<=num:
                return i
        return len(nums)#若超出