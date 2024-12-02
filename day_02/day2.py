from os import fspath            
  
# helper function to check if a level is "safe"

# safely increasing is strictly increasing and difference of 1-3           
def safely_increasing(levels):
    for i in range(1, len(levels)):
        # so, check if diff to next/prev item is in safe range
        diff = (int)(levels[i]) - (int)(levels[i-1]) 
        if diff not in range(1, 4):
            return False
    return True

# originally did safely increasing and decreasing, but removed to not repeat the similar logic

if __name__ == "__main__":
    
    result = 0
    with open(fspath('day2_input.txt'), 'r') as puzzle_input: 
        for line in puzzle_input.readlines():
            levels = [(int)(num) for num in line.split()]
            levels_reversed = levels.reverse()
            
            if safely_increasing(levels): 
                result += 1
                continue
            
            # if levels is actually decreasing, we can reverse it and check for strictness and differences with the same function
            # this is code golf. 
            
            levels.reverse() # in place reversal, then check again
            if safely_increasing(levels):
                result += 1
    
    print(result)
    