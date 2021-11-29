import numpy as np

class Error(Exception):
    pass

class KeyNotFoundError(Error):
    pass

class TableFullError(Error):
    pass

class DSAHashEntry():
    def __init__(self, in_key="", in_value=None): # default vals
        self.key = in_key
        self.value = in_value
        self.state = 1 # 0 = never used, 1 = used, -1 = formerly used

    def __repr__(self):
        return (self.key + " -> " + str(self.value))

class DSAHashTable():
    # CONSTRUCTOR
    def __init__(self, table_size):
        self.count = 0 
        self.actual_size = self.findNextPrime(table_size)      # Set table size
        self.hash_array = np.empty(self.actual_size, dtype=object)

    def findNextPrime(self, startVal):
        if (startVal % 2 == 0):
            primeVal = startVal + 1
        else:
            primeVal = startVal
        primeVal = primeVal - 2

        isPrime = False
        #### DO WHILE (1)
        primeVal= primeVal + 2

        i = 3
        isPrime = True
        rootVal = primeVal**(1/2)
        if (primeVal % i == 0):
            isPrime = False
        else:
            i = i + 2
        while (i <= rootVal) and isPrime:
            if (primeVal % i == 0):
                isPrime = False
            else:
                i = i + 2
        while not isPrime:
            primeVal= primeVal + 2

            i = 3
            isPrime = True
            rootVal = primeVal**(1/2)
            ### DO WHILE(2)
            if (primeVal % i == 0):
                isPrime = False
            else:
                i = i + 2
            while (i <= rootVal) and isPrime:
                if (primeVal % i == 0):
                    isPrime = False
                else:
                    i = i + 2
            ### END DO WHILE(2)
        ### END DO WHILE (1)
        return primeVal

    def hash(self, key):
        # ✓ Fits tables
        # ✓ Relatively fast to compute
        # ✓ Repeatable
        # ✓ Distributes keys evenly (most of the time)
        hashIndex = 0

        for i in key:
            hashIndex = (33 * hashIndex) + ord(i)

        hashVal = hashIndex % len(self.hash_array)
        return hashVal

    def _doublehash(self, index):
        max_step = int(self.findNextPrime(self.actual_size/2)) # define max step (prime num that's <<< table size)
        hash_step = int(max_step - (index % max_step))
        return hash_step

    def put(self, in_key, in_value):
        #self.checkThreshold()
        if self.count < self.actual_size:
            # -- Set entry and index
            entry = DSAHashEntry(in_key, in_value)
            index = self.hash(in_key)

            # -- Place into hash array
            if self.hash_array[index] is None: # empty slot, insert normally
                self.hash_array[index] = entry
            else: # duplicate found, perform double hash
                self.hash_array[index].state = -1 
                index = self._doublehash(index)
                self.hash_array[index] = entry

            self.count += 1
        else:
            raise TableFullError
      
    def hasKey(self, key):
        try:
            if self.hash_array[self._find(key)] != None: # if exists
                hasKey = True
        except AttributeError:
            hasKey = False
        return hasKey

    def get(self, key):
        entry = None
        if self.hasKey(key):
            entry = self.hash_array[self._find(key)]
        else:
            raise KeyNotFoundError
        return entry

    def remove(self, key):
        if self.hasKey(key):
            self.hash_array[self._find(key)] = None # remove from hash_array
            self.count -= 1
        else:
            raise KeyNotFoundError

        self.checkThreshold()

    def display(self):
        print("====================================")
        entries = (entry for entry in self.hash_array if entry != None)
        for entry in entries:
            print(str(self._find(entry.key)) + " | " + str(entry))
        print("\nCapacity: " + str(self.actual_size))
        print("Size: " + str(self.count))
        print("====================================")

    # Returns index (use get to return entry)
    def _find(self, key):
        idx = self.hash(key)
        entry = self.hash_array[idx]
        if entry.state == -1: # Double hash has occured
            idx = self._doublehash(idx)
        return idx

# -- ACTIVITY 2 -- #
    def checkThreshold(self):
        # LESS THAN
        if self._getLoadFactor() < 0.3:
            self._resize(int(self.actual_size / 2)) # half the size to next prime
        # GREATER THAN
        elif self._getLoadFactor() > 0.7:
            self._resize(int(self.actual_size * 2)) # double it
        
    def _resize(self, size):
        # Get all non null entry's keys
        entries = (entry for entry in self.hash_array if entry != None)
        # Redeclare hash array and count
        self.hash_array = np.empty(size, dtype=object)
        self.count = 0

        # Fill in hash array
        for entry in entries:
            self.put(entry.key, entry.value)

    def _getLoadFactor(self):
        load_factor = self.count / self.actual_size # space used divided by capacity
        return load_factor

# -- ACTIVITY 3 -- #
    def export(self, fileName):
        with open(fileName, 'w') as f:
            f.write("Index, Key, Value\n")
            for entry in self.hash_array:
                if entry is not None:
                    f.write(str(self._find(entry.key)) + ", " + str(entry.key) + ", " + str(entry.value) + "\n") #line format