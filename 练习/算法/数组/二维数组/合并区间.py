'''合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。


示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。'''



#先把所有区间按照开始位置排序，准备结果列表，
# 逐个遍历，查看新加入结果列表的区间是否与结
# 果列表最后一个区间重合，若重合则更新，否则直接加入结果列表。

'''
list表append方法
二位数组取值方法

'''

class Solution:
    def merge(self, intervals):
        """
        :param intervals: List[List[int]]
        :return: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            print(interval)
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
                print(merged)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged


if __name__ == "__main__":
    demo = Solution()
    intervals = [[1, 4], [4, 5]]
    print(demo.merge(intervals))