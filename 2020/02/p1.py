import re
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

valid = 0
for line in lines:
    policy, password = line.split(': ')
    p_occ, p_char = policy.split(' ')
    p_min, p_max = re.findall(r'\d+', p_occ)
    count = password.count(p_char)
    if count in range(int(p_min), int(p_max)+1):
        valid += 1
print(valid)
