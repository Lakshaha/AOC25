def read_file(filename):
    file1 = open(filename,'r')
    return file1.read().split(",")

def read_range(line):
    start , end = map(int, line.split("-"))
    return start, end

def check_repeating(x):
    st = str(x)
    if (len(st) == 1 or len(st) % 2 != 0):
        return False
    mid = len(st) // 2
    return st[:mid] == st[mid:]

def checking_in_range(start, end):
    counter = 0
    for i in range(start, end+1):
        if (check_repeating(i)):
            # print(i)
            counter += i
        
    return counter

def check_repeating_part2(x):
    st = str(x)
    if (len(st) == 1): return False
    return st in (st + st)[1:-1]

def check_in_range_part2(start, end):
    counter = 0
    for i in range(start, end+1):
        if (check_repeating_part2(i)):
            counter += i
        
    return counter




def part_1(lines):
    result = 0
    for line in lines:
        start, end = read_range(line)
        result += checking_in_range(start, end)

    return result

def part_2(lines):
    result = 0
    for line in lines:
        start, end = read_range(line)
        result += check_in_range_part2(start, end)
    
    return result



def main():
    lines = read_file('input.txt')
    result_1 = part_1(lines)
    print(result_1)
    result_2 = part_2(lines)
    print(result_2)

if __name__ == "__main__":
    main()
