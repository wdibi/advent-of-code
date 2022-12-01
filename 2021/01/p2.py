import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
args = parser.parse_args()

filename = "input_sample.txt" if args.s else "input.txt"

with open(filename) as file:
    lines = [int(line.rstrip()) for line in file]

line_sums = [line + lines[i+1] + lines[i+2]
             for i, line in enumerate(lines) if i < len(lines) - 2]

increased = 0
for i, line in enumerate(line_sums[1:]):
    if (line > line_sums[i]):
        increased += 1
print(increased)
