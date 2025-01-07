import re

test = open("test_day5.txt", "r")


def get_rules_and_instructions():
    f = open("pages.txt","r")
    lines = f.read()
    rules = []
    rules_input = re.findall("\d+\|\d+", lines)
    for r in rules_input:
        rules.append(r.split("|"))
    instr = lines.split("\n\n")[1].split("\n")
    return rules, instr


def find_middle_values(instr):
    index = int(len(instr) / 2)
    return index, instr[index]


def correct_pages(i0,i1, pages):
    t = pages[i0]
    pages[i0]=pages[i1]
    pages[i1] = t


def check_page_follows_rules(rules, pages,flag=True):
    for r in rules:
        pg1 = pages.index(r[0]) if r[0] in pages else -1
        pg2 = pages.index(r[1]) if r[1] in pages else -1

        if pg1 > pg2 and (pg2 != -1 and pg1 != -1):
            # The second page is first and therefore wrong
            correct_pages(pg1,pg2,pages)
            return check_page_follows_rules(rules, pages,False)

    i,val = find_middle_values(pages)
    if flag:
        return -1
    return int(val)


rules, instructions = get_rules_and_instructions()
total = 0
for i in instructions:
    output = check_page_follows_rules(rules,i.split(","))
    if output > -1:
        total += output
print(total)
