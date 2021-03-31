import numpy as np

class DSAStack:
    def __init__(self, in_default_cap=100):
        self.default_cap = in_default_cap
        self.stack = np.empty(self.default_cap, dtype = object)
        self.count = 0

    def set_default_capacity(self, cap):
        self.stack.resize(cap)

    def isEmpty(self):
        empty = (self.count == 0)
        return empty
    
    def isFull(self):
        full = (self.count >= self.default_cap)
        return full

    def push(self, val):
        if self.isFull():
            print("Stack is full")
        else:
            self.stack[self.count] = val
            self.count += 1

    def pop(self):
        topVal = self.top()
        self.stack[self.count-1] = None
        self.count -= 1
        return topVal

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            topVal = None
        else:
            topVal = self.stack[self.count-1]
        return topVal 

