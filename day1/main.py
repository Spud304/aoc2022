elf_cals = []

with open('day1/input.txt', 'r') as f:
    text = f.read()
    x = 0
    for line in text.splitlines():
        if line.strip() == '':
            elf_cals.append(x)
            x = 0
            continue
        else:
            x += int(line)

print(f'Part 1: {max(elf_cals)}')

x = sorted(elf_cals)[-3:]
print(f'Part 2: {x[0] + x[1] + x[2]}')