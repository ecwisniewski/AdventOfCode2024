import re

test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def parse_instructions(instructions):
    parsed_ins = re.findall("mul\(\d+\,\d+\)|do\(\)|don't\(\)", instructions)
    return parsed_ins


def generate_instructions_from_corrupted_report():
    f = open("corrupted_data.txt", "r")
    corrupted_instructions = f.read()

    return parse_instructions(corrupted_instructions)


def sum_mul_instructions(instructions):
    do_mul = True
    total_sum = 0
    for i in instructions:
        if i.find("m") != -1 and do_mul:
            d = re.findall("\d+", i)
            total_sum += int(d[0]) * int(d[1])
        elif i == "do()":
            do_mul = True
        elif i == "don't()":
            do_mul = False

    return total_sum


print(sum_mul_instructions(generate_instructions_from_corrupted_report()))
