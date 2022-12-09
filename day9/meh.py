import numpy as np

# Advent of Code 2022 Day 9

class knot:
    def __init__(self, name,parent):
        self.name = name
        self.parent = parent
        self.pos = [0, 0]
        self.child = None
        if parent:
            parent.child = self

    def add_child(self,  rec):
        self.child = knot(rec,self)
        if rec > 1:
             return self.child.add_child(rec-1)
        else:
            return self.child
    
    def update_pos(self):
        if self.parent:
            if abs(self.parent.pos[0] - self.pos[0]) <= 1 and abs(self.parent.pos[1] - self.pos[1]) <= 1:
                return
            if self.parent.pos[0] == self.pos[0] or self.parent.pos[1] == self.pos[1]:
                if self.parent.pos[0] > self.pos[0]:
                    self.pos[0] += 1
                elif self.parent.pos[0] < self.pos[0]:
                    self.pos[0] -= 1
                elif self.parent.pos[1] > self.pos[1]:
                    self.pos[1] += 1
                elif self.parent.pos[1] < self.pos[1]:
                    self.pos[1] -= 1
            else:
                if self.parent.pos[0] > self.pos[0]:
                    self.pos[0] += 1
                elif self.parent.pos[0] < self.pos[0]:
                    self.pos[0] -= 1
                if self.parent.pos[1] > self.pos[1]:
                    self.pos[1] += 1
                elif self.parent.pos[1] < self.pos[1]:
                    self.pos[1] -= 1
        if self.child:
            self.child.update_pos()


head = knot("head",None)
tail = head.add_child(9)
passed_by = [[0, 0]]

def moveHead(direction):
    if direction == 'U':
        head.pos[1] += 1
    elif direction == 'D':
        head.pos[1] -= 1
    elif direction == 'L':
        head.pos[0] -= 1
    elif direction == 'R':
        head.pos[0] += 1
    head.update_pos()

with open("day9/input") as f:
    data = f.read().splitlines()
    for move in data:
        direction = move[0]
        distance = int(move[2:])
        for i in range(distance):
            moveHead(direction)
            head.update_pos()
            if tail.pos not in passed_by:
                passed_by.append(tail.pos.copy())
    print(len(passed_by))
