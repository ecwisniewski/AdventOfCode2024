stones = {}

def add_stone(key,value=1,d=stones):
    #print(f'key {key} and value {value}')
    if key in d:
        d[key] += value
    else:
        d[key] = value

def blink():
    new_dict_items = {}
    for key in list(stones):
        value = stones[key]
        if key == 0:
            add_stone(1,value,new_dict_items)
        elif len(str(key)) %2 == 0:
            k = str(key)
            x = len(k) // 2
            add_stone(int(k[:x]), value,new_dict_items)
            add_stone(int(k[x:]), value,new_dict_items)
        else:
            k = key *2024
            add_stone(k,value,new_dict_items)
        del stones[key]
    for key,value in new_dict_items.items():
        add_stone(key,value)


i = "27 10647 103 9 0 5524 4594227 902936"
j = "125 17"
my_list = j.split()
for r in i.split():
    add_stone(int(r))
print(stones)
for _ in range(0,75):
    blink()
    #print(stones)
    #count = 0
    #for value in stones.values():
    #    count += value
    #print(count)
print(stones)
count =  0
for value in stones.values():
    count += value
print(count)