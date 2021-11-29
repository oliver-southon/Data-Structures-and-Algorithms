class DSAListNode():
    def __init__(self, inValue):
        self._value = inValue
        self._next = None 
    
    #for easier printing 
    def __repr__(self):
        return self._value

class DSALinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        nodeArray = []
        node = self._head
        while node != None:
            nodeArray.append(node._value)
            node = node._next
        nodeArray.append("None")
        return " -> ".join(nodeArray)

    #############################
    #--ACTIVITY 3: LL Iterator--#
    #############################
    def __iter__(self):
        # use yield instead of return, since iterating 
        node = self._head
        while node != None: #if true, end is reached
            yield node #yield current node
            node = node._next #move to next node
    ##############################
    ##############################

    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self._head = newNd
        else:
            newNd._next = self._head
            self._head = newNd

    def insertLast(self, newValue):
        newNode = DSAListNode(newValue)
        #if empty, new head is node
        if self.isEmpty():
            self._head = newNode
        else:
            #a) iterate until exception raised...
            currNd = self._head
            while currNd._next != None:
                currNd = currNd._next
            #b) and then set current node as last node
            currNd._next = newNode

    def isEmpty(self):
        empty = (self._head == None) 
        return empty

    def peekFirst(self):
        if self.isEmpty():
            print("List is empty.")
        else:
            nodeValue = self._head._value
        return nodeValue

    def peekLast(self):
        if self.isEmpty():
            print("List is empty.")
            nodeValue = None
        else:
            currNd = self._head
            while currNd._next != None:
                currNd = currNd._next
            nodeValue = currNd._value
        return nodeValue

    def removeFirst(self):
        #Check if empty
        if self.isEmpty():
            print("List is empty.")
            nodeValue = None
        else:
            nodeValue = self._head._value
            self._head = self._head._next
        return nodeValue

    def removeLast(self):
        #Check if empty
        if self.isEmpty():
            print("List is empty.")
            nodeValue = None
        #if list has one item
        elif self._head._next == None:
            nodeValue = self._head._value
            self.head = None
        #if list has more than one item
        else:
            #get second-last node, and set that as the last one
            prevNd = None
            currNd = self._head
            while currNd._next != None:
                prevNd = currNd
                currNd = currNd._next
            prevNd._next = None
            nodeValue = currNd._value
        return nodeValue






