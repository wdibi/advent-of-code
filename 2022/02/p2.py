import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

pairs = {'A': 'X', 'B': 'Y', 'C': 'Z'}
to_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
to_lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
bonus = {'X': 1, 'Y': 2, 'Z': 3}
outcome_bonus = {0: 3, -1: 0, 1: 6}
outcome = {'Z': 1, 'Y': 0, 'X': -1}


def score(x, y):
    o = outcome[y]
    tp = None
    if (o == 0):
        tp = pairs[x]
    if (o == 1):
        tp = to_win[x]
    if (o == -1):
        tp = to_lose[x]
    return bonus[tp] + outcome_bonus[o]


total_score = 0

for n in lines:
    [x, y] = n.split(' ')
    total_score += score(x, y)

print(total_score)
