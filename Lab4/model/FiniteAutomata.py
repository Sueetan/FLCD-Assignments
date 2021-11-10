def validate(states, alphabet, transitions, init_states, final_states):
    if init_states not in states:
        return False
    for f_state in final_states:
        if f_state not in states:
            return False
    for key in transitions.keys():
        state = key[0]
        symbol = key[1]
        if state not in states:
            return False
        if symbol not in alphabet:
            return False
        for dest in transitions[key]:
            if dest not in states:
                return False
    return True


class FiniteAutomata:
    def __init__(self):
        self.states = []        # Q
        self.alphabet = []    # E
        self.transitions = {}  # S
        self.init_states = None  # q0
        self.final_states = []    # F

    def get_states(self):
        return self.states

    def get_init_states(self):
        return self.init_states

    def get_transitions(self):
        return self.transitions

    def get_alphabet(self):
        return self.alphabet

    def get_final_states(self):
        return self.final_states

    def read_from_file(self, file_path="dfa.in"):
        with open(file_path) as file:
            lines = file.readlines()
            lines = [line.replace('\n', "").strip() for line in lines]

            self.states = lines[0].split(" ")
            self.alphabet = lines[1].split(" ")
            self.init_states = lines[2]
            self.final_states = lines[3].split(" ")

            for line in range(4, len(lines)):
                trans = lines[line].split(" ")
                source = trans[0]
                route = trans[1]
                dest = trans[2]

                if (source, route) in self.transitions.keys():
                    self.transitions[(source, route)].append(dest)
                else:
                    self.transitions[(source, route)] = [dest]

            if not validate(self.states, self.alphabet, self.transitions, self.init_states, self.final_states):
                print("invalid file")

    def DFA(self):
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return False
        return True

    def checkSequence(self, seq):
        if self.DFA():
            current = self.init_states
            for symbol in seq:
                if(current, symbol) in self.transitions.keys():
                    current = self.transitions[(current, symbol)][0]
                else:
                    return False
            return current in self.final_states
        return False

    def __str__(self):
        return "states = [ " + ', '.join(self.states) + " ]\n" \
                "alphabet = [ " + ', '.join(self.alphabet) + " ]\n" \
                "transitions = " + str(self.transitions) + " ]\n" \
                "init_states = [ " + self.init_states + " ]\n" \
                "final_states = [ " + ', '.join(self.final_states) + " ]"


