
# keep turning right...



if __name__ == '__main__':

    direction = [(-1,0), (0,1), (1,0), (0,-1)] 
            #    UP, RIGHT, DOWN, LEFT ...
                
    GUARD = '^'
    WALL = '#'
    EMPTY = '.'
    
    board = []
    board_dirs = []
    guard_pos = []
    curr = 0    # north
    RESULT = 0  # p2 does not include start position
    
    with open('sample.txt') as file:
        for ri, line in enumerate(file.readlines()):
            row = [] # strings are immutable
            dir_row = []
            # save line then search for guard position
            for ci in range(len(line.strip())):
                if line[ci] == GUARD:
                    guard_pos = [ri, ci]
                    row.append('X')
                    dir_row.append([True, False, False, False])
                else:
                    row.append(line[ci])
                    dir_row.append([False, False, False, False])

            board.append(row)
            board_dirs.append(dir_row)
    
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
                board[guard_pos[0] + dy][guard_pos[1] + dx] = 'X'
                board_dirs[guard_pos[0]][guard_pos[1]][curr] = True
            
            case ('X'):
                
                # still increment path
                board_dirs[guard_pos[0] + dy][guard_pos[1] + dx][curr] = True
                guard_pos = [guard_pos[0] + dy, guard_pos[1] + dx]

                
                # check space where it would go if it would turn here
                ddy, ddx = direction[(curr + 1) % 4]
                new_direction = (curr + 1) % 4
                
                if (board_dirs[guard_pos[0] + ddy][guard_pos[1] + ddx][new_direction]):
                    print("Possible obstacle at {}".format((guard_pos[0] + ddy, guard_pos[1] + ddx)))
                    RESULT += 1 # could turn here
                            
    print('\n'.join([''.join(line) for line in board]))
    print(RESULT)
        