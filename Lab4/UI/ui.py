from model.FiniteAutomata import FiniteAutomata


class UI:
    def __init__(self):
        self.finiteAutomata = FiniteAutomata()

    def run(self):
        commands = {'0': self.read_file, '1': self.set_of_states, '2': self.alphabet, '3': self.transitions,
                    '4': self.final_states, '5': self.init_states, '6': self.checkAcc, '7': self.printFA}

        print()
        print("0 - read file\n")
        print("1 - set of states\n")
        print("2 - the alphabet\n")
        print("3 - all the transitions\n")
        print("4 - the set of final states\n")
        print("5 - get ini states\n")
        print("6 - check accepted sequence\n")
        print("7 - print FA")

        exit = False

        while not exit:
            print(" -> ")
            command = input()
            if command in commands.keys():
                commands[command]()
            elif command == "exit":
                exit = True
            else:
                continue

    def checkAcc(self):
        seq = input()
        print(self.finiteAutomata.checkSequence(seq))

    def printFA(self):
        print(self.finiteAutomata)

    def read_file(self):
        self.finiteAutomata.read_from_file()

    def set_of_states(self):
        print(self.finiteAutomata.get_states())

    def alphabet(self):
        print(self.finiteAutomata.get_alphabet())

    def transitions(self):
        print(self.finiteAutomata.get_transitions())

    def final_states(self):
        print(self.finiteAutomata.get_final_states())

    def init_states(self):
        print(self.finiteAutomata.get_init_states())
