"""
多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
例子：
输入: [3,2,3]
输出: 3
1
2
输入: [2,2,1,1,1,2,2]
输出: 2
"""
#知识点  1.字典的用法   2.字典的赋值  3.取整用法  //


#哈希法
class Solution:
    def majorityElement(self, nums) :
        mid = len(nums) // 2  # 数组长度的一半
        dic = {}  # 定义字典

        for i in range(len(nums)):  # 循环遍历
            if nums[i] not in dic:  # 若元素不在字典中，添加到字典中
                dic[nums[i]] = 1
            else:  # 若元素在字典中，其Value加一
                dic[nums[i]] += 1
            if dic[nums[i]] > mid:  # 如果某Value值大于mid，则为多数元素，
                return nums[i]




