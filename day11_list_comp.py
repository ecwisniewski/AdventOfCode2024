import numpy as np

size = 200000000#9223372036854775807
input = np.empty(size,dtype='U8')
count: int = 0
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))


def option2():
    global count
    print(input)
    for x in range(0,count):
        #print(input[x])
        if input[x] == '0':
            input[x] = '1'
        elif len(input[x]) %2 == 0:
            y = input[x]
            input[x] = y[:len(y)//2]
            input[count] = str(int(y[len(y)//2:]))
            count+=1
        else:
            y = input[x]
            input[x] = str(int(y)*2024)


i = "27 10647 103 9 0 5524 4594227 902936"
j = "125 17"
my_list = j.split()
for r in j.split():
    input[count] = r
    count += 1
for p in range(0,75):
    option2()
    #print(input)
    print(f'for {p} length {count}')
print(count)

#for p in range(0,6):
#    print(f'for {p} length {len(my_list)}')
#    #print(my_list)
#    my_list = [
#        '1' if x == '0' else
#        f'{x[:len(x)//2]} {int(x[len(x)//2:])}' if len(x) %2 == 0 else
#        str(int(x)*2024)
#        for x in my_list
#    ]
#    for m in range(0,len(my_list)):
#        if " " in my_list[m]:
#            n = my_list[m].split()
#            my_list[m] = n[0]
#            my_list.append(n[1])
#    print(my_list)
    #print()
    #print(j)
#my_list = j.split()
#print(len(my_list))