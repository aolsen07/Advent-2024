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

# solution for part 2
# the idea is that we can remove one value at the problem spot
# an edge case was mentioned on reddit where the list starts increasing, but is ultimately decreasing
# this approach will weed out that scenario in list reversal, albeit a bit slower
# could rewrite this to be an int based error argument to accept more
def sketchy_increasing(levels, no_errors=True):
    for i in range(1, len(levels)):
        # so, check if diff to next/prev item is in safe range
        diff = (int)(levels[i]) - (int)(levels[i-1]) 
        if diff not in range(1, 4):

            if no_errors:   # create two shallow copies and remove possible problem values, see if it resolves the issue
                left = levels[:]; right = levels[:]
                left.pop(i)     # pop returns an int, so we let it remove the values
                right.pop(i-1)
                return sketchy_increasing(left, False) or sketchy_increasing(right, False) 
            else:
                return False # base case to end recursion

    return True

# originally did safely increasing and decreasing, but removed to not repeat the similar logic

if __name__ == "__main__":
    
    result = 0
    with open(fspath('day2_input.txt'), 'r') as puzzle_input: 
        for line in puzzle_input.readlines():
            levels = [(int)(num) for num in line.split()]
            levels_reversed = levels.reverse()
            
            # replaced the function call with error allowance
            if sketchy_increasing(levels, True): 
                result += 1
                continue
            
            # if levels is actually decreasing, we can reverse it and check for strictness and differences with the same function
            # this is code golf. 
            
            levels.reverse() # in place reversal, then check again
            if sketchy_increasing(levels, True):
                result += 1
    
    print(result)   # get the result to our terminal
    