class solutionMethod:
    def bubble_sort(self,arr):
        n = len(arr)
        # 遍历所有数组元素
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]



#改良版本

"""
因为冒泡排序必须要在最终位置找到之前不断
交换数据项，所以它经常被认为是最低效的排
 序方法。这些 “浪费式” 的交换操作消耗了
 许多时间。但是，由于冒泡排序要遍历整个
 未排好的 部分，它可以做一些大多数排序方
 法做不到的事。尤其是如果在整个排序过程中
 没有交换，我们就可断定列表已经排好。因此
 可改良冒泡排序，使其在已知列表排好的情况
 下提前结束。这就是说，如果一个列表只需要几次遍
 历就可排好，冒泡排序就占有优势：它可以在
 发现列表已排好时立刻结束。

"""
# 冒泡排序改良版本
def bubbleSort(alist):
    n = len(alist)
    exchange = False
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        # 如果发现整个排序过程中没有交换，提前结束
        if not exchange:
            break
    return alist

if __name__=="__main__":
    demo = solutionMethod()
    arr = [3, 2, 0, 7, 4]
    demo.bubble_sort(arr)
    print(arr)