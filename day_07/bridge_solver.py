# test operators, break when array is of length 2
def test_operators(target, nums):
    if len(nums) == 2:
        if nums[0] + nums[1] == target:
            return True
        elif nums[0] * nums[1] == target:
            return True
        elif concat_ints(nums[0], nums[1]) == target:
            return True
        else:
            return False
        
    else:
        return (test_operators(target, [nums[0] + nums[1]] + nums[2:]) or test_operators(target, [nums[0] * nums[1]] + nums[2:])) or test_operators(target, [concat_ints(nums[0], nums[1])] + nums[2:])
        
def concat_ints(a, b):
    return int(str(a) + str(b))

if __name__ == '__main__':
    
    result = 0
    
    with open('sample.txt', 'r') as f:
        for line in f.readlines():
            print('\n')
            target, nums = [s for s in line.strip().split(':')]
            nums = [int(num) for num in nums.split()]
                        
            if test_operators(int(target), nums):
                result += int(target)
            
    print(result)