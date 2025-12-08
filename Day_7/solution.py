from collections import deque

def read_file(filename):
    file1 = open(filename, 'r')
    return file1.read().splitlines()

def part_1(lines, visited = set()): #bfs type question
    R, C = len(lines), len(lines[0])
    #finding S
    for i in range(C):
        if (lines[0][i] == 'S'):
            starting_column = i
            break
    
    queue = deque()
    queue.append((0, starting_column)) # row, column
    splits = 0
    visited = set()
    while queue:
        r,c = queue.popleft()

        if (r,c) in visited:
            continue
        visited.add((r,c))

        while True:
            r += 1
            if r >= R:
                break
            if lines[r][c] == '.':
                continue
            
            if lines[r][c] == '^':
                if (r, c) not in visited:
                    visited.add((r, c))
                    splits += 1

                    # left beam
                    if c - 1 >= 0:
                        queue.append((r, c - 1))

                    # right beam
                    if c + 1 < C:
                        queue.append((r, c + 1))
                break
                
            else:
                break
    return splits

def part_2(lines):
    R, C = len(lines), len(lines[0])
    #finding S
    curr = [0] * C
    start_col = lines[0].index('S')
    curr[start_col] = 1

    result = 1 #found S

    for i in range(1, R):
        next_curr = [0] * C

        for c in range(C):
            if lines[i][c] == '^':
                result += curr[c]

                if c-1 >= 0:
                    next_curr[c-1] += curr[c]

                if c+1 < C: 
                    next_curr[c+1] += curr[c]
            else:
                next_curr[c] += curr[c]

        curr = next_curr


    return result
    


def main():
    file1 = 'input.txt'
    lines = read_file(file1)
    result_1 = part_1(lines)
    print(result_1)
    result_2 = part_2(lines)
    print(result_2)

if __name__ == '__main__':
    main()
