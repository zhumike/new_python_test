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















