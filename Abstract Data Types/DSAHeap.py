import numpy as np
import math

class DSAHeapEntry():
    def __init__(self, inPriority, inValue):
        self.priority = inPriority 
        self.value = inValue

    def __repr__(self):
        return (str(self.priority) + " -> " + str(self.value))

# MAX Heap
class DSAHeap():
    def __init__(self, maxSize):
        self.heap = np.empty([maxSize], dtype='object') # object array of DSAHeap entries
        self.count = 0

    def add(self, priority, value):
        # >1. add to array
        newEntry = DSAHeapEntry(priority, value)
        self.heap[self.count] = newEntry
        # >2. trickle up
        self.trickleUp(self.count)
        self.count += 1

    def remove(self):
        copyElement = self.heap[0] # get root element
        lastElement = self.heap[self.count-1] # get last element in heap array
    
        self.heap[0] = lastElement # set root to be the last element
        self.trickleDown(0) # trickle the rest down

        self.count -= 1 # decrement count
        self.heap[self.count] = None # clear last element
        return copyElement

    def heapify(self):
        for i in range(int((self.count / 2) - 1), 0, -1):
            self.trickleDown(i)

    def heapSort(self):
        self.heapify()
        for i in range(self.count-1, 0):
            self.swapnodes(self.heap[0], self.heap[i])
            self.trickleDown(0)

    def trickleUp(self, curIdx): 
        # RECURSIVE
        parentIdx= int((curIdx-1)/2)
        if curIdx > 0:
            curPrior = self.heap[curIdx]
            parPrior = self.heap[parentIdx]
            if curPrior.priority > parPrior.priority:
                temp = self.heap[parentIdx]
                self.heap[parentIdx] = self.heap[curIdx]
                self.heap[curIdx] = temp
                self.trickleUp(parentIdx)

    def trickleDown(self, curIdx):
        # ITERATIVE
        lChildIdx = curIdx * 2 + 1
        rChildIdx = lChildIdx + 1
        keep_going = True
        while keep_going and lChildIdx < self.count:
            keep_going = False
            largeIdx = lChildIdx
            if rChildIdx < self.count:
                if self.heap[curIdx]: # checks if not none
                    if self.heap[lChildIdx].priority < self.heap[curIdx].priority:
                        largeIdx = rChildIdx
            if self.heap[curIdx]:
                if self.heap[largeIdx].priority > self.heap[curIdx].priority:
                    self.swapnodes(largeIdx, curIdx)
                    keep_going = True
            curIdx = largeIdx
            lChildIdx = curIdx * 2 + 1
            rChildIdx = lChildIdx + 1

    def display(self):
        row_count = math.log(self._getRowCount(len(self.heap)+1), 2)-1
        print('[' + str(self.heap[0].priority) + ']') # print rood node
        row_length = 2
        index = 1
        i = 0
        while i < row_count:
            self._display(self.heap, row_length, index)
            index = index * 2 + 1
            row_length = row_length * 2
            i += 1

        
    def _display(self, arr, row_length, index):
        spaces_filled = 0
        row = []
        while spaces_filled < row_length:
            try:
                row.append(arr[index].priority)
                index += 1
                spaces_filled += 1
            except (IndexError, AttributeError):
                spaces_filled += 1
                row.append(None)
        print(row)

    def _getRowCount(self, n):
        count = 0
        if (n and not(n & (n - 1))):
            return n   
        while( n != 0):
            n >>= 1
            count += 1
        return 1 << count

    def swapnodes(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

