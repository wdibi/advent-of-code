moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def path(commands):
    points = [(0, 0)]
    for step in commands:
        for i in range(int(step[1:])):
            points.append(tuple(map(sum, zip(points[-1], moves[step[0]]))))
    return points[1:]


with open("input.in") as f:
    lines = f.readlines()
    wire_1 = path(lines[0].rstrip('\n').split(','))
    wire_2 = path(lines[1].rstrip('\n').split(','))
    intersection = set(wire_1).intersection(wire_2)
    print(min([wire_1.index(p) + wire_2.index(p) + 2 for p in intersection]))

