import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

group = 0
e = []
for n in lines:
    if n == '':
        group += 1
    else:
        if len(e)-1 < group:
            e.append(int(n))
        else:
            e[group] += int(n)
print(sum(sorted(e, reverse=True)[:3]))
