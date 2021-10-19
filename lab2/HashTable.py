class HashTable:

    def __init__(self, size):
        self.hash_table = [[] for _ in range(size)]
        self.__size = size

    def hash(self, key):
        newKey = 0
        for char in str(key):
            newKey += ord(char)
        return newKey % len(self.hash_table)

    def add(self, key):
        hash_key = self.hash(key)
        i = 0
        for i in range(len(self.hash_table[hash_key])):
            if self.hash_table[hash_key] == key:
                return (hash_key, i)
        self.hash_table[hash_key].append(key)
        return (hash_key, i + 1)

    def getPos(self, key):
        pos = self.hash(key)
        i = 0
        for itm in self.hash_table[pos]:
            if itm == key:
                break
            else:
                i = i + 1
        return (pos, i)

    def getSize(self):
        return self.__size

