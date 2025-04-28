# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python_test
# @File     :两数相加
# @Date     :2023/6/20 10:36
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

"""

#Definition for singly-linked list
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 进位符号
        carry=0
        #result用于返回结果list的头节点，head用于遍历
        head=result=ListNode(0)
        #如果l1和l2没有被遍历完，或者有一个进位，继续循环
        while l1 or l2 or carry:
            t= l1.val if l1 else 0
            t+=(l2.val if l2 else 0)
            head.next=ListNode((t+carry)%10) #将两个list的相同位数相加，再加上carry，再对10取模，就得到结果list对应位数的值
            head=head.next #让head始终是结果list的最后一个节点
            carry=1 if t+carry>=10 else 0 #carry的取值只能是0或者1
            l1=l1.next if l1 else l1
            l2=l2.next if l2 else l2
        return result.next
