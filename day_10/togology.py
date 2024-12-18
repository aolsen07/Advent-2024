
# brief exploration of terminal color with an imperfect gradient 
# these values are part of the SGR palette
color_codes = [46, 40, 34, 28, 22, 52, 88, 124, 160, 196]
color_string = "\x1B[48;5;{}m{}\x1b[0m"

def print_map(board):
    for line in board:
        print(''.join([color_string.format(str(color_codes[int(c)]), c) for c in line]))

if __name__ == '__main__':
    board = []
    # a good hiking trail goes from 0 to 9
    with open('input.txt') as f:
        for line in f.readlines():
            board.append(line.strip())

