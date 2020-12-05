with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

seats = []
for line in lines:
    r_range = [*range(0, 128)]
    c_range = [*range(0, 8)]
    for c in line:
        if c == 'F':
            r_range = r_range[:len(r_range)//2]
        elif c == 'B':
            r_range = r_range[len(r_range)//2:]
        elif c == 'R':
            c_range = c_range[len(c_range)//2:]
        elif c == 'L':
            c_range = c_range[:len(c_range)//2]
    seats.append(r_range[0]*8+c_range[0])
print(max(seats))