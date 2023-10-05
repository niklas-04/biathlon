from random import randint
def splash():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('               Biathlon')
    print()
    print('           A hit or miss game')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
splash()

open = 0
closed = 1
def is_open(n):
    if n==open:
        return True
    else:
        return False

def is_closed(n):
    if n==closed:
        return True
    else:
        return False 

def new_targets():
    targets = []
    for x in range(5):
        targets.append(open)
    return targets
    
def close_target(targets, position):
    targets[position] = closed
    return targets

def points(targets):
    count = 0
    for x in targets:
        if is_closed(x):
            count = count + 1
    return count

def targets_to_string(targets):
    s = ""
    for x in targets:
        if is_closed(x):
            s = s + "* "
        else:
            s = s + "0 "
    return s
def view_targets(targets):
    for x in range(len(targets)):
        print (str(x+1) + " ", end="")
    print()
    print (targets_to_string(targets))
    
def random_hit():
    if randint(0,1) == 1:
        return True
    else:
        return False
    
def shoot(targets):
    position = input()
    parsed_position = parse_target(position)
    hitOrNot = random_hit()
    
    if parsed_position > 0 and parsed_position <= len(targets):   
        if not hitOrNot:
            return "Miss"
        elif is_open(targets[parsed_position-1]) and hitOrNot:
            close_target(targets, parsed_position-1)
            return "Hit on open target" 
        else:
            return "Hit on closed target"
    else:
        print("ogiltigt val")
    
def parse_target(string):
    if string.isnumeric():
        return int(string)
    
    
targets = new_targets()
        