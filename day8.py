fmap = []


def get_frequency_map():
    f = open("frequency-map.txt", "r")
    txt_fmap = f.readlines()
    for line in txt_fmap:
        new_line = []
        for i in line.strip():
            new_line.append(i)
        fmap.append(new_line)


def check_point(point, boundX, boundY):
    if point[0] < 0 or point[0] >= boundX:
        return False
    if point[1] < 0 or point[1] >= boundY:
        return False
    return True


def find_new_points(pointA, pointB, boundX, boundY, output=[]):
    x_A = pointA[0]
    y_A = pointA[1]
    x_B = pointB[0]
    y_B = pointB[1]
    x = x_B - x_A
    y = y_B - y_A
    if boundX > boundY:
        bound = int(boundX)
    else:
        bound = int(boundY)

    for k in range(1,bound):
        new_points = [[x_B + k*x, y_B + k*y], [x_A - k*x, y_A - k*y]]
        for n in new_points:
            #print(n)
            if check_point(n, boundX, boundY):
                #print("True")
                output.append(n)
            #else:
            #print("False")
    #print(output)
    return output


def get_locations():
    locations = {}
    for i in range(0, len(fmap)):
        for j in range(0, len(fmap[0])):
            if fmap[i][j] != ".":
                if fmap[i][j] in locations:
                    new = locations.get(fmap[i][j])
                    new.append([i, j])
                    locations[fmap[i][j]] = new
                else:
                    locations[fmap[i][j]] = [[i, j]]
    return locations


def print_points_map(points):
    copy_map = fmap.copy()
    for p in points:
        copy_map[p[0]][p[1]] = '#'
    #print(copy_map)
    for l in copy_map:
        print(l)


get_frequency_map()
#print(fmap)
boundX = len(fmap)
boundY = len(fmap[0])
locs = get_locations()
#print(locs)
all_points = []
for key, value in locs.items():
    #print(key)
    for i in range(0, len(value)):
        for j in range(i + 1, len(value)):
            #print(f'Point A: {value[i]}, Point B: {value[j]}')
            all_points.append(value[i])
            all_points.append(value[j])
            find_new_points(value[i], value[j], boundX, boundY, all_points)
#print(all_points)
final = []
[final.append(p) for p in all_points if p not in final]
#print(final)
print(len(final))
#print(find_new_points([2,1],[3,2],9,6))

#print_points_map(all_points)
