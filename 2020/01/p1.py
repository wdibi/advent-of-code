with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

seen = set()
for n in lines:
    n = int(n)
    x = 2020 - n 
    if x in seen:
        print(x * n)
        break
    seen.add(n)