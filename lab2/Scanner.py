from ReadFile import read_tokens, check_ident, check_const
from SymbolTable import SymbolTable

class Scanner:

    def __init__(self, file="token.in"):
        self.reserved_words, self.separators, self.operators = read_tokens(file)
        self.tokens = self.reserved_words + self.separators + self.operators
        self.idTable = SymbolTable(10)
        self.constTable = SymbolTable(10)
        self.pif = []

    def run(self):
        file = open("p1.smt")
        file.readline()
        line = file.readline()

        count = 1
        while line:
            count += 1
            line = line.strip()
            elements = line.split(" ")
            for element in elements:
                if element != "":
                    if element in self.tokens:
                        self.pif.append([element, None])
                    else:
                        if check_ident(element):
                            pos = self.idTable.add(element)
                            self.pif.append(['ID', pos])
                        elif check_const(element):
                            pos = self.constTable.add(element)
                            self.pif.append(['CONST', pos])
                        else:
                            print("Error: line " + str(count) + " token " + element)
                            return
            line = file.readline()

        with open("pif.out", 'w') as file:
            for elem in self.get_pif():
                file.write(str(elem) + '\n')

        with open("st.out", 'w') as file:
            file.write("ID: \n\n")
            file.write(str(self.idTable))
            file.write("\n\n")
            file.write("CONST: \n\n")
            file.write(str(self.constTable))

    def get_tokens(self):
        return self.tokens

    def get_identifiers(self):
        return self.idTable

    def get_consts(self):
        return self.constTable

    def get_pif(self):
        return self.pif