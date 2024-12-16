"""
- Count total space needed
- Create array, allocate blocks
- Two pointer swap
    - right pointer moves digits to left pointer, which will be an empty space
- After swapping, checksum 
- loop until empty, summing up index * id
"""

NULL = -1
    
def part1(disk):
                
    # two pointers 
    left = 0
    right = len(disk) - 1
    
    while left < right:
        # we want left to point to an empty spot 
        if disk[left] != NULL:
            left += 1
        
        # and right to have a file
        elif disk[right] == NULL:
            right -= 1
            
        # once both are good, swap value
        else:
            disk[left] = disk[right]
            disk[right] = NULL
            
    CHECKSUM = 0
    for pos, num in enumerate(disk):
        if num == NULL:
            break
        CHECKSUM += pos * num
    print(CHECKSUM)
    

"""
This is not my most graceful solution, but brute force eventually works
"""
def part2(disk, file):
    
    # seek to find an id
    # len of file will be file[id * 2]
    empty_count = 0
    right = len(disk) - 1
    left = 0

    print(file)
    print(disk)
    while right > 0:
        
        if right % 100 == 0:
            print( '\r{}/{}'.format(right,len(disk)), end=None)
        
        # right has found a fragment
        if disk[right] != NULL:
            
            # find the length of this segment in our file input
            id = disk[right]
            fragment_len = int(file[id*2])
            left = 0
            
            # loop counting empty spaces to find a free space
            while left < right:
                
                if disk[left] == NULL:
                    empty_count += 1
                    if empty_count == fragment_len:
                    
                        empty_count = 0
                        disk[left-fragment_len+1:left+1] = disk[right-fragment_len+1:right+1]
                        disk[right-fragment_len+1:right+1] = [NULL for _ in range(fragment_len)]
                    
                        # problem style debug statement, dont use for full input
                        # print(''.join([str(num) if num != NULL else '.' for num in disk]))
                        break
                    
                else:
                    # ckprint("Reset")
                    empty_count = 0 # I HAD THIS AS == 0 SO IT WASNT RESETTING AND THIS TOOK ME AN EXTRA HOUR
                    
                # increment to keep going to next space
                left += 1
                
            # caught up, go to start of this fragment
            right = right - fragment_len
            
        # seek right to search for fragment
        else:
            right -= 1
            
    # solution, don't count null spaces
    CHECKSUM = 0
    for pos, num in enumerate(disk):
        if num != NULL:
            CHECKSUM += pos * num
    print(CHECKSUM)
        
if __name__ == '__main__':
    
    id = 0      # assign an id starting at 0
    disk = []   # we'll do a disk and append to it, and not think about runtime of that
        
    with open('input.txt') as f:
        file = f.readline().strip()
        # loop through lone input line, count 
        # use enumerate to check if the index is odd or even
        for i, num in enumerate(file):
            
            # digits alternate between files and free space
            if i % 2 == 0:  # file
                disk.extend([id for _ in range(int(num))])
                id += 1
            else:           # empty space
                disk.extend([NULL for _ in range(int(num))])
                
    part1(disk.copy())
    part2(disk.copy(), file)