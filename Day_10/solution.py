import re, itertools
import z3



def read_file(filename):
    file1 = open(filename,'r')
    return file1.read().splitlines()

def part_1(lines):
    total = 0
    for line in lines:
        match = re.match(r"^\[([.#]+)\]\s+(.*?)\s+\{.*?\}$", line.strip())
        target, button = match.groups()
        #making a true false set of target and then finally getting the values that are on
        target = {index for index, light in enumerate(target) if light == "#"}
        #making buttons into set, and removing the brackets
        #button = [set(map(int, butt[1:-1].split(","))) for butt in button.split()]
        buttons_raw = re.findall(r"\((.*?)\)", button)
        button = [set(map(int, b.split(","))) for b in buttons_raw]
        for count in range(1, len(button) + 1):
            for attempt in itertools.combinations(button, r= count):
                lights = set() #empty set
                for butt in attempt:
                    lights ^= butt
                if lights == target:
                    total += count
                    break
            else:
                continue
            break
    
    return total

def part_2(lines):
    total = 0
    for line in lines:
        match = match = re.match(r"^\[([.#]+)\]\s+(.*?)\s+\{(.*?)\}$", line.strip())
        _, buttons, joltages = match.groups()
        buttons = [set(map(int, button.split(","))) for button in re.findall(r"\((.*?)\)", buttons)]
        joltages = list(map(int, joltages.split(",")))

        o = z3.Optimize()
        vars = [z3.Int(f"n{i}" ) for i in range(len(buttons))]
        for var in vars: o.add(var >= 0)
        for i, joltage in enumerate(joltages):
            equation = 0
            for b,  button in enumerate(buttons):
                if i in button:
                    equation += vars[b]
            o.add( equation == joltage)
        o.minimize(z3.Sum(vars))
        assert o.check() == z3.sat
        
        total += o.model().eval(z3.Sum(vars)).as_long()




        
    
    return total
        

def main():
    file1 = 'input.txt'
    lines = read_file(file1)
    result_1 = part_1(lines)
    print(result_1)
    result_2 = part_2(lines)
    print(result_2)
            

if __name__ == "__main__":
    main()