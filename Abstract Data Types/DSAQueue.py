import numpy as np
from ADTs.dblDSAList import *

class DSAQueue(object):
    def __init__(self):
        # self.default_cap = in_default_cap
        self.queue = DSALinkedList()

    def isEmpty(self):
        empty = self.queue.isEmpty()
        return empty

    def peek(self):
        if self.isEmpty():
            print("DSA Queue is empty.")
            topVal = None
        else:
            topVal = self.queue.peekFirst()
        return topVal

class DSAShuffleQueue(DSAQueue):
# -- CONSTRUCTOR -- #
    def __init__(self):
        DSAQueue.__init__(self) # to borrow properties and methods from parent class (may not be necessary)

# -- MUTATORS -- #
    def enqueue(self, value): # "insert
        self.queue.insertLast(value)

    def dequeue(self): # "remove"
        if self.queue.isEmpty():
            print("Shuffle queue is empty.\n")
        else:
            self.queue.removeFirst()



