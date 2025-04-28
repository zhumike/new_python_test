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
class Solution:
    def intersect(self, nums1, nums2) :
        nums1.sort()
        nums2.sort()
        p = q = 0

        ans = []
        # 任意指针到达数组末尾，结束遍历
        while p < len(nums1) and q < len(nums2):
            # 在这里，先判断指针对应元素的大小
            # 当不相等时，指针对应元素小的移动
            # 相等时，将元素放入结果列表中，同时移动指针
            if nums1[p] > nums2[q]:
                q += 1
            elif nums1[p] < nums2[q]:
                p += 1
            else:
                ans.append(nums1[p])
                print(ans)
                p += 1
                q += 1
        return ans