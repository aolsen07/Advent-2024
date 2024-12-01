# historian hysteria
# pair smallest number in left with smallest number in right
# sounds like sorting
from os import fspath

# getting file import logic set in stone for faster future use
def process_input():
    with open(fspath('day1_input.txt'), 'r') as puzzle_input: 
        list1 = []
        list2 = {} # part 2 requires a map to get counts
        
        # each line has an id from the left and right lists
        for line in puzzle_input.readlines():
            ids = line.split()
            list1.append(ids[0])
            
            # check if key exists
            if ids[1] in list2:
                list2[ids[1]] += 1
            else:
                list2[ids[1]] = 1
            
        return list1, list2
    
    
if __name__ == "__main__":
    
    list1, list2 = process_input()
    
    # don't need to sort since order doesn't matter for the lookups
    
    result = 0
    
    for num in list1:
        if num in list2:
            # add similarity score
            result += int(num) * int(list2[num])
        
    print(result)   


