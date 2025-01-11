#Regex???

import re

def separate_evens(match):
    m = match.group(1)
    print(m)
    size = len(m)//2
    return f' {m[:size]} {m[size:]} '

def change_digitis(match):
    m = match.group(1)
    if m == '0':
        return '1'
    elif len(m) %2 == 0:
        size = len(m) // 2
        return f'{int(m[:size])} {int(m[size:])}'
    else:
        return str(int(m) * 2024)

def mult_2k24(match):
    m = match.group(1)
    return

def do_blink_digit_match(input):
    input = re.sub(r"(\d+)",change_digitis,input)
    #input = re.sub(r"([2 - 9])\s | (\d{2, })",change_digitis,input)
    #input = re.sub(r"0\s","1 ",input)
    return input

def do_blink(input):
    input = re.sub(r"\s\s","2024",input)
    #input = re.match("\s")
    # If stone is engraved with the number 0, replaced by 1
    input = re.sub(r"\s0\s"," 1 ",input)
    m = re.search(r"\s((\d{2})*)\s",input)
    print(m.groups())
    print(m.group(2))
    input = re.sub(r"\s((\d{2})*)\s",separate_evens,input)
    # If the stone is even, replaced by 2 stones LH and RH
    print(re.sub(r"(\s[2-9])\s|\s(\d{2,})\s",input))
    # Else stone is replace by new stone - old x 2024
    return input

def another_attempt(input):
    for i in range(0,len(input)):
        if input[i] == '0':
            input[i] = '1'
        elif len(input[i]) % 2 == 0:
            size = len(input[i])//2
            new1 = int(input[i][:size])
            new2 = int(input[i][size:])
            input[i] = f'{str(new1)} {str(new2)}'
        else:
            new = str(int(input[i]) * 2024)
            #print(type(input[i]))
            input[i] = new
    out = ""
    for i in input:
        out += f'{i} '
    input = out.split()
    return input


i = "27 10647 103 9 0 5524 4594227 902936"
j = "125 17"
for p in range(0,75):
    i = do_blink_digit_match(i)
    l = i.split()
    print(f'at {p+1} len {len(l)}')
#x = j.split()
#p=1
#m=2
#n= 1
#for _ in range(0,5):
#    for _ in range(0,5):
#        n = len(j)
#        for nn in range(0,n):
#            print(j[nn][])
#            j[nn] = do_blink_digit_match(j[nn])
#    t = j
#   j = []
#    for q in t:
#        s = len(t) // m
#        for w in range(0,m):
#            j.append(t[s*w:s*w+1])
#    m+=1
#print(j)




#for _ in range(0,25):
  #  x = another_attempt(x)
  #  print(f'at {p} = {len(x)}')
 #   p+=1
#x_size = len(x)//4
#x_1 = x[:x_size]
#x_2 = x[x_size:x_size*2]
#x_3 = x[x_size*2:x_size*3]
#x_4 = x[x_size*3:]
#for _ in range(0,20):
 #   x_1 = another_attempt(x_1)

  #  x_2 = another_attempt(x_2)
   # x_3 = another_attempt(x_3)
   # x_4 = another_attempt(x_4)
   # print(f'at {p} = {len(x_1)}')
   # p += 1
#print(len(x))