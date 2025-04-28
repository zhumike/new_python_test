class Solution:
    """
    使用异或算法
    """
    def singleNumber(self,nums):
        res =0
        for i in nums:
            res^=i
        return res
if __name__ == '__main__':
    s1= Solution()
    l1=[5,5,3,7,3,1,1,]
    result=s1.singleNumber(l1)
    print(result)

