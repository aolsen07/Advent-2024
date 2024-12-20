   
class TrieNode:
    def __init__(self):
        self.child = [None] * 5
        self.wordEnd = False
        self.parent = None

def letter_idx(towel):
    match towel:
        case 'w':
            return 0
        case 'u':
            return 1
        case 'b':
            return 2
        case 'r':
            return 3
        case 'g':
            return 4
        
        case _:
            print('?')
            return ord(towel) # would return an error on retrieval anyway

def add_word(root, key):
    curr = root
    for c in key:
        
        i = letter_idx(c)
        if curr.child[i] == None:
            new_node = TrieNode()
            curr.child[i] = new_node
            
        curr = curr.child[i]
    curr.wordEnd = True

from functools import cache

def search(root, key):               
    
    # print(key)
    curr = root
    n = len(key)
    if n == 0:
        return True
    
    for i in range(n):
        next = letter_idx(key[i])
        
        if curr.child[next] is not None:       
            curr = curr.child[next]
        else:
            return False
        
        if curr.wordEnd:
            if search(root, key[i+1:]):
                return True
         
    # ending on a non-terminal, non-word node is not valid
    return False

    
    
if __name__ == '__main__':
    
    result = 0
    TrieRoot = TrieNode()
    
    with open('input.txt') as f:
        patterns = f.readline().strip().split(', ')
        for p in patterns:
            # print("inserting {}".format(p))
            add_word(TrieRoot, p.strip())
            
        f.readline() # skip empty line
        
        # rest of lines are designs
        for line in f.readlines():
            
            # check if part of the design exists in a trie of existing towels
            design = line.strip()
            i = 0
            # keep advancing search with index or stop search
            result += search(TrieRoot, design)
                        
    print(result)
        