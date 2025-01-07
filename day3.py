import common as c

test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


# parse out mul instructions
def parse_instructions(instructions: object) -> object:
    corrupted_ins = c.make_string_list(instructions)
    parsed_ins = []
    do_mul = True

    j = 0
    for i in range(0, len(corrupted_ins)):
        j = i
        instruction = []
        if corrupted_ins[j:j + 4] == ["m", "u", "l", "("]:
            j += 4
            if corrupted_ins[j].isdigit():
                d=""
                while corrupted_ins[j].isdigit():
                    d += corrupted_ins[j]
                    j += 1

                instruction.append(d)
                if corrupted_ins[j] == ",":
                    j = j + 1
                    if corrupted_ins[j].isdigit():
                        d=""
                        while corrupted_ins[j].isdigit():
                            d += corrupted_ins[j]
                            j = j + 1
                        instruction.append(d)
                        if corrupted_ins[j] == ")":
                            if do_mul:
                                parsed_ins.append(instruction)

        if corrupted_ins[j:j+7] == ["d","o","n","'","t","(",")"]:
            do_mul = False
        if corrupted_ins[j:j+4] == ["d","o","(",")"]:
            do_mul = True

    return parsed_ins


def generate_instructions_from_corrupted_report():
    f = open("corrupted_data.txt", "r")
    corrupted_instructions = f.read()

    return parse_instructions(corrupted_instructions)


# do multiplications
def sum_of_mul_instructions(instructions):
    total_sum =0
    for inst in instructions:
        total_sum += int(inst[0]) * int(inst[1])
    return total_sum

# add everything together

print(sum_of_mul_instructions(generate_instructions_from_corrupted_report()))
