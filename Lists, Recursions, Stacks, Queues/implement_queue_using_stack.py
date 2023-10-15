# implement queues using two stacks

class MyQueue(object):

    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.first_stack) > 0:
            self.second_stack.append(self.first_stack.pop())
        result = self.second_stack.pop()
        while len(self.second_stack) > 0:
            self.first_stack.append(self.second_stack.pop())
        return result
        

    def peek(self):
        """
        :rtype: int
        """
        while len(self.first_stack) > 0:
            self.second_stack.append(self.first_stack.pop())
        result = self.second_stack[-1]
        while len(self.second_stack) > 0:
            self.first_stack.append(self.second_stack.pop())
        return result
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()