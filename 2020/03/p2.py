with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

product = 1
for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    r, c = 0, 0
    tree_count = 0
    while r < len(lines):
        if lines[r][c] == '#':
            tree_count += 1
        if c + slope[0] >= len(lines[0]):
            c = c + slope[0] - len(lines[0])
        else:
            c += slope[0]
        r += slope[1]
    product *= tree_count
print(product)
