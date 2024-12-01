# historian hysteria
# pair smallest number in left with smallest number in right
# sounds like sorting
from os import fspath

# getting file import logic set in stone for faster future use
def process_input():
    with open(fspath('day1_input.txt'), 'r') as puzzle_input: 
        list1 = []
        list2 = []
        
        # each line has an id from the left and right lists
        for line in puzzle_input.readlines():
            ids = line.split()
            list1.append(ids[0])
            list2.append(ids[1])
            
        return list1, list2
    
    
if __name__ == "__main__":
    
    list1, list2 = process_input()
    
    # sort lists to correlate the ids
    list1.sort()
    list2.sort()
    
    result = 0
    
    for i in range(len(list1)):
        result += abs(int(list1[i]) - int(list2[i]))
        
    print(result)   


