from math import lcm
# Advent of Code 2022 Day 11


class monkey:
    def __init__(self, name, operation='', div=1, test=(0, 0)):
        self.name = name
        self.operation = operation.split(' ')
        self.items = []
        self.div = div
        self.test = test
        self.inspectCount = 0

    def add_item(self, item = 0):
        self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def inspect(self,mod):
        for i in range(len(self.items)):
            self.inspectCount += 1
            item = int(self.items.pop(0))
            if self.operation[4] == '*':
                if self.operation[5] == 'old':
                    item = item * item
                else:
                    item = item * int(self.operation[5])
            elif self.operation[4] == '+':
                if self.operation[5] == 'old':
                    item = item + item
                else:
                    item = item + int(self.operation[5])
            # item = item // 3
            if item % self.div == 0:
                monkeys[self.test[0]].add_item(item % mod)
            else:
                monkeys[self.test[1]].add_item(item % mod)
            




monkeys = []

with open('day11/input') as f:
    data = f.read().split('\n\n')

    for monkey_data in data:
        m = monkey(monkey_data.split('\n')[0].split(' ')[1], monkey_data.split('\n')[2].split(':')[1], int(monkey_data.split('\n')[
                   3].split('divisible by')[1]), (int(monkey_data.split('\n')[4].split('monkey ')[1]), int(monkey_data.split('\n')[5].split('monkey ')[1])))
        for item in monkey_data.split('\n')[1].split(':')[1].split(','):
            m.add_item(int(item))
        print(m.name, m.operation, m.items, m.div, m.test)
        monkeys.append(m)

    mod = lcm(*[monkey.div for monkey in monkeys])

    for r in range(10000):
        print(r)
        for m in monkeys:
            m.inspect(mod)
            
    inspectCount = []
    for m in monkeys:
        inspectCount.append(m.inspectCount)
    inspctCount = sorted(inspectCount)
    print(inspctCount)
    print(inspctCount[-1] * inspctCount[-2])
