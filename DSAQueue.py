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
    def __init__(self):
        super().__init__()

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
      #Constructor
    def __init__(self):
        super().__init__()
        self.head = 0
        self.tail = 0
        self.maxSize = self.default_cap

    #Adding elements to the queue
    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            print ("Queue Full!")
        elif (self.head != 0): # if it has been dequeued
            self.queue[self.head-1] = data
        else:
            self.queue[self.count] = data
            self.tail = (self.tail + 1) % self.maxSize
            self.count += 1

    #Removing elements from the queue
    def dequeue(self):
        if self.size()==0:
            print("Queue Empty!") 
        else:
            data = self.queue[self.head]

            for element in self.queue:
                if element == data:
                    self.queue[element-1] = None

            self.head = (self.head + 1) % self.maxSize
            self.count -= 1
        return data

    #Calculating the size of the queue
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))

# Q = DSAShuffleQueue()
# Q.set_default_capacity(5)
# Q.enqueue(1)
# Q.enqueue(2)
# Q.enqueue(3)
# print(Q.queue)
# print(Q.queue)
# print(Q.peek())
# Q.dequeue()
# print(Q.queue)
# print(Q.peek())


# print(Q.count)
# # Q.printStuff()

# # Q.enqueue(1)
# # print(Q.queue)


