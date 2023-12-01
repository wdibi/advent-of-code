filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

sum = 0
for n in lines:
    ss = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for w in ss:
        for ww in ss:
            if w[-1] == ww[0]:
                n = n.replace(w[:-1] + ww, w + ww)
    for i, w in enumerate(ss):
        n = n.replace(w, str(i+1))
    # p1
    digits = [c for c in n if c.isdigit()]
    x = digits[0], digits[-1]
    sum += int(x[0] + x[1])
print(sum)
