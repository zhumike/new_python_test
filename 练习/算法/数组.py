"""
乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


"""思路
动态规划
，在这里，我们可以这样进行状态设计，也就是以 nums[i] 结尾的连续子数组的最大值。
现在具体看下如何进行状态设计、推导状态转移方程，进而加以实现。
因为数组中存在着负数，所以有可能导致乘积会从最大变为最小，同样的，最小也可能变为最大。这里需要注意。
现在，先进行状态设计：
d[i][j]： 表示以 nums[i] 结尾的连续子数组的最值。在这里，j 决定计算的是最大值还是最小值。
其中当 j = 0 时，表示计算的是最小值，
当 j = 1 时，表示计算的是最大值。
现在推导状态转移方程：

因为是乘积的关系，nums[i] 数值的正负，与前面的状态值是有联系的，具体如下：

当 nums[i] > 0 时：
与最大值的乘积依然是最大值
与最小值的乘积依然是最小值
当 nums[i] < 0 时：
与最大值的乘积变为最小值
与最小值的乘积变为最大值
当 nums[i] = 0 时，这里无论最大最小值，最终结果都是 0，这里其实可以合并在上面任意一种情况。
但是还有需要注意的地方，这里前面的状态值的正负也是会影响最终的最值。假如，前面的最大值是负数的情况下，也就是 dp[i-1][1] < 0，但这是 nums[i] > 0 的情况下，
这里就要重新考虑，此时的最大值应该是 dp[i][1] = nums[i]。

按照这个思路，将所有情况的状态转移方程都写出来，具体如下：

dp[i][0] = min(nums[i], dp[i-1][0] * nums[i]) if nums[i] >= 0
dp[i][1] = max(nums[i], dp[i-1][1] * nums[i]) if nums[i] >= 0

dp[i][0] = min(nums[i], dp[i-1][1] * nums[i]) if nums[i] < 0
dp[i][1] = max(nums[i], dp[i-1][0] * nums[i]) if nums[i] < 0
"""

# class Solution:
#     def maxProduct(self, nums) :
#         if len(nums) == 0:
#             return 0
#         length = len(nums)
#         # 初始化
#         # dp 数组有两个元素，一个存储最大值，一个最小值
#         dp = [[0] * 2 for _ in range(length)]
#         # 初始化数组首元素为最大值和最小值
#         dp[0][0] = nums[0]
#         dp[0][1] = nums[0]
#         # 　开始遍历
#         for i in range(1, length):
#             # 状态转移方程
#             if nums[i] > 0:
#                 dp[i][0] = min(nums[i], dp[i - 1][0] * nums[i])
#                 dp[i][1] = max(nums[i], dp[i - 1][1] * nums[i])
#             else:
#                 dp[i][0] = min(nums[i], dp[i - 1][1] * nums[i])
#                 dp[i][1] = max(nums[i], dp[i - 1][0] * nums[i])
#
#         # 因为最终要求得最大值，那么在 dp[i][1] 找得最大即可
#         # 初始化返回值
#         res = dp[0][1]
#         for i in range(1, length):
#             res = max(res, dp[i][1])
#             print(res)
#         return res












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

#哈希法
# class Solution:
#     def majorityElement(self, nums) :
#         mid = len(nums) // 2  # 数组长度的一半
#         dic = {}  # 定义字典
#
#         for i in range(len(nums)):  # 循环遍历
#             if nums[i] not in dic:  # 若元素不在字典中，添加到字典中
#                 dic[nums[i]] = 1
#             else:  # 若元素在字典中，其Value加一
#                 dic[nums[i]] += 1
#             if dic[nums[i]] > mid:  # 如果某Value值大于mid，则为多数元素，
#                 return nums[i]
# list1 = [2,2,1,1,1,2,2]
# a  = Solution()
# B = a.majorityElement(list1)
# print(B)


"""
旋转数组

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""
#方法1，方案1

# 一个一个旋转旋转数组是一个 进队列  出队列 动作，用下标来控制进出顺序
# k是要移动的次数，输入数组的长度是队的长度，长度减去次数就是元素将要移动到位置的下标地址
# k要对长度取余不出错
# class Solution:
#     def rotate(self, nums, k):
#         temp = []
#         l = len(nums) #数组长度
#         k = k % l
#         if k ==0:
#             return nums
#         for i in range(l):
#             temp.append(nums[(i - k)])
#         nums[:] = temp
#         return nums



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
# class Solution:
#     def containsDuplicate(self,nums):
#         return len(nums) != len(set(nums))



"""
常规方法
"""
# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) == 0 or len(nums) == 1:
#             return False
#         d = {}
#         for i in nums:
#             if i in d:
#                 print(i)
#                 return True
#             d[i] = 0
#             print(d[i])
#         return False






"""
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions/xmy9jh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


#用数组的remove方法和extend方法
# class Solution:
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n = nums.count(0)
#         for i in range(n):
#             nums.remove(0)
#         nums.extend([0]*n)
#         return nums


#方法2
"""
变量j用来保存已遍历过部位0的值。
"""
# class Solution:
#     def moveZeroes(self, nums):
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j], nums[i] = nums[i], nums[j]
#                 j += 1
#         return nums














"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
 

示例：

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
"""

# import random
#
# class Solution:
#     def __init__(self, nums):
#         self.nums = nums
#         self.original = list(nums)
#         print(list(nums))
#
#     def reset(self) :
#         self.nums = self.original
#         self.original = list(self.original)
#         return self.nums
#
#     def shuffle(self) :
#         for i1 in range(len(self.nums)):
#             i2 = random.randrange(i1, len(self.nums))
#             self.nums[i1], self.nums[i2] = self.nums[i2], self.nums[i1]
#         return self.nums





"""
两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

"""

#双指针解法
# class Solution:
#     def intersect(self, nums1, nums2) :
#         nums1.sort()
#         nums2.sort()
#         p = q = 0
#
#         ans = []
#         # 任意指针到达数组末尾，结束遍历
#         while p < len(nums1) and q < len(nums2):
#             # 在这里，先判断指针对应元素的大小
#             # 当不相等时，指针对应元素小的移动
#             # 相等时，将元素放入结果列表中，同时移动指针
#             if nums1[p] > nums2[q]:
#                 q += 1
#             elif nums1[p] < nums2[q]:
#                 p += 1
#             else:
#                 ans.append(nums1[p])
#                 print(ans)
#                 p += 1
#                 q += 1
#         return ans



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


#
# class Solution:
#     def productExceptSelf(self, nums):
#         n =len(nums)
#         result = [1 for i in range(n)]
#         print(result)
#         result_left = 1
#         result_right = 1
#         for i in range(n-1):
#             result_left *=nums[i]
#             result[i+1] =result_left
#         for i in range(n-1,0,-1): #从n-1到1
#             result_right *=nums[i]
#             result[i-1] *= result_right
#             print(result[i-1])
#         return result





"""
最小栈
描述：

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) – 将元素 x 推入栈中。
pop() – 删除栈顶的元素。
top() – 获取栈顶元素。
getMin() – 检索栈中的最小元素。

示例

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); --> 返回 -3.
minStack.pop();
minStack.top(); --> 返回 0.
minStack.getMin(); --> 返回 -2.
"""


# class MinStack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min = None
#
#     def push(self, x):
#         self.stack.append(x)
#         if self.min == None or self.min > x:
#             self.min = x
#
#     def pop(self):
#
#         popItem = self.stack.pop()
#         if len(self.stack) == 0:
#             self.min = None
#             return popItem
#
#         if popItem == self.min:
#             self.min = self.stack[0]
#             for i in self.stack:
#                 if i < self.min:
#                     self.min = i
#         return popItem
#
#     def top(self):
#         return self.stack[-1]
#
#     def getMin(self):
#         return self.min
#
# if __name__ == "__main__":
#     demo = MinStack()
#     demo.push(1)
#     demo.push(2)
#     demo.push(3)
#     print(demo.getMin())