if __name__ == '__main__':
    # map of sets to map antennas
    antenna_pos = {}
    # 2d arrays of possible antinode positions
    RESULT = 0
    
    with open('input.txt') as f:
        lines = f.readlines()
        n = len(lines)
        m = len(lines[0].strip())
        antinode_map = [[False for _ in range(m)] for _ in range(n)] 

        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                
                # check for empty space
                if c == '.':
                    continue
                
                # if c is not yet logged, initialize
                elif c not in antenna_pos:
                    antenna_pos[c] = [(y, x)]
                    
                    # print(antinode_maps[c])
                
                else: 
                    for (mate_y, mate_x) in antenna_pos[c]:
                        # get differences
                        dy = mate_y - y 
                        dx = mate_x - x
                        
                        ant1 = (y + dy+dy, x + dx+dx)
                        ant2 = (mate_y - dy-dy, mate_x -dx - dx)
                        
                        if (0 <= ant1[1] < m) and (0 <= ant1[0] < n) and not antinode_map[ant1[0]][ant1[1]]:
                            RESULT += 1
                            antinode_map[ant1[0]][ant1[1]] = True
                        
                        if (0 <= ant2[1] < m) and (0 <= ant2[0] < n) and not antinode_map[ant2[0]][ant2[1]]:
                            RESULT += 1
                            antinode_map[ant2[0]][ant2[1]] = True
                                
                    antenna_pos[c].append((y,x))
        
        for j, r in enumerate(antinode_map):
            print(''.join(('#' if c else lines[j][i] for i, c in enumerate(r))))
            
        print(RESULT)