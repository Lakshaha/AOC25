from collections import defaultdict
from functools import lru_cache

def read_file(filename):
    file1 = open(filename, 'r')
    return file1.read().splitlines()

graph = defaultdict(list)

@lru_cache(None)
def dfs_2(node, vis_fft, vis_dac):
    if (node == "fft"): vis_fft = True
    if (node == "dac"): vis_dac = True
    if (node == "out"): 
        if (vis_dac == True and vis_fft == True):
            return 1
        else:
            return 0
    
    total = 0
    for nxt in graph[node] :
        total += dfs_2(nxt, vis_fft, vis_dac)
    
    
    return total


def part_2(lines):
     #makes empty list for keys in dictionary
    # for line in lines:
    #     node,neighbor = line.split(":")
    #     node = node.strip()
    #     neighbor = neighbor.strip().split()
    #     graph[node].extend(neighbor) 
    # #adjaceny list ready
    vis_fft = False
    vis_dac = False
    result = dfs_2("svr", vis_fft, vis_dac)
    return result

def dfs_1(node):
    if (node == "out"): 
            return 1
    total = 0
    for nxt in graph[node] :
        total += dfs_1(nxt)
    
    
    return total


def part_1(lines):
    for line in lines:
        node,neighbor = line.split(":")
        node = node.strip()
        neighbor = neighbor.strip().split()
        graph[node].extend(neighbor) 
    result = dfs_1("you")
    return result

def main():
    filename = 'input.txt'
    lines = read_file(filename)
    result_1 = part_1(lines)
    print(result_1)
    result_2 = part_2(lines)
    print(result_2)

if __name__ == "__main__":
    main()

