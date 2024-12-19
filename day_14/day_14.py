# struct class with simulation / retrieval methods
class Robot:
    def __init__(self, p, v):
        self.x, self.y = int(p[0]), int(p[1])
        self.dx, self.dy = int(v[0]), int(v[1])
        
    def update(self, t):
        for _ in range(t):
            self.y = (self.y + self.dy + n) % n 
            
            self.x = (self.x + self.dx + m) % m
            
            
    def quadrant(self):
        if self.y < ((n - 1) / 2) and self.x < ((m - 1) / 2):
            return 1
        if self.y < ((n - 1) / 2) and self.x > ((m - 1) / 2):
            return 2
        if self.y > ((n - 1) / 2) and self.x < ((m - 1) / 2):
            return 3
        if self.y > ((n - 1) / 2) and self.x > ((m - 1) / 2):
            return 4
        else:
            return 0
    
    def pos(self):
        return self.x, self.y
            
    
def print_board(robots, n, m):
    
    board = [[0 for _ in range(m)] for _ in range(n)]
    for r in robots:
        x, y = r.pos()
        board[y][x] += 1
        
    for row in board:
        # color coding the active tiles to try and find the tree
        print(''.join(['.' if s == 0 else "\033[92m#\033[0m" for s in row]))
         

def part1(robots):
    q1 = 0 
    q2 = 0 
    q3 = 0 
    q4 = 0
    
    rob.update(TURNS)
    # print(rob.quadrant(), rob.pos())
            
    # Increment Quadrant counter after the simulation
    match rob.quadrant():
        case 1:
            q1 += 1
        case 2:
            q2 += 1
        case 3: 
            q3 += 1
        case 4: 
            q4 += 1
        case 0:
            print('Passed!')
            pass
    
    print("q1: {}, q2: {}, q3: {}, q4: {}".format(q1,q2,q3,q4))
    print(q1 * q2 * q3 * q4)
    print_board(robots, n, m)
    
    
def part2(robots):
    t = 0
    board = [[0 for _ in range(m)] for _ in range(n)]

    # takes a second, but continually adjusts robot position until it finds an edge for the tree
    while True:
        t += 1
        for r in robots:
            r.update(1)
            x, y = r.pos()
            board[y][x] += 1
                        
        for i in range(n):
            in_a_row = 0
            for j in range(m):
                if board[i][j] != 0:
                    in_a_row += 1
                    if in_a_row > 10:
                        
                        print_board(robots, n, m)
                        print("Turn {}:".format(t))
                        input()
                else:
                    in_a_row = 0
                board[i][j] = 0

         
import re

if __name__ == '__main__':
    
    # SET BOUNDS!
    n = 103 # height
    m = 101 # width 
    
    TURNS = 100
    format = r'-?\d{1,3},-?\d{1,3}'
    reg = re.compile(format)
    robots = []
    
    with open('input.txt') as f:
        for line in f.readlines():
            
            # Process string for position and velocity
            pv = reg.findall(line.strip()) 
            #print(pv)
            p, v = pv[0].split(','), pv[1].split(',')
            #print(p,v)
            
            # Simulate robot movement over t turns
            rob = Robot(p, v)
            robots.append(rob)
            
        part2(robots)   # !!! switch this line to see other result
    
