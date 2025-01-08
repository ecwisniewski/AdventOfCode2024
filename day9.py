test = "2333133121414131402"

def get_input():
    f = open("input.txt","r")
    disk = f.read()
    return disk.strip()

def id_space_allocation(input):
    id = 0
    space = []
    alloc = []
    blocks=0
    print(len(input))
    if len(input) % 2:
        input += '0'
    for i in range(0,len(input)):
        if i % 2 == 0:
            for j in range(0,int(input[i])):
                alloc.append(str(id))
            blocks = input[i]
        else:
            for j in range(0,int(input[i])):
                alloc.append('.')
            free = input[i]
            id += 1
            space.append({"id": id-1, "blocks":int(blocks),"free":int(free),"visual":alloc})
            alloc = []

    return space


def move_backwards_free_space(input):
    for i in range(0,len(input),1):
        if input[i] == '.' and any(item != '.' for item in input[i:len(input)-1]):
            for j in range(len(input)-1,0,-1):
                if input[j] != '.':
                    input[i] = input[j]
                    input[j] = '.'
                    break

    return [x for x in input if x != '.']


def move_backwards_exact_free_space(input):
    for i in reversed(input):
        blocks = i["blocks"]
        for j in input[0:i["id"]+1]:
            free = j["free"]
            if free >= blocks:
                for k in range(0,len(j["visual"])):

                    if j["visual"][k] != ".":
                        continue
                    else:
                        j["visual"][k:k+blocks] = i["visual"][0:blocks]
                        j["free"] = free - blocks
                        i["visual"][0:blocks] = ['.']*blocks
                        break
                break






def calculate_final_checksum(input):
    checksum = 0
    for i in range(0,len(input)):
        if input[i] != '.':
            checksum += i*int(input[i])
    print(checksum)


def turn_big_list(allocation):
    big_list = []
    for a in allocation:
        for v in a["visual"]:
            big_list.append(v)
    return big_list

#calculate_final_checksum(move_backwards_free_space(id_space_allocation(get_input())))
allocation = id_space_allocation(get_input())
#print(allocation)
#print(allocation)

#big_list = turn_big_list(allocation)
#calculate_final_checksum(move_backwards_free_space(turn_big_list(allocation)))

move_backwards_exact_free_space(allocation)
#print(allocation)
print(turn_big_list(allocation))
calculate_final_checksum(turn_big_list(allocation))
