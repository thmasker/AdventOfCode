from typing import List


class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []

    def get_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.size

        for directory in self.directories:
            size += directory.get_size()

        return size


class File:
    def __init__(self, name: str, size: int, parent: Directory):
        self.name = name
        self.size = size
        self.parent = parent


def find_directory(name: str, current_dir: Directory) -> Directory:
    for directory in current_dir.directories:
        if directory.name == name:
            return directory


def initialize_filesystem() -> Directory:
    with open('input.txt', 'r') as file:
        root = Directory('/', None)
        current_dir = root
        for line in file.readlines()[2:]:
            line = line.rstrip()
            if line[:4] == '$ cd':
                if line[5:] == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = find_directory(line[5:], current_dir)
            elif line[:3] == 'dir':
                current_dir.directories.append(Directory(line.split(' ')[1], current_dir))
            elif line[:4] != '$ ls':
                size, name = line.split(' ')
                current_dir.files.append(File(name, int(size), current_dir))
    return root


def find_sizes_smaller_than(root: Directory, limit_size: int) -> List[int]:
    sizes = []
    current_dir = root

    size = current_dir.get_size()
    if size <= limit_size:
        sizes.append(size)

    for directory in current_dir.directories:
        sizes.extend(find_sizes_smaller_than(directory, limit_size))

    return sizes


def find_sizes_to_delete(root: Directory, root_size: int, required_size: int) -> List[int]:
    sizes = []
    current_dir = root

    if root_size >= required_size:
        sizes.append(root_size)

    for directory in current_dir.directories:
        sizes.extend(find_sizes_to_delete(directory, directory.get_size(), required_size))

    return sizes


def part1() -> int:
    return sum(find_sizes_smaller_than(initialize_filesystem(), 100000))


def part2() -> int:
    root = initialize_filesystem()
    root_size = root.get_size()
    return min(find_sizes_to_delete(root, root_size, 30000000 - 70000000 + root_size))


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
