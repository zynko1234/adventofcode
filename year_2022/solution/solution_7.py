# Allows classes to be self-referential in type hints. This must occur at the
# beginning of the file.
from __future__ import annotations

import copy

def solve(in_list):
    ansA = None
    ansB = None

    data = normalize_input(in_list)

    ansA = partA(data)
    ansB = partB(data)
    return ansA, ansB

def partA(data):
    ret = 0
    modified_data = copy.deepcopy(data)
    root_name = modified_data[0][1]

    # Throw away the first instruction. The tree starts in the root directory.
    modified_data = modified_data[1:]

    # Generate the tree.
    root = FileTree(root_name)
    root.construct_fs(modified_data)
    ret = root.total_size_less_than(100000)

    return ret

def partB(data):
    ret = 0
    modified_data = copy.deepcopy(data)
    SYSTEM_SIZE = 70000000
    UPDATE_SIZE = 30000000

    # Throw away the first cd instruction. The file tree will start in the root directory.
    root_name = modified_data[0][1]
    modified_data = modified_data[1:]

    root = FileTree(root_name)
    root.construct_fs(modified_data)

    needed_space = UPDATE_SIZE - (SYSTEM_SIZE - root.size)
    ret = root.get_dir_closest_to_target(needed_space, SYSTEM_SIZE)

    return ret

def normalize_input(input):
    ret = []

    for line in input:
        tmp = line.split(' ')

        # Switch out the commands and superfluous glyphs with code numbers and
        # just the parameters to avoid string comparisons down the line.
        if tmp[0] == '$':
            if tmp[1] == 'cd':
                # cd command code 0
                tmp = tmp[2:]
                tmp.insert(0, 0)
            else:
                # ls command code 1
                tmp = tmp[2:]
                tmp.insert(0, 1)
        elif tmp[0] == 'dir':
            # New directory code 2
            tmp = tmp[1:]
            tmp.insert(0, 2)
        else:
            # New file code 3
            tmp[0] = int(tmp[0])
            tmp.insert(0, 3)
        ret.append(tmp)

    return ret

class FileTree(object):
    def __init__(self, name:str=''):
        self.name = name
        self.parent = None
        self.files = []
        self.dirs = []
        self.size = 0

    def add_file(self, size: int, name: str):
        self.files.append((size, name))

        # Cascade the new size up the line of parent trees, as they are
        # indirectly increasing in size from the file additon on this level.
        current_tree = self

        while current_tree is not None:
            current_tree.size += size
            current_tree = current_tree.parent

    def add_dir(self, name: str):
        tmp = FileTree(name)
        tmp.parent = self
        self.dirs.append(tmp)

    def set_parent(self, parent: FileTree):
        self.parent = parent

    def construct_fs(self, terminal_output: list):
        current_tree = self

        for instruction in terminal_output:
            code = instruction[0]
            # cd
            if code == 0:
                if instruction[1] == '..':
                    current_tree = current_tree.parent
                else:
                    current_tree = current_tree.get_dir(instruction[1])
            # ls
            elif code == 1:
                continue
            # new dir
            elif code == 2:
                current_tree.add_dir(instruction[1])
            # new file
            else:
                current_tree.add_file(instruction[1], instruction[2])

    def get_dir(self, name):
        for tree in self.dirs:
            if tree.name == name:
                return tree

    def total_size_less_than(self, size_limit:int=0):
        ret = 0

        if self.size <= size_limit:
            ret += self.size

        for tree in self.dirs:
            ret += tree.total_size_less_than(size_limit)

        return ret

    def get_dir_closest_to_target(self, target: int, system_size: int):
        candidate = int()

        if self.size < target:
            candidate = system_size
        else:
            candidate = self.size

        if len(self.dirs) != 0:
            for tree in self.dirs:
                # Recurse into this function to find the best candidate in
                # child directories.
                child_size = tree.get_dir_closest_to_target(target, system_size)

                # Replace the candidate if a child directory is closer to the
                # target size.
                if (child_size - target) < (candidate - target):
                    candidate = child_size

        return candidate









