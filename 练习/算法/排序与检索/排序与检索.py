'''
最大数





给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
'''

'''
判断每个数字谁在最前面，其实就是一个另类排序了。
现在假设有两个数字 x，y，单独看这两个数字，谁在前面谁在后面？
可以这样比较：str(x) + str(y) > str(y) + str(x) 很显然x在前，否则 y在前。'''

# class compare(str):
#     def __lt__(x, y):
#         return x + y > y + x
#
# def largestNumber(nums):
#     largest = sorted([str(n) for n in nums], key=compare)
#     largest = ''.join(largest)
#     return '0' if largest[0] == '0' else largest
#
#
# if __name__ == '__main__':
#     nums = [3, 30, 34, 5, 9]
#     result = largestNumber(nums)
#     print(result)


'''
摆动排序 II

给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。

 

示例 1：

输入：nums = [1,5,1,1,6,4]
输出：[1,6,1,5,1,4]
解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
示例 2：

输入：nums = [1,3,2,2,3,1]
输出：[2,3,1,3,1,2]
'''

'''
排序后重组
对数组进行排序(从小打大)。
取前半部分，后半部分，进行间隔式赋值。'''
# class Solution:
#     def wiggleSort(self, nums):
#         nums.sort()
#         half = len(nums[::2])
#         nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
# if __name__ == '__main__':
#     demo = Solution()
#     l1 = [1,3,2,2,3,1]
#     demo.wiggleSort(l1)
#     print(l1)


'''
寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

 

示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

'''

'''
方法：二分查找
思路：如果中间元素大于其相邻后续元素，则中间元素左侧(包含该中间元素）必
包含一个局部最大值。如果中间元素小于其相邻后续元素，则中间元素右侧必包含
一个局部最大值。
'''


# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return -1
#
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) >> 1
#             if nums[mid] < nums[mid + 1]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left
#
# if __name__ == '__main__':
#     demo = Solution()
#     nums =nums = [1,2,3,1]
#     print(demo.findPeakElement(nums))


'''
寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

 

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
'''


#线性数组扫描 遇到第一个count > 1 的元素就把它返回。


# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for item in nums:
#             if nums.count(item) != 1:
#                 return item
#
# #比较一下sum（nums）和sum（set（nums））和的差值，然后除以它们俩的长度差，就是那个重复的元素
# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return (sum(nums) - sum(set(nums)))/ (len(nums) - len(set(nums)))


'''
计算右侧小于当前元素的个数


给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 
有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

 

示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
'''


'''
我们可以把遍历过的数据排序，然后搜索每个数据排入这个数组的位置，也就得到了右侧比它小的数据个数。
这里可以用bisect来很容易的实现这个功能
'''
import bisect
class Solution:
    def countSmaller(self, nums):
        ans=[]
        tmp = []
        for i in reversed(nums):
            print("i:{}".format(i))
            pos = bisect.bisect_right(tmp, i)
            print("pos 是{}".format(pos))
            ans.append(pos)
            print("ans 是{}".format(ans))
            tmp.insert(pos, i)
            print("tmp:{}".format(tmp))
        return list(reversed(ans))
if __name__ == '__main__':
    demo = Solution()
    nums = [5, 2, 6, 1]
    print(demo.countSmaller(nums))