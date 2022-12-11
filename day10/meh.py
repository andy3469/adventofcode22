#Advent of Code 2022 Day 10

cycle = 1
reg_x = 1
sig_str = []
image = []
img_line = ['.' for i in range(40)]

def noop_fct():
    global cycle
    cycle += 1


def add_fct(x):
    global cycle
    global reg_x
    global img_line
    cycle += 1
    if cycle < 221:
        if cycle % 40 == 20 or cycle == 20:
            sig_str.append(reg_x * cycle)
    if (cycle-1) % 40 == reg_x or (cycle-1) % 40 == reg_x + 1 or (cycle-1) % 40 == reg_x - 1:
        img_line[(cycle-1) % 40] = '#'
    if cycle % 40 == 0:
        image.append(img_line.copy())
        img_line = ['.' for i in range(40)]
    cycle += 1
    reg_x += x


with open('day10/input') as f:
    
    for line in f.read().splitlines():
        print(cycle, reg_x)
        if (cycle-1) % 40 == reg_x or (cycle-1) % 40 == reg_x + 1 or (cycle-1) % 40 == reg_x - 1:
            img_line[(cycle-1) % 40] = '#'
        if cycle % 40 == 0:
            image.append(img_line.copy())
            img_line = ['.' for i in range(40)]

        if line.startswith('noop'):
            noop_fct()
        elif line.startswith('addx'):
            add_fct(int(line.split(' ')[1]))
        if cycle < 221:
            if cycle % 40 == 20 or cycle == 20:
                sig_str.append(reg_x * cycle)
        
        
    print('part-1')
    print(sig_str)
    print(sum(sig_str))

    print('part-2')
    for line in image:
        print(''.join(line))