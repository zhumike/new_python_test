'''
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''

#两次遍历
#先遍历一次用两个数组分别记录有0的行和列，再遍历一次清零。

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        a = []
        b = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    a.append(i)
                    b.append(j)
        #清除含有0的行
        for i in a:
            for j in range(m):
                matrix[i][j] = 0
        #清除含有0的列
        for i in b:
            for j in range(n):
                matrix[j][i] = 0