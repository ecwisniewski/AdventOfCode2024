#directions: up, right, down, left
from typing import List, Any

d = [0,1,2,3]

def get_map():
    f = open("guardpath.txt","r")
    input = f.read()

    map_matrix = []
    for i in input.split('\n'):
        t = []
        for j in i:
            t.append(j)
        map_matrix.append(t)

    return map_matrix


def find_starting_point(map):
    for row in map:
        if '^' in row:
            #print(row)
            i = map.index(row)
            for c in row:
                if c == '^':
                    #print(c)
                    j = row.index(c)
                    return i,j
    return -1,-1


def check_obstruction(map,x,y):
    t = map[x][y]
    if map[x][y] == "#" or map[x][y] == "O":
        return True
    return False


def check_inside_map(map,x,y):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    return True


def move_guard(g_map, x, y, d):
    new_x = x
    new_y = y

    if d == 0:
        # Move Forward
        new_x -= 1
    elif d == 1:
        # Move Right
        new_y += 1
    elif d == 2:
        # Move Down
        new_x += 1
    elif d == 3:
        # Move Left
        new_y -= 1
    else:
        return -1,-1,d

    if check_inside_map(g_map, new_x, new_y):

        if not check_obstruction(g_map, new_x, new_y):
            x = new_x
            y = new_y
            if d == 0 or d == 2:
                g_map[x][y] = '|'
            elif d == 1 or d == 3:
                g_map[x][y] = '-'
        else:
            d += 1
            if d > 3:
                d = 0
            g_map[x][y] = "+"

        return x, y, d
    else:
        return x, y, -1


def loop_test(g_map, x, y, d=0):
    # return True if loop
    times = 0
    while times < (len(g_map)*len(g_map[0])):
        new_x = x
        new_y = y

        if d == 0:
            # Move Forward
            new_x -= 1
        elif d == 1:
            # Move Right
            new_y += 1
        elif d == 2:
            # Move Down
            new_x += 1
        elif d == 3:
            # Move Left
            new_y -= 1

        if check_inside_map(g_map, new_x, new_y):

            if not check_obstruction(g_map, new_x, new_y):
                x = new_x
                y = new_y
                if d == 0 or d == 2:
                    g_map[x][y] = '|'
                elif d == 1 or d == 3:
                    g_map[x][y] = '-'
            else:
                d += 1
                if d > 3:
                    d = 0
                g_map[x][y] = "+"
        else:
            return False
        times +=1
    return True


def create_obstructions(g_map, x, y, start_x, start_y):
    new_map = get_map()
    found = False
    # add obstruction
    new_map[x][y] = 'O'
    # run a move test
    if loop_test(new_map, start_x,start_y):
        found = True
        #for m in new_map:
        #    print(m)
    del new_map
    return found


guard_map = get_map()
empty_map = guard_map.copy()
start_x,start_y = find_starting_point(guard_map)
x = start_x
y = start_y
print(f'{x,y}')
move = True
dir = 0
#print(guard_map)
while move:
    x,y,dir = move_guard(guard_map, x,y,dir)
    if x == -1 or y == -1 or dir == -1:
        move = False
count = 0
for m in guard_map:
  count += (m.count('-') + m.count('+') + m.count("|"))

count2 = 0
for i in range(0,len(guard_map)):
    for j in range(0,len(guard_map[0])):
        if guard_map[i][j] == '-' or guard_map[i][j] == '|' or guard_map[i][j] == '+':
            if create_obstructions(empty_map,i,j,start_x,start_y):
                count2 += 1

print(count2)