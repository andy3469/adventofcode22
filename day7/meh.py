
#Advent of Code 2022 Day 7


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.parent = None

class Directory:
    def __init__(self, name, size=0):
        self.name = name
        self.parent = None
        self.size = size
        self.files = {}
    
    def add_file(self, file):
        file.parent = self
        self.files[file.name] = file
        self.size += file.size
        self.update_size(file.size)

    def update_size(self, size=0):
        # if the directory has a parent, update its size
        if self.parent:
            self.parent.size += size
            # recursively update the size of the parent directory
            self.parent.update_size(size)

    def get_sizes(self):
        sizes = []
        
        # add the size of the current directory to the list
        sizes.append(self.size)
        
        # recursively get the sizes of the subdirectories
        for file in self.files.values():
            if isinstance(file, Directory):
                sizes += file.get_sizes()
        
        return sizes


    def print(self, indent=""):
        # print the directory name
        print(indent + self.name + " (" + str(self.size) + ")")
        
        # print the files and subdirectories in this directory
        for file in self.files.values():
            # if the file is a directory, recursively print its contents
            if isinstance(file, Directory):
                file.print(indent + "    ")
            # otherwise, print the file name and size
            else:
                print(indent + "    " + file.name + " (" + str(file.size) + ")")


# initialize the root directory
root = Directory("/")

# initialize the current directory
current = root

# read the input and process each line
with open("day7/input") as f:
    input_lines = f.read().splitlines()
    for command in input_lines:
        # split the line into a command and its arguments

        
        # handle the 'cd' command
        if command.startswith("$ cd"):
            target_dir = command.split(" ")[-1]
            # if '..' is specified, move up one level
            if target_dir == "/":
                current = root
            elif target_dir == "..":
                current = current.parent
            # otherwise, move down one level
            else:
                current = current.files[target_dir]
        
        # handle the 'ls' command
        elif command.startswith("$ ls"):
            #do nothing
            pass
        else:
            # add the files and directories listed in the output
            a, b = command.split(" ")
            if a == "dir":
                # create a new directory
                dir = Directory(b)
                current.add_file(dir)
            else:
                # create a new file with the specified size
                size = int(a)
                file = File(b, size)
                current.add_file(file)
                

    # print the size of the root directory
    # root.print()

    print('part-1')
    sum = 0
    for size in root.get_sizes():
        if size < 100000:
            sum += size
    print(sum)
    
    print('part-2')
    print("%d space free",70000000-root.size)
    space_needed = 30000000 - (70000000-root.size)

    dir_deletable = []
    for size in root.get_sizes():
        if size > space_needed:
            dir_deletable.append(size)
    print(min(sorted(dir_deletable)))
