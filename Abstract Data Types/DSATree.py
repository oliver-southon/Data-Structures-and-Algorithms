class Error(Exception):
    pass

class InvalidKeyError(Error):
    pass

class DSATreeNode():
    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None

    def __str__(self):
        return ("Key: " + str(self._key) + " Value: " + str(self._value))

    def setLeft(self, node):
        self._left = node

    def setRight(self, node):
        self._right = node

class DSABinarySearchTree():
    def __init__(self):
        self._root = None # start with an empty tree

    def find(self, key):
        return self._findRec(key, self._root)

    def _findRec(self, key, cur):
        value = None
        if cur == None:
            raise InvalidKeyError("Key " + str(key) + " not found")
        elif key == cur._key: # Base case: found
            value = cur # assing value to 'cur' instead of 'cur._value' so we receive whole node object
        elif key < cur._key: # goes left
            value = self._findRec(key, cur._left)
        else: # goes right
            value = self._findRec(key, cur._right)
        return value

    def insert(self, key, data):
        return self._insertRec(key, data, self._root)

    def _insertRec(self, key, data, cur):
        if not self._root:
            newNode = DSATreeNode(key, data)
            self._root = newNode
        else:

            updateNode = cur
            if cur == None:
                updateNode = DSATreeNode(key, data)
            elif key == cur._key:
                raise InvalidKeyError("Key " + str(key) + " is already in the tree")
            elif key < cur._key:
                cur.setLeft(self._insertRec(key, data, cur._left))
            else:
                cur.setRight(self._insertRec(key, data, cur._right))
            return updateNode
        
    def delete(self, key):
        return self._deleteRec(key, self._root)

    def _deleteRec(self, key, cur):
        updateNode = cur
        if cur == None:
            raise InvalidKeyError("Not in tree.")
        elif key == cur._key:
            updateNode = self.deleteNode(key, cur)
        elif key < cur._key:
            cur.setLeft(self._deleteRec(key, cur._left))
        else:
            cur.setRight(self._deleteRec(key, cur._right))
        return updateNode
        
    def deleteNode(self, key, delNode):
        updateNode = None
        if (delNode._left == None) and (delNode._right == None):
            updateNode = None
        elif (delNode._left is not None) and (delNode._right == None):
            updateNode = delNode._left # one child == left
        elif delNode._left == None and delNode._right is not None:
            updateNode = delNode._right # one child - right
        else:
            updateNode = self.promoteSuccessor(delNode._right)
            if updateNode is not delNode._right:
                updateNode.setRight(delNode._right)
            updateNode.setLeft(delNode._left)

    def promoteSuccessor(self, cur):
        successor = cur
        if cur._left is not None:
           successor = self.promoteSuccessor(cur._left)
           if successor == cur._left:
               cur.setLeft(successor._right)

    def display(self):
        cont = True
        nodes = [self._root]
        while cont:
            if nodes:
                nodes = self._getChildren(nodes)
            else:
                cont = False

    def _getChildren(self, nodes):
        newNodes = []
        if nodes:
            try:
                print("")
                for node in nodes:
                    print(node._value, end = " ")
                    newNodes.append(node._left)
                    newNodes.append(node._right)
            except AttributeError:
                print("End of tree. :)\n")
        return newNodes

    def height(self): #Wrapper method
        return self._heightRec(self._root)

    def _heightRec(self, curNode):
        if curNode == None:
            htSoFar = -1
        else:
            leftHt = self._heightRec(curNode._left) #calc left height
            rightHt = self._heightRec(curNode._right) #calc right height

            #Get highest branch
            if leftHt > rightHt:
                htSoFar = leftHt + 1 
            else:
                htSoFar = rightHt + 1
        return htSoFar

    def min(self):
        return self._minRec(self._root)

    def _minRec(self, curNode):
        if curNode._left != None:
            minKey = self._minRec(curNode._left)
        else:
            minKey = curNode._key
        return minKey

    def max(self):
        return self._maxRec(self._root)

    def _maxRec(self, curNode):
        if curNode._right != None:
            maxKey = self._maxRec(curNode._right)
        else:
            maxKey = curNode._key
        return maxKey

    def balance(self):
        # Get total amount of keys in the tree
        keyTotal = (self.max() - self.min()) + 1

        # Get amount of node spaces in the tree
        nodeSpaces = 0
        for i in range(self.height()+1):
            nodeSpaces += (2 ** i)

        # Get ratio (ie how many spaces are filled)
        balance = keyTotal / nodeSpaces
        balance *= 100
        return balance

    # - ACTIVITY 3: Traversals

    def inOrder(self):
        return self._inOrderRec(self._root)

    def _inOrderRec(self, cur): #left-child -> cur -> right-child
        nodes = [] 
        #(if there are nodes in the tree)
        if cur is not None:
            nodes = nodes + self._inOrderRec(cur._left) #left
            nodes.append(cur._key) #current
            nodes = nodes + self._inOrderRec(cur._right) #right
        return nodes

    def preOrder(self):
        return self._preOrderRec(self._root)

    def _preOrderRec(self, cur): #cur -> left-child -> right-child
        nodes = [] 
        #(if there are nodes in the tree)
        if cur:
            nodes.append(cur._key) #current
            nodes = nodes + self._inOrderRec(cur._left) #left
            nodes = nodes + self._inOrderRec(cur._right) #right
        return nodes
    
    def postOrder(self): #left-child -> right-child -> cur
        return self._postOrderRec(self._root)

    def _postOrderRec(self, cur):
        nodes = []
        if cur:
            nodes = nodes + self._inOrderRec(cur._left)
            nodes = nodes + self._inOrderRec(cur._right)
            nodes.append(cur._key)
        return nodes



