import re
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

valid = 0
for line in lines:
    policy, password = line.split(': ')
    p_occ, p_char = policy.split(' ')
    p_min, p_max = re.findall(r'\d+', p_occ)
    if (password[int(p_min)-1] is p_char) ^ (password[int(p_max)-1] is p_char):
        valid += 1
print(valid)
