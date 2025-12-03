def read_file(filename):
    file1 = open(filename, 'r')
    return file1.read().splitlines()

def finding_max(line, id):
    n = len(line)
    max_val = -1
    idx = 0
    for i in range(id,n):
        if int(line[i]) > max_val:
            max_val = int(line[i])
            idx = i
    
    line = line[:idx] + '0' + line[idx+1:]
    return max_val, line, idx

def part_1(lines):
    result = 0
    for line in lines:
        max1, line, idx1 = finding_max(line, 0)
        if (idx1 == len(line)-1):
            max2, line, idx2 = finding_max(line, 0)
        else: 
            max2, line, idx2 = finding_max(line, idx1)

        if (idx1 > idx2):
            st = str(max2) + str(max1)
        else:
            st = str(max1)+str(max2)

        print(st)
        result += int(st)
    return result

def largest_12_digits(line):
    remove = len(line) - 12
    stack = []

    for digit in line:
        while remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            remove-=1
        stack.append(digit)



    return "".join(stack[:12])

def part_2(lines):
    result = 0
    for line in lines:
        val = int(largest_12_digits(line))
        result += val
        print(val)
    return result
    



def main():
    file1 = 'input.txt'
    lines = read_file(file1)
    result_1 = part_1(lines)
    print(result_1)
    result_2 = part_2(lines)
    print(result_2)

if __name__ == "__main__":
    main()


    


    
