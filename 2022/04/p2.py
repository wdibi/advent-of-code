import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]


pairs = 0
for l in lines:
    [e1, e2] = l.split(',')
    e1 = e1.split('-')
    e2 = e2.split('-')
    r1 = range(int(e1[0]), int(e1[1]))
    r2 = range(int(e2[0]), int(e2[1]))

    i = range(max(r1.start, r2.start), min(r1.stop, r2.stop))
    if i.start <= i.stop:
        pairs += 1

print(pairs)
