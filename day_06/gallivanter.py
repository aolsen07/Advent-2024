# directions = {"UP":(1, 0), "DOWN":(-1, 0), "LEFT": (0, 1), "RIGHT": (0, -1)}


# keep turning right...



if __name__ == '__main__':

    direction = [(-1,0), (0,1), (1,0), (0,-1)] 
    
    GUARD = '^'
    WALL = '#'
    VISITED = 'X'
    EMPTY = '.'
    
    
    
    board = []
    guard_pos = []
    curr = 0
    RESULT = 1 # includes start position
    
    with open('input.txt') as file:
        for ri, line in enumerate(file.readlines()):
            row = [] # strings are immutable
            # save line then search for guard position
            for ci in range(len(line.strip())):
                if line[ci] == GUARD:
                    guard_pos = [ri, ci]
                    row.append('X')
                else:
                    row.append(line[ci])

            board.append(row)
    
    n = len(board)
    m = len(board[0])
    dy, dx = direction[curr]            
    # iterate until the guard leave the bounds
    while (0 <= guard_pos[0] + dy < n) & (0 <= guard_pos[1] + dx < m):
        
        # using match here to help with readability
        # depending on the space ahead of the guard, either turn, count, or advance        
        match (board[guard_pos[0] + dy][guard_pos[1] + dx]):
            # check for collision, if facing wall then rotate
            case ('#'):
                curr = (curr + 1) % 4
                dy, dx = direction[curr]
        
            case ('.'):
                RESULT += 1
                board[guard_pos[0] + dy][guard_pos[1] + dx] = VISITED
            
            case ('X'):
                guard_pos = [guard_pos[0] + dy, guard_pos[1] + dx]
                            
    print('\n'.join([''.join(line) for line in board]))
    print(RESULT)
        