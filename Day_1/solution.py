def readlines(file_name): #reading the file to get the inputs
    file1 = open(file_name, 'r')
    lines = file1.read().strip().splitlines()
    return lines

def read_instruction(line):
    direction = line[0]
    val = int(line[1:])
    return direction, val

def perform_rotation(direction, val, pos, size):
    if (direction == 'L'):
        pos = pos - val
        pos = pos%size
    else:
        pos = pos + val
        pos = pos%size
    return pos
    
def part_1(lines):
    pos = 50
    counter = 0
    for line in lines:
        direction , val = read_instruction(line)
        pos = perform_rotation(direction, val, pos, 100)
        if (pos == 0): counter+=1
    
    return counter



def check_crossing(direction, newpos, oldpos, size, val):
    full_wrap = val // size
    partial_wrap = 0

    if (direction == 'L' and newpos > oldpos):
        partial_wrap = 1
    elif (direction == 'R' and newpos < oldpos):
        partial_wrap = 1

    return full_wrap + partial_wrap

def part_2(lines):
    pos = 50
    counter = 0
    
    for line in lines:
        direction, val = read_instruction(line)
        oldpos = pos
        newpos = perform_rotation(direction, val, pos, 100)
        counter += check_crossing(direction, newpos, oldpos, 100, val)
        pos = newpos
    return counter



def main():
    lines = readlines('input.txt')
    count_1 = part_1(lines)
    count_2 = part_2(lines)
    print(count_1)
    print(count_2)
   


if __name__ == "__main__":
    main()
