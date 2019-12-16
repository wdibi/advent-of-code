class Intcode:
    def __init__(self, memory, changes):
        self.intList = self.setup(memory, changes)
        self.index = 0
        
    @staticmethod
    def setup(memory, changes):
        intList = memory[:]
        for pos, val in changes.items():
            intList[pos] = val
        return intList

    def positions(self):
        return self.intList[self.index + 1], self.intList[self.index + 2], self.intList[self.index + 3]

    def opcode_add(self):
        p = self.positions()
        self.intList[p[2]] = self.intList[p[0]] + self.intList[p[1]]
        self.index += 4

    def opcode_multiple(self):
        p = self.positions()
        self.intList[p[2]] = self.intList[p[0]] * self.intList[p[1]]
        self.index += 4
    
    def run(self):
        while self.current != 99:
            if self.current == 1:
                self.opcode_add()
            elif self.current == 2:
                self.opcode_multiple()
        return self.intList

    @property
    def current(self):
        return self.intList[self.index]

def main():
    memory = [int(i) for i in open("input.in").read().split(',')]
    for noun, verb in ((a, b) for a in range(100) for b in range(100)):
        if Intcode(memory, {1: noun, 2: verb}).run()[0] == 19690720:
            print(100 * noun + verb)
            break


if __name__ == "__main__":
    main()
