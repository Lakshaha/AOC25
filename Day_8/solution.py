def read_file(filename):
    file1 = open(filename, 'r')
    return file1.read().splitlines()

def part_1(lines):
    coods = []
    for line in lines:
        if "," in line:
            x,y,z = map(int, line.split(","))
            coods.append((x,y,z))

    n = len(coods)

    #edge distances now
    edges = []
    for i in range(n):
        x,y,z = coods[i]
        for j in range(i+1, n):
            a,b,c = coods[j]
            dx = x-a
            dy = y-b
            dz = z-c
            dist = (dx*dx + dy*dy + dz*dz)
            edges.append((dist, i, j))
    
    edges.sort(key=lambda e:e[0])

    parents = []
    size = []
    for i in range(n):
        parents.append(i)
        size.append(1)

    def find_parent(x):
        if parents[x] == x: return x
        parents[x] = find_parent(parents[x])
        return parents[x]
    
    def union(a , b):
        parents[find_parent(a)] = find_parent(b)

    

    for dist, a, b, in edges[:1000]:
        union(a,b)
    
    sizes = [0] * len(coods)

    for i in range(len(sizes)):
        sizes[find_parent(i)] += 1

    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def part_2(lines):
    coods = []
    for line in lines:
        if "," in line:
            x,y,z = map(int, line.split(","))
            coods.append((x,y,z))

    n = len(coods)

    #edge distances now
    edges = []
    for i in range(n):
        x,y,z = coods[i]
        for j in range(i+1, n):
            a,b,c = coods[j]
            dx = x-a
            dy = y-b
            dz = z-c
            dist = (dx*dx + dy*dy + dz*dz)
            edges.append((dist, i, j))
    
    edges.sort(key=lambda e:e[0])
    p = len(coods)

    parents = []
    size = []
    for i in range(n):
        parents.append(i)
        size.append(1)

    def find_parent(x):
        if parents[x] == x: return x
        parents[x] = find_parent(parents[x])
        return parents[x]
    
    def union(a , b):
        parents[find_parent(a)] = find_parent(b)

    

    for dist, a, b, in edges:
        if find_parent(a) == find_parent(b): continue
        union(a,b)
        p -= 1
        if p == 1:
            return(coods[a][0] * coods[b][0])


def main():
    file1 = "input.txt"
    lines = read_file(file1)
    result_1 = part_1(lines)
    print(result_1)
    result_2 = part_2(lines)
    print(result_2)

if __name__ == "__main__":
    main()
