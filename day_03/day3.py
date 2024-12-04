# let's try regular expressions
import re
mull = r'mul\((\d{1,3}),(\d{1,3})\)' # regex to capture any mul(a,b), with a and b being the capture groups

if __name__ == "__main__":
    result = 0
    with open("input.txt", "r") as input:
        for line in input.readlines():
            mul_inputs = re.findall(mull, line)
            # each valid function calls are put into tuples ('a', 'b')
            for (a, b) in mul_inputs:
                result += (int)(a) * (int)(b)
                
    print(result)