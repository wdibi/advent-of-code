with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

seen = set()
for n in lines:
    n = int(n)
    for s in seen:
      x = 2020 - n - s
      if x in seen:
        print(n * x * s)
        break
    seen.add(n)