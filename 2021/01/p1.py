with open("input.txt") as file:
    lines = [int(line.rstrip()) for line in file]

increased = 0
for i, line in enumerate(lines[1:]):
    if (line > lines[i]):
        increased += 1
print(increased)
