from HashTable import HashTable

class SymbolTable:
    def __init__(self, size):
        self.__hashTable = HashTable(size)

    def add(self, key):
        return self.__hashTable.add(key)

    def getPos(self, key):
        return self.__hashTable.getPos(key)

    def getSize(self):
        return self.__hashTable.getSize()