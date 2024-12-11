# they hate to see me move in mysterious ways

# class initialization in prep for part 2
class CeresSearcher:
    
    def __init__(self):
                
        self.grid = []
        with open("input.txt", "r") as file:
            for line in file.readlines():
                self.grid.append(line)
        self.n = len(self.grid)
        self.m = len(self.grid[0])
                
        # save directions for traversal
        self.directions = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    self.directions.append((dx, dy))
    
    # higher level loop, search in each direction in each cell
    def solve(self, search_string="XMAS"):
        result = 0
        for y in range(self.n):
            for x in range(self.m):
                for d in self.directions:
                    # O(n * m * constant time for all directions)
                    result += self.word_search(x, y, d, search_string)
        return result
        
    def word_search(self, x, y, direction, search_string): 
        dx, dy = direction
        # this actually helped understand how to repeat loops less
        for k, char in enumerate(search_string):
            ii = x + k * dx
            jj = y + k * dy
            if not (0 <= ii < self.n and 0 <= jj < self.m):
                return False
            if self.grid[ii][jj] != char:
                return False
        return True
        
if __name__ == '__main__':
    search = CeresSearcher()
    print(search.solve()) # print result