with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

r, c = 0, 0

tree_count = 0
while r < len(lines):
    if lines[r][c] == '#':
        tree_count += 1
    if c + 3 >= len(lines[0]):
        c = c + 3 - len(lines[0])
    else:
        c += 3
    r += 1

print(tree_count)
