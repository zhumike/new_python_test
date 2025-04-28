"""
除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
 
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""

#1.先向右遍历，求出每个位置元素的所有在它左边元素的乘积   2.得出第一步的结果集，再在原数组从后往前遍历，求出对应元素
#位置所有右边的元素的乘积后，再乘以结果集对应的位置的元素值，就是最终的结果。

class Solution:
    def productExceptSelf(self, nums):
        n =len(nums)
        result = [1 for i in range(n)]
        print(result)
        result_left = 1
        result_right = 1
        for i in range(n-1):
            result_left *=nums[i]
            result[i+1] =result_left
        for i in range(n-1,0,-1): #从n-1到1
            result_right *=nums[i]
            result[i-1] *= result_right
            print(result[i-1])
        return result
if __name__ == "__main__":
    demo = Solution()
    l1=[1, 2, 3, 4]
    print(demo.productExceptSelf(l1))