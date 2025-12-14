from collections import defaultdict
from functools import lru_cache

def read_file(filename):
    file1 = open(filename, 'r')
    return file1.read().splitlines()

graph = defaultdict(list)

@lru_cache(None)
def dfs(node, vis_fft, vis_dac):
    if (node == "fft"): vis_fft = True
    if (node == "dac"): vis_dac = True
    if (node == "out"): 
        if (vis_dac == True and vis_fft == True):
            return 1
        else:
            return 0
    
    total = 0
    for nxt in graph[node] :
        total += dfs(nxt, vis_fft, vis_dac)
    
    
    return total


def part_1(lines):
     #makes empty list for keys in dictionary
    for line in lines:
        node,neighbor = line.split(":")
        node = node.strip()
        neighbor = neighbor.strip().split()
        graph[node].extend(neighbor) 
    #adjaceny list ready
    vis_fft = False
    vis_dac = False
    result = dfs("svr", vis_fft, vis_dac)
    return result

def main():
    filename = 'input.txt'
    lines = read_file(filename)
    result_1 = part_1(lines)
    print(result_1)

if __name__ == "__main__":
    main()

