import common as c
test = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20"


def get_ops():
    operations = []
    f = open("calibration.txt","r")
    input = f.read()
    for i in test.split('\n'):
        j = i.split(":")
        digits = []
        for d in j[1].split():
            digits.append(int(d))
        operations.append({'result': int(j[0]), 'values': digits})
    return operations


def add_mult_concat(ops, result, val=0):
    if len(ops) == 1:
        last_val = ops[0]
        # do mult
        if val != 0:
            if result == val * last_val:
                return True
            elif result == val + last_val:
                return True
            elif result == int(str(val) + str(last_val)):
                return True
        else:
            if result == 1 * last_val:
                return True
            elif result == val + last_val:
                return True
            elif result == last_val:
                return True
    else:
        item = ops[0]
        new_ops = ops[1:]
        if add_mult_concat(new_ops, result,val * item) or add_mult_concat(new_ops, result,val + item) or add_mult_concat(new_ops, result,int(str(val) + str(item))):
            return True

    return False


def is_true_calibration(op):
    t = op['values']
    res = op['result']
    return add_mult_concat(t,res)



operations = get_ops()
total = 0
for o in operations:
    if is_true_calibration(o):
        total += o['result']
print(total)
