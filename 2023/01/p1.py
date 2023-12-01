filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

sum = 0
for n in lines:
    digits = [c for c in n if c.isdigit()]
    x = digits[0], digits[-1]
    sum += int(x[0] + x[1])
print(sum)
