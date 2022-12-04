import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]


total = 0

grouped = [[lines[i], lines[i+1], lines[i+2]]
           for i in range(0, len(lines)-2, 3)]
for g in grouped:
    print(g)
    match = {c for c in g[0] if c in g[1] and c in g[2]}
    for m in match:
        total += string.ascii_letters.index(m) + 1

print(total)
