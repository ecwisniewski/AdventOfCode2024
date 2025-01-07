import numpy as np
import pandas as pd

def get_map():
    f = open("test_antannes.txt","r")
    input = f.read().split("\n")
    l = []
    antenna_map = []
    for i in input:
        l = []
        for j in i:
            l.append(j)
        antenna_map.append(l)

    np_antenna_map = np.array(antenna_map)
    #print(np_antenna_map)
    return np_antenna_map


def map_antenna(df,puzzle):
    print(df)
    list_of_new_indexes = []
    for i,j in df.iterrows():
        in1 = j['index']
        for k,l in df.iterrows():
            in2 = l['index']
            if in1 == in2:
                print(f'check {in1} {in2}')
            else:
                new_i1 = [in1[0]-in2[0], in1[1]-in2[1]]
                new_i2 = [-1*new_i1[0],-1*new_i1[1]]
                list_of_new_indexes.append([in1[0]-new_i2[0],in1[1]-new_i2[1]])
                list_of_new_indexes.append(([in2[0]-new_i1[0],in2[1]-new_i1[1]]))
    print(list_of_new_indexes)

    for l in list_of_new_indexes:
        if not (l[0] < 0 or l[1] < 0 or l[0] >= len(list_of_new_indexes) or l[1] >= len(list_of_new_indexes[0])):
            puzzle[l[0],l[1]] = '#'

    print(puzzle)
    return list_of_new_indexes

puzzle = get_map()
final = puzzle.copy()
no_dots = np.where(puzzle!='.')
#print(no_dots)
letters_index = []
for i in range(0,len(no_dots[0])):
    row = no_dots[0][i].item()
    col = no_dots[1][i].item()
    value = puzzle[row,col].item()
    letters_index.append({"value":value, "index": [row,col]})
#print(letters_index)
#counter = {}
data = pd.DataFrame.from_dict(letters_index)
#print(data)
unique_letters = data['value'].unique()

for u in unique_letters:
    l = map_antenna(data.loc[data['value'] == u],final)

#for c in counter:

