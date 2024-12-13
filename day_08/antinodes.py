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
                        
                        # didn't need this slope reduction snippet
                        
                        # regardless of distance means thinking about slope, so reduce units if the slope allows it
                        #if dy % dx == 0:
                            #dy = int(dy / dx)
                            #dx = int(dx / dx)
                        
                        # calculate initial changes
                        ant1 = (y + dy, x + dx)
                        ant2 = (mate_y - dy, mate_x -dx)
                        
                        # in each direction, mark possible locations along the line
                        # if vs while for one antenna or continuous until o.o.b.
                        while (0 <= ant1[1] < m) and (0 <= ant1[0] < n):
                            if not antinode_map[ant1[0]][ant1[1]]:
                                RESULT += 1
                                antinode_map[ant1[0]][ant1[1]] = True
                            ant1 = (ant1[0] + dy, ant1[1] + dx)

                        while (0 <= ant2[1] < m) and (0 <= ant2[0] < n):
                            if not antinode_map[ant2[0]][ant2[1]]:
                                RESULT += 1
                                antinode_map[ant2[0]][ant2[1]] = True
                            ant2 = (ant2[0] - dy, ant2[1] - dx)

                    # save antenna for future search                                
                    antenna_pos[c].append((y,x))
        
        # debug printout to view all antinode positions
        for j, r in enumerate(antinode_map):
            print(''.join(('#' if c else lines[j][i] for i, c in enumerate(r))))
        # lookups to include the chars for all the antennas would be more complex
            
        print(RESULT)