import numpy as np

class DSAQueue(object):
    default_cap = 100

    def __init__(self):
        # self.default_cap = in_default_cap
        self.queue = np.empty(self.default_cap, dtype = object)
        self.count = 0

    def set_default_capacity(self, cap):
        self.queue.resize(cap)
        self.default_cap = cap

    def isEmpty(self):
        empty = (self.count == 0)
        return empty
    
    def isFull(self):
        full = (self.count >= self.default_cap)
        return full

    def peek(self):
        if self.isEmpty():
            print("DSA Queue is empty.")
            topVal = None
        else:
            topVal = self.queue[0]
        return topVal

class DSAShuffleQueue(DSAQueue):
# -- CONSTRUCTOR -- #
    def __init__(self):
        DSAQueue.__init__(self) # to borrow properties and methods from parent class (may not be necessary)

# -- MUTATORS -- #
    def enqueue(self, value): # "insert"
        if self.isFull():
            print("Shuffle queue is full.\n")
        else:
            self.queue[self.count] = value
            self.count += 1

    def dequeue(self): # "remove"
        if self.isEmpty():
            print("Shuffle queue is empty.\n")

        # Avoids error when dequeueing a full queue
        elif self.isFull(): 
            self.set_default_capacity(self.count+1) # add extra slot at end

            for i in range (0, self.count):
                self.queue[i] = self.queue[i+1]

            self.set_default_capacity(self.count) # removes extra slot
            self.queue[-1] = None
            self.count -= 1

        else:
            for i in range (0, self.count):
                self.queue[i] = self.queue[i+1]

            self.count -= 1

class DSACircularQueue(DSAQueue):
# -- CONSTRUCTOR - -#
    def __init__(self):
        self.queue = []
        self.maxSize = 0
        self.head = 0
        self.tail = 0

# -- SETTERS - -#
    def set_default_capacity(self, cap):
        self.maxSize = cap

# -- GETTERS -- #
    def peek(self):
        if self.getSize() == 0:
            print("DSA Queue is empty.")
            topVal = None
        else:
            topVal = self.queue[self.head]
        return topVal

    def getSize(self):
        if self.tail >= self.head:
            size = self.tail - self.head
        else:
            size = self.maxSize - (self.head - self.tail)
        # return the size of the queue
        return size

# -- MUTATORS -- #
    def enqueue(self, value):
        if self.getSize() == (self.maxSize - 1):
            print("Circular Queue is full!")
        else:
            self.queue.append(value) # add to queue
            self.tail = (self.tail+1) % self.maxSize # increment tail

        # remove element from the queue
    def dequeue(self):
        if self.getSize() == 0:
            print("Queue is empty!")
            headVal = None
        else:
            headVal = self.queue[self.head] # get head val
            self.head = (self.head+1) % self.maxSize # increment head
        return headVal




