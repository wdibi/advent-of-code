import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

pairs = {'A': 'X', 'B': 'Y', 'C': 'Z'}
to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
bonus = {'X': 1, 'Y': 2, 'Z': 3}
outcome_bonus = {0: 3, -1: 0, 1: 6}


def outcome(x, y):
    if (pairs[x] == y):
        return 0
    wins = to_win[x] == y
    return 1 if wins else -1


def score(x, y):
    o = outcome(x, y)
    b = bonus[y]
    print(b, outcome_bonus[o])
    return b + outcome_bonus[o]


total_score = 0

for n in lines:
    [x, y] = n.split(' ')
    total_score += score(x, y)

print(total_score)
