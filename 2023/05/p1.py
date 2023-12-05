filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

seeds = lines[0].split()[1:]

grouped = []
cur_group = []
for n in lines[2:]:
    if (len(n) and n[0].isdigit()):
        cur_group.append([int(i) for i in n.split()])
    elif len(cur_group):
        grouped.append(cur_group)
        cur_group = []
grouped.append(cur_group)

min_loc = None
for s in seeds:
    nv = int(s)
    for gg in grouped:
        for g in gg:
            diff = nv - g[1]
            if nv >= g[1] and nv < (g[1] + g[2]):
                nv = g[0] + diff
                break

    if not min_loc or nv < min_loc:
        min_loc = nv
print(min_loc)
