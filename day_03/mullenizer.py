# part 2 requires searching a few different patterns, so let's make a tokenizer
# reference in using is https://docs.python.org/3/library/re.html#writing-a-tokenizer

import re
mull = r'mul\((\d{1,3}),(\d{1,3})\)' # regex to capture any mul(a,b), with a and b being the capture groups
do = r'do\(\)'
dont = r'don\'t\(\)'

named_group = { ("mull", mull), 
                ("do",   do),
                ("dont", dont) }

# self contained logic to process mul inputs, since it's harder to extract the groups directly from the match
def mul(str):
    # findall gives us the two values in a list with a tuple
    [(a, b)] = re.findall(mull, string=str)
    return (int)(a) * (int)(b)    

if __name__ == "__main__":
    result = 0
    doing = True    # state variable to track do / dont
    regex = '|'.join('(?P<%s>%s)' % pair for pair in named_group)
    # this join syntax makes named capture groups, so we can do a direct name in the lookup
    
    print(regex)
    
    with open("input.txt", "r") as input:
        for line in input.readlines():
            for match in re.finditer(regex, line):
                # each match will be one of these three
                if match.lastgroup == 'mull' and doing:
                    # print(match)
                    result += mul(str=match.group())
                # otherwise, check for toggle
                elif match.lastgroup == 'do':
                    doing = True
                    print("Doing!")
                elif match.lastgroup == 'dont':
                    doing = False
                    print("Done.")
                
    print(result)