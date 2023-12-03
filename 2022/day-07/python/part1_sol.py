f = open("../input.txt")
data = f.read().strip()
lines = data.split("\n")

dir_sizes = {}

def calc_dir_size(dir, dir_map):
    size = 0
    for x, y in dir_map[dir]:
        if x == "dir":
            if dir_sizes.get(y) is None:
                dir_sizes[y] = calc_dir_size(y, dir_map)
            size += dir_sizes[y]
        else:
            size += int(x)
    dir_sizes[dir] = size
    return size 

dir_map = {}
i = 0
path = ""

while i < len(lines):
    v = lines[i].split(" ")
    if v[1] == "cd":
        if v[2] == "/":
            path = "root"
        elif v[2] == "..":
            path = path.rsplit("/", 1)[0]
        else:
            path = path + "/" + v[2]
        i += 1
    elif v[1] == "ls":
        if dir_map.get(path) is None:
            dir_map[path] = []
            i += 1
            while i < len(lines) and lines[i].split(" ")[0] != "$":
                x, y = lines[i].split(" ")
                if x == "dir":
                    y = path + "/" + y
                dir_map[path].append((x, y))
                i += 1
    
# print(dir_map)

total = sum([k for k in [calc_dir_size(dir, dir_map) for dir in dir_map] if k <= 100000])
print(total)
