import heapq
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆  小顶堆
print(heap)

print(heap[0]) #获取小顶堆的最小值
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果


