'''
直线上最多的点数
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
https://www.freesion.com/article/1939833123/
'''

#
# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#
#         if len(points) < 3:
#             return len(points)
#
#         res = 0
#         for index, point1 in enumerate(points):
#             x1, y1 = point1
#             param_dict = {}
#             same_point_cnt = 1
#             for point2 in points[index + 1:]:
#                 x2, y2 = point2
#
#                 part1 = y2 - y1
#                 part2 = x2 - x1
#
#                 if part1 == 0 and part2 == 0:
#                     same_point_cnt += 1
#                     continue
#
#                 flag = False
#                 for key in param_dict:
#                     if part1 * key[1] == part2 * key[0]:
#                         param_dict[key] += 1
#                         flag = True
#                         break
#
#                 if not flag:
#                     param_dict[(part1, part2)] = 1
#
#             if param_dict:
#                 same_line_cnt = max(param_dict.values())
#             else:
#                 same_line_cnt = 0
#
#             res = max(res, same_line_cnt + same_point_cnt)
#
#         return res



'''
分数到小数(python3)
描述
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例

输入: numerator = 1, denominator = 2
输出: "0.5"

输入: numerator = 2, denominator = 3
输出: "0.(6)"
'''

#使用divmod获取商和余数. 然后通过余数求小数.
#不断将余数*10, 再次调用divmod, 则算出来的商就是小数.
#如果重复出现小数, 则说明为循环.
#
# class Solution:
#     def fractionToDecimal(self, numerator: int, denominator: int) -> str:
#         # 求整数 n保存取整部分；remainder保存取余部分
#         n, remainder = divmod(abs(numerator), abs(denominator))
#         sign = '-' if numerator*denominator < 0 else ''
#         fraction = [sign+str(n)]
#         if remainder == 0:
#             return ''.join(fraction)
#
#         fraction.append('.')
#         dic = {}
#         # 求小数
#         while remainder != 0:
#             # 出现过, 则说明进入循环.
#             if remainder in dic:
#                 fraction.insert(dic[remainder], '(')
#                 fraction.append(')')
#                 break
#             dic[remainder] = len(fraction)
#             n, remainder = divmod(remainder*10, abs(denominator))
#             fraction.append(str(n))
#             print(fraction)
#         return ''.join(fraction)



'''
阶乘后的零
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。
'''
'''阶乘后的零：给定一个整数 n，返回 n! 结果尾数中零的数量。
说明: 你算法的时间复杂度应为 O(log n) 。
思路：
结果末尾的0只可能由5*2，5*4，5*6和5*8得来，往小了说就是5*2，因此找
出可能有多少个5是本题的关键。因为限制了时间复杂度，因此使用这样的思路，没有限制的话，第一开始想到的是暴力法。'''
#
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n < 5:
#             return 0
#         result = 0
#         while n >= 5:
#             n = (n // 5)
#             result = result + n
#         return result





'''
颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。

 

示例 1：

输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
     因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
示例 2：

输入：11111111111111111111111111111101
输出：10111111111111111111111111111111
解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
     因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。
'''


'''
bin(n)：将十进制数转换为二进制字符串，不过字符串首段有“0b”字符；
s.rjust(32, '0')：将字符串s补全为长度为32的字符串，s右对齐，不够的地方用字符“0”补全；
int(x, base=2)：将二进制字符串转换为十进制数。
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         return int(bin(n)[2:].rjust(32, '0')[::-1], base=2)





'''
位1的个数




编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

 

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
 

进阶：

如果多次调用这个函数，你将如何优化你的算法？
 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
'''

#位与的思想

# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         ans = 0
#         while n!=0:
#             if n&1:
#                 ans += 1
#             n >>= 1
#         return ans




'''计算质数

统计所有小于非负整数 n 的质数的数量。

 

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0

'''


'''
厄拉多塞筛法
要寻找到正整数n为止的质数个数，构造一个长度为n的向量output，output[i]表示
正整数i是否是质数，初始化这个向量中所有的元素为1（True）。
output前两个数置零（1和2不是质数），遍历从2开始到suqare(n)+1范围内的所有正
整数i，将output向量中所有是i的正整数倍（大于1）的数所在位置全部置零。
循环结束后得到的output向量即可代表相应位置的每一个正整数是否为质数，求和即为结果。。'''

# class Solution(object):
#
#     def countPrimes(self, n):
#
#         if n <= 2:
#             return 0
#         output = [1] * n                                        # 首先生成一个全部为1的列表
#         output[0], output[1] = 0, 0
#         for i in range(2, int(n**0.5)+1):
#             if output[i] == 1:                                  # 如果i为质数
#                 output[i*2:n:i] = [0] * len(output[i*2:n:i])    # 将i的倍数置为0
#                 # print(i, output)
#         return sum(output)



'''

缺失数字


给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
进阶：
你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
'''

#set方法
# class Solution():
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return (set(range(len(nums) + 1)) - set(nums)).pop()

#0～n，满足等差数列公式
# class Solution():
#     def missingNumber(self, nums):
#         return (len(nums) * (len(nums) + 1) // 2) - sum(nums)



'''
3的幂



给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
示例 1：

输入：n = 27
输出：true
示例 2：

输入：n = 0
输出：false
'''

'''
%运算符
'''
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n == 0:
#             return False
#         if n == 1:
#             return True
#         if n == 2:
#             return False
#         while n != 1:
#             if n % 3 == 0:
#                 n = n // 3
#             else:
#                 return False
#         return True

if __name__ == "__main__":
    demo = Solution()
    print(demo.isPowerOfThree(27))