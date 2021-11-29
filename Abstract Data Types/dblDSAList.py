class Error(Exception):
    pass

class ListError(Error):
    pass

class DSAListNode():
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.previous = None

    #ACCESSORS
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    #MUTATORS
    def setValue(self, newVal):
        self.value = newVal
    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious
    
    #for easier printing 
    def __repr__(self):
        return self.value

#   "has a"
#  ^
#  |
# --

class DSALinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __repr__(self):
        nodeArray = []
        node = self.head
        while node != None:
            nodeArray.append(node.value)
            node = node.next
        # nodeArray.append("None")
        return " -> ".join(nodeArray)

    def __iter__(self):
        # use yield instead of return, since iterating 
        cur = self.head
        while cur: #if true, end is reached
            yield cur.value
            cur = cur.next

    def getCount(self):
        return self.count

    def insertFirst(self, newValue):
        # >1. make new value a node object
        newNode = DSAListNode(newValue)
        if self.tail == None:
            self.tail = newNode 
            self.head = self.tail
        else:
            # >2. set next/prev of newNode
            newNode.next = self.head
            newNode.previous = None
            #if head doesn't point to anything ie one obj in list
            if self.head == None:
                self.head.previous = newNode
            self.head = newNode
        self.count += 1

    def insertLast(self, newValue):
        #make new value a node object
        newNode = DSAListNode(newValue)
        #if head doesn't point to anything ie one obj in list
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            #set head as next
            newNode.previous = self.tail

            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def isEmpty(self):
        empty = (self.head == None) 
        return empty

    def peekFirst(self):
        #Check if empty
        if self.isEmpty():
            print("List is empty.")
        else:
            #first nodeVal
            nodeValue = self.head.value
        return nodeValue

    def peekLast(self):
        #Check if empty
        if self.isEmpty():
            print("List is empty.")
            nodeValue = None
        #Traverse to last node, then return it
        else:
            nodeValue = self.tail.value
        return nodeValue

    def removeFirst(self):
        #Check if empty
        if self.isEmpty():
            print("List is empty.")
            nodeValue = None
        else:
            #nodeVal will be head's value, and head will be next val
            nodeValue = self.head.value
            self.head = self.head.next
        self.count -= 1
        return nodeValue

    def removeLast(self):
        #Check if empty
        if self.isEmpty():
            print("List is empty.")
            nodeValue = None
        #if list has one item
        elif self.head.next == None:
            nodeValue = self.head.value
            self.head = None
        #if list has more than one item
        else:
            #get second-last node, and set that as the last one
            prevNd = None
            currNd = self.head
            while currNd.next != None:
                prevNd = currNd
                currNd = currNd.next
            prevNd.next = None
            nodeValue = currNd.value
        self.count -= 1
        return nodeValue






