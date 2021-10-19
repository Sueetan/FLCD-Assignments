from SymbolTable import SymbolTable

size = 10

symbolTable = SymbolTable(size)

smt = 0
for i in range(size):
    smt = symbolTable.add(i)

for i in range(5):
    smt = symbolTable.add(i)
    print(smt)

for i in range(5):
    smt = symbolTable.add(i)
    print(smt)
