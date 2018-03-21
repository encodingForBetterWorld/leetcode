# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = None
        self.stock = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min_val is None:
            self.min_val = x
        else:
            self.min_val = min(self.min_val, x)
        self.stock.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stock.pop()
        le = len(self.stock)
        if le == 0:
            self.min_val = None
        elif le > 1:
            self.min_val = min(*self.stock)
        else:
            self.min_val = self.stock[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stock[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print minStack.getMin()
print minStack.pop()
print minStack.top()
print minStack.getMin()