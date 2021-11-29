from ADTs.dblDSAList import *
from ADTs.DSAStack import *
from ADTs.DSAQueue import *
from ADTs.DSATree import *
from ADTs.DSAHeap import *

class Error(Exception):
    pass

class LabelNotFoundError(Error):
    pass

class VertexNotFoundError(Error):
    pass

class DSAGraph():
    def __init__(self):
        self._vertices = DSALinkedList() # Each node in _vertices list will have its own adj. list
        self._edges = DSALinkedList() # Nodes are edge objects

    #################
    # - ACCESSORS - #
    #################

    def hasVertex(self, _label):
        hasVertex = False
        for curVert in self._vertices:
            if curVert._label == _label:
                hasVertex = True
        return hasVertex

    def getVertexCount(self):
        vertCount = self._vertices.getCount()
        return vertCount

    def getEdgeCount(self):
        edgeCount = self._edges.getCount()
        return edgeCount

    def getVertex(self, _label):
        # >1. Iter thru objects in DSAGraph
        for curVert in self._vertices:
            if curVert._label == _label:
                return curVert

    def getEdge(self, _label):
        chosenVert = self.getVertex(_label)
        return chosenVert._links

    def getEdgeObject(self, label1, label2):
        vert1 = self.getVertex(label1)
        vert2 = self.getVertex(label2)
        for edge in self._edges:
            if (edge._firstVert == vert1 and edge._secondVert == vert2) or (edge._firstVert == vert2 and edge._secondVert == vert1):
                return edge

    def getNeighbors(self, label1):
        neighbors = []
        for edge in self._edges:
            if edge._firstVert._label == label1:
                neighbors.append([edge._secondVert._label, edge._value])
            elif edge._secondVert._label == label1:
                neighbors.append([edge._firstVert._label, edge._value])
        return neighbors # return neighbor label and value between them
        

    def display(self):
        if self.getVertexCount() > 0:
            print("\n VERTEX      ADJ. LIST")
            print("=======================")
            for vertex in self._vertices:
                print(" " + str(vertex._label) + ", "  + str(vertex._value) + " --> " + str(vertex._links))
            print("=======================\n")
        else:
            raise VertexNotFoundError

    # Used if edges have objects
    def displayObjects(self):
        for edge in self._edges:
            print(edge)

    ################
    # - SEARCHES - #
    ################
    def depthFirst(self, v):
        old = DSAStack()
        self._depthFirstRec(old, v)

    def _depthFirstRec(self, old, v):
        print(v)
        # MAIN ALGORITHM
        v._visited = True
        for link in v._links:
            linkVert = self.getVertex(link)
            if linkVert._visited == True:
                pass
            elif linkVert not in old.stack and linkVert._visited == False:
                old.push(linkVert)
                
                linkVert._visited = True
                self._depthFirstRec(old, linkVert)
            elif linkVert in old.stack:
                old.pop()

    def breadthFirst(self, v):
        for vert in self._vertices:
            vert._visited = False
        T = []
        v._visited = True
        Q = DSAShuffleQueue()
        Q.enqueue(v)
        while Q.isEmpty() == False:
            v = Q.peek()
            Q.dequeue()
            for w in v._links:
                w = self.getVertex(w)
                if not w._visited:
                    if v not in T:
                        T.append(v)
                    if w not in T:
                        T.append(w)
                    w._visited = True
                    Q.enqueue(w)

        return T


    ################
    # - MUTATORS - #
    ################

    def addVertex(self, label, value):
        newVertex = DSAGraphVertex(label, value)
        self._vertices.insertLast(newVertex)
    def addEdge(self, label1, label2):
        # >1. Check labels exist in graph
        if self.hasVertex(label1) and self.hasVertex(label2):
            # >2. Find the vertex, then add edge   
            vert1 = self.getVertex(label1)
            vert1._links.append(label2)
            vert2 = self.getVertex(label2)
            vert2._links.append(label1)
        else:
            raise LabelNotFoundError

    # Used if you want values for your edges
    def addEdgeObj(self, label1, label2, value):
        self.addEdge(label1, label2)
        vert1 = self.getVertex(label1)
        vert2 = self.getVertex(label2)
        edge = DSAGraphEdge(vert1, vert2, value)
        self._edges.insertFirst(edge)

class DSAGraphVertex():
    def __init__(self, inLabel, inValue):
        self._label = inLabel
        self._value = inValue
        self._links = [] # adj list
        self._visited = False # Starts as unvisited

    def __repr__(self):
        return (str(self._label) + " - " + str(self._value))

    # SETTERS
    def setVisited(self, TorF):
        self._visited = TorF

    # GETTERS
    def getVisited(self):
        return self._visited

class DSAGraphEdge():
    def __init__(self, inFirstVert, inSecondVert, inValue):
        self._firstVert = inFirstVert
        self._secondVert = inSecondVert
        self._value = inValue

    def __repr__(self):
        return (str(self._firstVert._label) + " | " + str(self._secondVert._label) + " | " + str(self._value))




