def read_file(filename):
    file1 = open(filename, 'r')
    return file1.read().splitlines()

def merged_arrr(arr):
    arr.sort(key = lambda x: x[0])
    merged_arr = []
    cur_start, cur_end = arr[0]
    for i in range(1,len(arr)):
        start = arr[i][0]
        end = arr[i][1]
        if (start <= cur_end):
            cur_end = max(cur_end, end)
        else: 
            merged_arr.append([cur_start, cur_end])
            cur_start = start
            cur_end = end
    merged_arr.append([cur_start,cur_end])
    return  merged_arr

        

def part_1(lines):
    arr = []
    i = 0
    for i in range (len(lines)):
        if lines[i] == "": break
        else:
            start, end = map(int, lines[i].split('-'))
            arr.append([start, end])

            
    #lines read
    counter = 0
    i += 1
    number = 0
    merged_arr = merged_arrr(arr)
    for j in lines[i:]:
        v = int(j)
        for k in range(len(merged_arr)):
            low = merged_arr[k][0]
            high = merged_arr[k][1]
            if (low <= v <= high):
                counter += 1
                break
    
    number = sum(end - start + 1 for start, end in merged_arr)
        
    return counter, number

def main():
    lines = read_file('input.txt')
    result_1, result_2 = part_1(lines)
    print(result_1)
    print(result_2)

if __name__ == '__main__':
    main()