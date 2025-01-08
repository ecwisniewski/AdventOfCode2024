# Directions: up, down, left, right
directions = [0,1,2,3]
count = 0
hit_summits = []

def get_topographic_map():
    f = open("topographicmap.txt","r")
    file_map = []
    for t in f.readlines():
        line = []
        for i in t.strip():
            line.append(int(i))
        file_map.append(line)
    return file_map


def find_the_trailheads(graph):
    trailheads= []
    for x in range(0, len(graph)):
        for y in range(0, len(graph[0])):
            if graph[x][y] == 0:
                trailheads.append([x, y, 0])
    return trailheads


def traverse_the_map(graph, x, y, target=0):
    global count
    if 0 <= x < len(graph) and 0 <= y < len(graph[0]):
        if graph[x][y] == target and target == 9:
            count += 1
            if [x,y] not in hit_summits:
                hit_summits.append([x,y])
            #print(f'Found a 9 at {x},{y}')
        elif graph[x][y] == target:
            #print(f'Found target: {target} at {x},{y}')
            traverse_the_map(graph, x-1, y, target+1)
            traverse_the_map(graph, x+1, y, target+1)
            traverse_the_map(graph, x, y-1, target+1)
            traverse_the_map(graph, x, y+1, target+1)


topographic_map = get_topographic_map()
trailheads = find_the_trailheads(topographic_map)
total_score = 0
for t in trailheads:
    hit_summits = []
    traverse_the_map(topographic_map, t[0],t[1])
    t[2] = len(hit_summits)
    total_score += t[2]
#print(trailheads)
print(total_score)
print(count)