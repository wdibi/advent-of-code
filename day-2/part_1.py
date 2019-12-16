class Intcode:
    def __init__(self, data):
        self.intList = data
        self.index = 0

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
    data = [int(i) for i in open("input.in").read().split(',')]
    data[1] = 12
    data[2] = 2
    print(Intcode(data).run()[0])


if __name__ == "__main__":
    main()
