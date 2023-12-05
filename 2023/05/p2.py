filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

seed_groups = [int(i) for i in lines[0].split()[1:]]
seed_ranges = seed_groups[1::2]
seed_start = seed_groups[0::2]

grouped = []
cur_group = []
for n in lines[2:]:
    if (len(n) and n[0].isdigit()):
        cur_group.append([int(i) for i in n.split()])
    elif len(cur_group):
        grouped.append(cur_group)
        cur_group = []
grouped.append(cur_group)


def in_seed(v):
    for i, ss in enumerate(seed_start):
        if v >= ss and v <= ss + seed_ranges[i]:
            return True
    return False


start = 0
while True:
    nv = start
    for gg in reversed(grouped):
        for g in gg:
            if nv >= g[0] and nv <= g[0] + g[2]:
                nv = nv - g[0] + g[1]
                break
    if in_seed(nv):
        print(start)
        break
    start += 1
