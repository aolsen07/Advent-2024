# brief exploration of terminal color with an imperfect gradient 
# these values are part of the SGR palette
color_codes = [46, 40, 34, 28, 22, 52, 88, 124, 160, 196]
color_string = "\x1B[48;5;{}m{}\x1b[0m"

def print_map(board, colored = False):
    if colored:
        for line in board:
            print(''.join([color_string.format(str(color_codes[int(c)]), c) for c in line]))
    else: 
        for line in board:
            print(''.join([c for c in line]))

# start real solution

from functools import cache
directions = [(-1,0), (0,1), (1,0), (0,-1)] 

@cache
def hike_score(row, column, height):
    if height == 9:
        return [(row, column)]
    
    peaks = set()
    for dy, dx in directions:
        if 0 <= row + dy < n and 0 <= column + dx < m and int(board[row + dy][column + dx]) == (height + 1):
            peaks.update(peak for peak in hike_score(row + dy, column + dx, height+1))
    return peaks
            
            
@cache
def hike_rating(row, column, height):
    if height == 9:
        return 1
    
    peaks = 0
    for dy, dx in directions:
        if 0 <= row + dy < n and 0 <= column + dx < m and int(board[row + dy][column + dx]) == (height + 1):
            peaks += hike_rating(row + dy, column + dx, height + 1)
    return peaks

if __name__ == '__main__':
    board = []
    # a good hiking trail goes from 0 to 9
    with open('input.txt') as f:
        for line in f.readlines():
            board.append(line.strip())
        
    p1_result = 0
    p2_result = 0
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                score = hike_score(i, j, 0)
                rating = hike_rating(i, j, 0)
                
                p1_result += len(score)
                p2_result += rating
                print("{}, {} has score of {} and a rating of {}".format(i, j, score, rating))
                
    print(p1_result)
    print(p2_result)
    

