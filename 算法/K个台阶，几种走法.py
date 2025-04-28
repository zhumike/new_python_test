'''有n步台阶，一次只能上1步或2步，共有多少种走法'''
'''分析
1、n=0 和 n=1 的时候 并没有其他可选择的，所以可以得出f(0)=0;f(1)=1; 
2、n>2时情况就变复杂起来，但是这个时候可以操作的步骤也就2种 
也就是走1步(n-1)与走2步(n-2)。所以可以得到f(n)=f(n-1)+f(n-2); 
从当前状态转为下一状态的通用算法既可。 
3、 验证，使用2以上的数字验证几次。'''


#递归算法
# class  Solution():
#     def footstep(self, n):
#         if n <=2:
#             return n
#         else:
#             return self.footstep(n - 1) + self.footstep(n - 2)

#迭代算法
# class  Solution():
#     def footstep(self, n):
#         if n <= 2:
#             return n
#         f=1
#         s=2
#         t=0
#         for i in range(3,n+1):
#             t=f+s
#             f=s
#             s=t
#         return  t
#
# if __name__=="__main__":
#     demo = Solution()
#     k=1000
#     print(demo.footstep(k))
