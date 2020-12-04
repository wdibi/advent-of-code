import re
with open("input.txt") as file:
    passports = [line.replace('\n', ' ') for line in file.read().split('\n\n')]

required = [('byr', lambda x: int(x) in range(1920, 2003)),
            ('iyr', lambda x: int(x) in range(2010, 2021)),
            ('eyr', lambda x: int(x) in range(2020, 2031)),
            ('hgt', lambda x: x[-2:] ==
             'cm' and int(x[:-2]) in range(150, 194) or x[-2:] == 'in' and int(x[:-2]) in range(59, 77)),
            ('hcl', lambda x: re.match(r"^#[0-9a-f]{6}$", x)),
            ('ecl', lambda x: x in {'amb', 'blu',
                                    'brn', 'gry', 'grn', 'hzl', 'oth'}),
            ('pid', lambda x: re.match(r"^[0-9]{9}$", x))]
valid = 0
for p in passports:
    fields = {x.split(':')[0]: x.split(':')[1] for x in p.split(' ')}
    try:
        if all([rule[1](fields[rule[0]]) for rule in required]):
            valid += 1
    except:
        pass
print(valid)
