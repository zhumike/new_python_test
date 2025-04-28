'''
判断一个链表是否是回文结构，如果是返回 True，否则返回 False
比如，给出一个链表为[2, 5, 12, 198, 12, 5, 2]，返回 True，
给定链表[2, 5, 12, 198, 12, 54, 20]，返回 False。

方法1：空间复杂度为 o(n)，使用一个栈，将链表中的数据全部push 到栈里，然后再迭代一遍链表，取出栈里的值逐个相互比较，如果不一样则说明不是回文链表。
'''

class Solution():
    def is_palindrome1(head):
        '''
        判断一个链表是否是回文结构，如果是返回 True，否则返回 False
        方法1：时间复杂度o(n),空间复杂度o(n)
        '''
        if head == 0 or head.next == 0:
            return True
        p = head
        stack = Stack()  # 自定义的 Stack 数据结构，也可以使用python内置的 list来实现
        while p != 0:
            stack.push(p.value)
            p = p.next
        p = head
        while p != 0:
            if p.value != stack.pop():
                return False
            p = p.next
        return True
