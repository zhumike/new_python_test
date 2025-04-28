'''
数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''

# class Solution():
#     def findKthLargest(self,nums,k):
#         """
#         nums: List[int]
#         k: int
#         return:返回数组排序后的第k个最大的元素，不是第k个不同的元素；
#         """
#         # 查看输入内容是否符合要求
#         if k >= 1 and k <= len(nums) and len(nums) > 0:
#             nums_ = sorted(nums,reverse = True)
#             result = nums_[k-1]
#         else:
#             print('error：输入内容不符合要求')
#         return result
# if __name__ == "__main__":
#     demo = Solution()
#     k=3
#     nt = [45,98,-2,6,87,-9]
#     result=demo.findKthLargest(nt, k)
#     print(result)
#
#

'''
数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:
如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

'''
#思路我们可以通过sort()函数来实现，当然，这就需要一个list
# 　　　　读取数据流，我们将数据流的元素全部用append方法添加到list中，再用sort()函数进行排序
# 　　　　读取数据的中位数：计算数据流的长度，如果除以2有余数说明是奇数，那么返回中间位置元素
# 　　　　如果等于0，没有余数，那么返回中间位置元素以及右移一位元素相加之后除以2的结果，完成所有操作
# 双堆策略法   https://cloud.tencent.com/developer/article/1686135

# import heapq
#
#
# class MedianFinder(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.len = 0
#         # 小顶堆
#         self.minheap = []
#         # 大顶堆
#         self.maxheap = []
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         # 加入一个数，长度加1
#         self.len += 1
#         # 首先明确的是python中的heapq是小顶堆
#         # heappushpop：将num放入堆中，然后弹出并返回heap的最小元素。
#         # heappush：将item的值加入heap中，保持堆的不变性。
#         # heappop：弹出并返回heap的最小的元素，保持堆的不变性。
#         heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))
#         if len(self.maxheap) > len(self.minheap):
#             heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
#         print("小顶堆：", self.minheap)
#         print("大顶堆：", self.maxheap)
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if self.len & 1 == 0:
#             return (self.minheap[0] - self.maxheap[0]) / 2.0
#         return self.minheap[0]
#
# m=MedianFinder()
# m.addNum(4)
# print("中位数：",m.findMedian())
# m.addNum(1)
# print("中位数：",m.findMedian())
# m.addNum(5)
# print("中位数：",m.findMedian())
# m.addNum(2)
# print("中位数：",m.findMedian())
# m.addNum(7)
# print("中位数：",m.findMedian())

# class Solution:
#     def Insert(self, num):
#         mid = self.GetMedian(num)
#         return mid
#
#     def GetMedian(self, num):
#         num = self.getsort(num)
#         if len(num) % 2 == 1:
#             mid = num[len(num) // 2]
#         else:
#             mid = (num[len(num) // 2] + num[(len(num) - 1) // 2]) / 2
#         return mid
#
#     def getsort(self, num):
#         for i in range(len(num) - 1):
#             for j in range(i + 1, len(num)):
#                 if num[i] > num[j]:
#                     num[i], num[j] = num[j], num[i]
#         return num
#
# if __name__ == '__main__':
#     s = Solution()
#     num = [1, 5, 7, 4, 6, 2, 8, 3]
#     mid = s.Insert(num)
#     print(mid)

'''有序矩阵中第K小的元素
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
示例 1：

输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
'''



'''转化为list排序后算出'''
# class Solution:
#     def kthSmallest(self, matrix, k):
#         my_list = []
#         for tmp in matrix:
#             my_list += tmp
#         my_list = sorted(my_list)
#         return my_list[k-1]



#二分法  https://www.cnblogs.com/yiluolion/p/13226963.html

# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         def search(mid, n):
#             # 从左下角开始往右上角找
#             i, j = n - 1, 0
#             # 统计小于或等于 mid 的元素个数
#             count = 0
#             while i >= 0 and j < n:
#                 if matrix[i][j] <= mid:
#                     # 当此时元素小于等于 mid
#                     # 那么该元素往上的所有元素都会小于或等于 mid
#                     count += (i + 1)
#                     # 向右移动，继续比较
#                     j += 1
#                 else:
#                     # 当此时元素大于 mid 时，说明这个元素不包含在内，往上移动
#                     i -= 1
#             # count 与 k 值比对，判断所求元素落在哪边
#             return count >= k
#
#         n = len(matrix)
#
#         left, right = matrix[0][0], matrix[n - 1][n - 1]
#
#         while left < right:
#             mid = left + (right - left) // 2
#             if search(mid, n):
#                 # 当 count 大于等于 k 时，表明答案落在 [left, mid]
#                 # 否则落在 [mid+1, right]
#                 right = mid
#             else:
#                 left = mid + 1
#
#         return left



'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''


#可以用𝑑𝑖𝑐𝑡来统计最后用𝑠𝑜𝑟𝑡𝑒𝑑方法来排序取出前k个即可
#
# 或者用𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑜𝑖𝑛𝑠里面的𝐶𝑜𝑢𝑛𝑡𝑒𝑟，调用most_common方法

import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = collections.Counter(nums)
        return [x[0] for x in l.most_common(k)]

# if __name__ == "__main__":
#     num = [1,1,1,2,2,3]
#     k = 2
#     demo = Solution()
#     print(demo.topKFrequent(num,k))
#


'''滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
'''

#循环遍历  本质用的是max函数
# class Solution:
#     def maxInWindows(self, num, size):
#         # write code here
#             if size<=0:
#                 return []
#             a=[]
#             for i in range(0,len(num)-size+1):
#                 a.append(max(num[i:i+size]))
#             return a
# if  __name__ == "__main__":
#     demo = Solution()
#     nums = [1,3,-1,-3,5,3,6,7]
#     k = 3
#     print(demo.maxInWindows(nums,k))


'''
python内置的堆是最小堆，所以在元素入堆的时候取负，以便求最大值。
另外我们需要判断最大值是否在当前的窗口内，所以需要索引值，在入堆
的时候一起存入。每次取堆内最大值，也就是堆顶元素的时候，检查索引
值是否是在窗口内的。

'''

# import  heapq
# class Solution:
#     def maxSlidingWindow(self, nums, k) :
#         res, heap = [], []
#         for i in range(len(nums)):
#             heapq.heappush(heap, (-nums[i], i))
#             if i + 1 >= k:
#                 while heap and heap[0][1] < i + 1 - k:
#                     heapq.heappop(heap)
#                 res.append(-heap[0][0])
#         return res
#         print (heap)
# if  __name__ == "__main__":
#     demo = Solution()
#     nums = [1,3,-1,-3,5,3,6,7]
#     k = 3
#     print(demo.maxSlidingWindow(nums,k))


#基本计算器 II
'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
示例 :
输入: "3+2*2"，输出: 7
输入: " 3/2 "，输出: 1
输入: " 3+5 / 2 "，输出: 5
说明：
你可以假设所给定的表达式都是有效的。
'''

#思路：把所有加减乘除运算转化“加法”运算
# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # 遇到加减，先保存元素结果；遇到乘除，则直接计算出结果
#         stack = []  # 用于存储每一步的运算结果
#         opera = '+'  # 设定初始运算为加法
#
#         num = 0
#         s += '+'
#         for str in s:
#             if str == ' ':
#                 continue
#             # 遇到数字后，继续看后面是否还是如此
#             if str in '0123456789':
#                 # 这里num*10操作的目的，是为了处理除个位数之外多位数，eg, 12, 437
#                 num = num * 10 + int(str)
#                 continue
#
#             if opera == '+':
#                 stack.append(num)
#             elif opera == '-':
#                 stack.append(-num)
#             elif opera == '*':
#                 # 遇到*，直接取出上一步运算的结果stack[-1]跟num相乘
#                 stack[-1] *= num
#             elif opera == '/':
#                 # 遇到/，直接取出上一步运算的结果stack[-1]跟num做整除处理
#                 stack[-1] = stack[-1] // num
#             opera = str
#             num = 0
#         return sum(stack)
# if  __name__ == "__main__":
#     demo=Solution()
#     print(demo.calculate("3+2*2"))


'''
扁平化嵌套列表迭代器
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
'''

'''
为了解决这个问题，我们将遵循以下步骤-

在初始化部分，它将获取嵌套列表，其工作方式如下：

将res设置为空列表，索引：= 0，调用getVal(nestedList)

该getVal()会采取nestedIntegers，这将作为工作-

为我在nestedIntegers

如果i是整数，则将i插入res数组，否则调用getVal（i列表）

该next()方法将返回索引所指向的值，并将索引增加1

hasNext()当旁边有一个元素时，它将返回true，否则返回false

'''
#递归思路
class NestedIterator(object):
   def __init__(self, nestedList):
      self.res = []
      self.index = 0
      self.getVal(nestedList)
      #print(self.res)
   def getVal(self,NestedList):
      for item in NestedList:
         if isinstance(item, int):
            self.res.append(item)
         else:
            self.getVal(item)
   def next(self):
      self.index+=1
      return self.res[self.index-1]
   def hasNext(self):
      if self.index == len(self.res):
         return False
      return True
ob = NestedIterator([[1,1],2,[1,1]])
while ob.hasNext():
   print(ob.next())
print(ob.res)