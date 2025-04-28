"""
https://zhuanlan.zhihu.com/p/40695917
算法思想：
但其工作原理稍有不同。它总是保持一个位置靠前的 已排好的子
表，然后每一个新的数据项被 “插入” 到前边的子表里，排好的子表增加一项。我们认为只含有一个数据
项的列表是已经排好的。每排后面一个数据（从 1 开始到 n-1），这 个的数据会和已排好子表中的数据
比较。比较时，我们把之前已经排好的列表中比这个数据大的移到它的右边。当子表数据小于当前数据，或
者当前数据已经和子表的所有数据比较了时，就可以在此处插入当前数据项。
"""

# 插入排序
def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue=alist[i]
        position=i
        while alist[position-1]>currentvalue and position>0:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue
    return alist