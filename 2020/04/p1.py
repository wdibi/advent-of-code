with open("input.txt") as file:
    passports = [line.replace('\n', ' ') for line in file.read().split('\n\n')]

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
for p in passports:
    keys = [x.split(':')[0] for x in p.split(' ')]
    if all(elem in keys for elem in required):
        valid += 1
print(valid)
