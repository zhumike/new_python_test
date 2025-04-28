'''
至少有K个重复字符的最长子串
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

 

示例 1：

输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2：

输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
'''

#思路：若一个字符出现的总次数小于k，它一定不在子串里，用它作为界限去分割

# class Solution(object):
# #     def longestSubstring(self, s, k):
# #         """
# #         :type s: str
# #         :type k: int
# #         :rtype: int
# #         """
# #         if len(s) < k:
# #             return 0
# #         c = min(set(s), key=s.count)
# #
# #         if s.count(c) >= k:
# #             return len(s)
# #         return max(self.longestSubstring(t, k) for t in s.split(c))
# # if __name__ == "__main__":
# #     demo = Solution()
# #     s = "ababbc"
# #     k = 2
# #     print(demo.longestSubstring(s,k))



'''
二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
'''

#思路：
# 创建递归函数，实现子节点到父节点回溯的方式来计算最大值
#
# 注意：最长的路径肯定是属于“从一端的最左侧到这端的最右侧” 这个完整链条的一部分。

# class Solution(object):
#     def __init__(self):
#         self.result = float('-inf')
#
#     def maxPathSum(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root == None:
#             return 0
#         self.getMax(root)
#         return self.result
#
#     def getMax(self, root):
#         """辅助函数"""
#
#         # 如果当前节点为空就表示包含当前节点的最大路径为0
#         if root == None:
#             return 0
#
#         # 递归的计算当前节点的左子树和右子树能提供的最大路径和。如果为负，就置为0（相当于从头开始）
#         left = max(0, self.getMax(root.left))
#         right = max(0, self.getMax(root.right))
#
#         # 注意：最长的路径肯定是属于从一端的最左侧到这端的最右侧的一部分
#         # 每计算一次左右子树的最大值，就更新当前的result
#         self.result = max(self.result, left + right + root.val)
#
#         # 回溯到父节点，最大路径就只能包含左右两个子树中的一个
#         return max(left, right) + root.val








'''
最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

 

进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
'''

#常规解法，遍历的形式
#
# class Solution(object):
#
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#
#         # 用于存储最大长度
#         max_count = 1
#         # 存储每一个元素的最长组合长度
#         count = 1
#         for num in nums:
#             ele = num
#             while (ele + 1) in nums:
#                 count += 1
#                 ele += 1
#
#             if count > max_count:
#                 max_count = count
#             count = 1
#
#         return max_count
# if __name__ == "__main__":
#     demo = Solution()
#     nums = [100, 4, 200, 1, 3, 2]
#     print(demo.longestConsecutive(nums))

# 解法2  # ：通过 "字典记录" 的形式
#
#
# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#
#         record = dict()
#         res = 0
#         for num in nums:
#             if num not in record:
#                 left = record.get(num - 1, 0)
#                 right = record.get(num + 1, 0)
#
#                 length = right + left + 1
#
#                 res = max(res, length)
#
#                 # 相邻几个连续元素的长度都按照最长序列赋值
#                 for item in [num - left, num, num + right]:
#                     record[item] = length
#
#         return res






'''
打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''


'''
动态规划问题
'''
#
# class Solution:
#     def rob(self, nums):
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         pre1, cur1 = 0, 0
#         for i in nums[:-1]:
#             pre1, cur1 = cur1, max(pre1 + i, cur1)
#
#         pre2, cur2 = 0, 0
#         for j in nums[1:]:
#             pre2, cur2 = cur2, max(pre2 + j, cur2)
#
#         return max(cur1, cur2)
# if __name__ == "__main__":
#     demo = Solution()
#     l1 = [2,7,9,3,1]
#     print(demo.rob(l1))




'''
最长上升子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
'''


'''
思路：https://blog.csdn.net/qq_32424059/article/details/88076376
'''

# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l = len(nums)
#         if not l:
#             return 0
#         dp = [1 for _ in range(l)]
#
#         for i in range(1, l):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[j] + 1, dp[i])
#
#         return max(dp)
# if __name__ == "__main__":
#     demo = Solution()
#     nums = [10, 9, 2, 5, 3, 7, 101, 18]
#     print(demo.lengthOfLIS(nums))



'''
零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来
计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
'''


#思路https://blog.csdn.net/cy_believ/article/details/104742610

class Solution:
    def coinChange(self, coins, amount):

        memo = dict()

        # 备忘录算法
        def dfs(n):

            if n in memo: return memo[n]

            if n == 0:
                return 0
            if n < 0:
                return -1

            res = float("inf")

            for coin in coins:

                sub_problem = dfs(n - coin)

                # 子问题无解，跳过
                if sub_problem == -1:
                    continue

                # res记录子问题的最优解
                res = min(res, 1 + sub_problem)

            if res == float("inf"):
                return -1
            else:
                memo[n] = res
                return res
        return dfs(amount)