import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]


total = 0


for l in lines:
    l_len = len(l)
    p1 = [*l[0:l_len//2]]
    p2 = [*l[l_len//2:]]
    match = {c for c in p1 if c in p2}
    for m in match:
        total += string.ascii_letters.index(m) + 1

print(total)
