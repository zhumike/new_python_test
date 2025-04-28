# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :合并区间
# @Date     :2023/6/20 18:00
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""

"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 

提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    def merge(self, intervals) :
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空,或者当前区间与上一区间不重合,直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话,我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

if __name__ == '__main__':
    ls = [[1,4],[4,5]]
    ob = Solution()
    print(ob.merge(ls))