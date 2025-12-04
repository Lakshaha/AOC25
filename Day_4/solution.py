def read_file(filename):
    file1 = open(filename, 'r')
    grid = [list(line.strip()) for line in file1]
    return grid

def check(grid, r,c):
    if (grid[r][c] != '@'): return 0
    counter = 0
    dr = [1,1,0,-1,-1,-1,0,1]
    dc = [0,-1,-1,-1,0,1,1,1]
    for j in range(8):
        nr = r + dr[j]
        nc = c + dc[j]
        if (nr >= len(grid) or nr < 0 or nc >= len(grid[r]) or nc < 0): 
            continue
        elif (grid[nr][nc] == '@'): 
            counter += 1

    if (counter < 4):
        return 1
    return 0

def check_2(grid, r,c):
    if (grid[r][c] != '@'): return 0
    counter = 0
    dr = [1,1,0,-1,-1,-1,0,1]
    dc = [0,-1,-1,-1,0,1,1,1]
    for j in range(8):
        nr = r + dr[j]
        nc = c + dc[j]
        if (nr >= len(grid) or nr < 0 or nc >= len(grid[r]) or nc < 0): 
            continue
        elif (grid[nr][nc] == '@'): 
            counter += 1

    if (counter < 4):
        grid[r][c] = '.'
        return 1
    return 0



def Bfs_1(grid):
    result = 0

    for r in range (len(grid)):
        for c in range(len(grid[r])):
            if (check(grid, r ,c)):
                result += 1
        
    # for row in grid:
    #     print(row)
    return result

def Bfs_2(grid):
    result = 0
    flag = 1
    while(flag != 0):
        flag = 0
        for r in range (len(grid)):
            for c in range(len(grid[r])):
                if (check_2(grid, r ,c)):
                    result += 1
                    flag = 1
            
    # for row in grid:
    #     print(row)
    return result


def main():
    file1 = 'input.txt'
    grid = read_file(file1)
    result_1 = Bfs_1(grid)
    print(result_1)
    result_2 = Bfs_2(grid)
    print(result_2)

if __name__ == "__main__":
    main()