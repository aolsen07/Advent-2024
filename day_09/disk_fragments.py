"""
- Count total space needed
- Create array, allocate blocks
- Two pointer swap
    - right pointer moves digits to left pointer, which will be an empty space
- After swapping, checksum 
- loop until empty, summing up index * id
"""

NULL = -1

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