i = "27 10647 103 9 0 5524 4594227 902936"
j = "125 17"
for p in range(0,75):
    my_List = j.split()
    print(f'for {p} length {len(my_List)}')
    my_list = [
        '1' if x == '0' else
        f'{x[:len(x)//2]} {int(x[len(x)//2:])}' if len(x) %2 == 0 else
        str(int(x)*2024)
        for x in my_List
    ]
    j=""
    for i in my_list:
        j+= f'{i} '
    #print(j)
my_list = j.split()
print(len(my_list))