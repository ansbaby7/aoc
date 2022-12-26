f = open("../input.txt")
data = f.read().strip()
lines = data.split("\n")

def calc_dir_size(dir, dir_map):
    size = 0
    for x, y in dir_map[dir]:
        if x == "dir":
            size += calc_dir_size(y, dir_map)
        else:
            size += int(x)
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

root_size = calc_dir_size("root", dir_map)
free_space = 70000000 - root_size
needed = 30000000
to_free = needed - free_space

min = root_size
for dir in dir_map:
    k = calc_dir_size(dir, dir_map)
    if k >= to_free and k < min:
        min = k

print(min)


