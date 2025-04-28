"""普通算法，使用count函数"""

# class Solotion(object):
#     def searchMatrix(self,matrix,target):
#         if not matrix or matrix == [[]]:
#             return  False
#         for i in range(len(matrix)):
#             if matrix[i].count(target):
#                 return  True
#             if i == len(matrix) -1:
#                 return False
#             else:
#                 continue

"""遍历搜索方法"""


def search_matrix(matrix: list, target: int) -> bool:
    """
    :type matrix: list
    :type target: int
    :rtype: bool
    """
    for i in matrix:
        for j in i:
            if target < j:
                # 当要搜索的数字小于当前数字的时候，结束本次遍历，减少遍历次数
                break
            elif target == j:
                return True
            else:
                pass
    return False


if __name__ == '__main__':
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    t = 10
    print(search_matrix(m, t))
