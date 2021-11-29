from ADTs.DSAList import DSALinkedList

class DSAStack:
    def __init__(self, in_default_cap=100):
        self.stack = DSALinkedList()

    def isEmpty(self):
        empty = self.stack.isEmpty()
        return empty

    def push(self, val):
        self.stack.insertFirst(val)

    def pop(self):
        topVal = self.stack.removeFirst() #peekfirst not needed bc already returns
        return topVal

    def top(self):
        topVal = self.stack.peekFirst()
        return topVal 

