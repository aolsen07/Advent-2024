from functools import cache

def split_even_stones(stone):
    # stone will be passed in as a digit with even length
    s = str(stone)
    l = int(len(s) / 2)
    left = int(s[:l])
    right = int(s[l:])
    
    # check even number length
    return left, right 

@cache
def split_stone(stone, depth):
    if depth == 0:
        return 1
    
    if stone == 0:
        return split_stone(1, depth-1)
    
    if len(str(stone)) % 2 != 0:
        return split_stone(stone * 2024, depth-1)

    else:
        left, right = split_even_stones(stone)
        return split_stone(left, depth-1) + split_stone(right, depth-1)
    
def brute_force():
    NUM_BLINKS = 25
    MULT = 2024
    
    with open('input.txt', 'r') as f:
        stones = [int(stone) for stone in f.readline().strip().split()]
    
        for b, blink in enumerate(range(NUM_BLINKS)):
            # print("Blink {}: {}".format(b, stones))
            offset = 0
            
            # learning moment, enumerate() is dynamic and will expand if you insert more elements
            for i in range(len(stones)):
                i
                if stones[i] == 0:
                    stones[i] = 1
                    
                elif len(str(stones[i])) % 2 != 0:
                    stones[i] *= MULT
                
                else: 
                    left, right = split_even_stones(stones[i])
                    stones[i] = right
                    stones.append(left)
                    # inserting the stone at the end will reduce time complexity...
                    # ...rather than keeping the stones next to each other
                    
            print("Blink {} END: {}".format(b, len(stones)))

            
def recursive_sol(depth):
    with open('input.txt', 'r') as f:
        stones = [int(stone) for stone in f.readline().strip().split()]
        result = 0
        for stone in stones:
            result += split_stone(stone, depth)
            
        return result

if __name__ == '__main__':
    print(recursive_sol(25))
    print(recursive_sol(75))