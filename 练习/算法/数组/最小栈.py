"""
最小栈
描述：

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) – 将元素 x 推入栈中。
pop() – 删除栈顶的元素。
top() – 获取栈顶元素。
getMin() – 检索栈中的最小元素。

示例

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); --> 返回 -3.
minStack.pop();
minStack.top(); --> 返回 0.
minStack.getMin(); --> 返回 -2.
"""


#1.考察list结构的append()方法使用   2.list的pop()方法使用  3.list取末尾值方法的使用  xxx[-1]

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        self.stack.append(x)
        if self.min == None or self.min > x:
            self.min = x

    def pop(self):
        popItem = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
            return popItem

        if popItem == self.min:
            self.min = self.stack[0]
            for i in self.stack:
                if i < self.min:
                    self.min = i
        return popItem

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min

if __name__ == "__main__":
    demo = MinStack()
    demo.push(1)
    demo.push(2)
    demo.push(3)
    print(demo.getMin())