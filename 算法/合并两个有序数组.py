"""直接通过切片+sort()实现"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:m + n] = nums2[:n]
        nums1.sort()
        return nums1



"""从后往前比较排序
将最大的值依次放到最后"""




# class Solution:
#     def merge(self,nums1,m,nums2,n) :
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         pointer1 = m - 1
#         pointer2 = n - 1
#         pointer_res = m + n - 1
#         while pointer1 >= 0 and pointer2 >= 0:
#             if nums1[pointer1] >= nums2[pointer2]:
#                 nums1[pointer_res] = nums1[pointer1]
#                 pointer1 -= 1
#             else:
#                 nums1[pointer_res] = nums2[pointer2]
#                 pointer2 -= 1
#             pointer_res -= 1
#         if pointer2 != -1:
#             nums1[:pointer2 + 1] = nums2[:pointer2 + 1]
#         return nums1






if __name__ =="__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s1 = Solution()
    print(s1.merge(nums1,m,nums2,n))
