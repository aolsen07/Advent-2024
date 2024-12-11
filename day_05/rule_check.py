def check_update_rules(rule_set, update):
    for first in range(len(update)):
        for last in range(first, len(update)):
            
            if ((update[last], update[first])) in rule_set:
                print('{} in set'.format( (update[last], update[first]) ))
                return 0
            
    print(update)
    mid = int((len(update) - 1) / 2)
    return int(update[mid])

if __name__ == '__main__':
    rule_set = []
    breakpoint = 0 #line number to read updates
    file = open('input.txt', 'r')
    line = file.readline()
    
    while line != '\n':
        breakpoint += 1
        rule = line.strip().partition('|')
        rule_set.append((rule[0], rule[2])) # first page, later
        line = file.readline()
    
    result = 0
    updates = file.readlines() # remaining lines are updates
    
    for u in updates:
        result += check_update_rules(rule_set=rule_set, update=u.strip().split(','))
    
    print(result)
    file.close()
            

