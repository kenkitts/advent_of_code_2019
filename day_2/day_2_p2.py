with open('input.txt', 'rt') as file:
    inputs = []
    for i in file.readlines():
        for ii in i.split(','):
            inputs.append(int(ii))


def calc(noun,verb):
    c_inputs = inputs.copy()
    idx = 0
    opcode = c_inputs[idx]
    c_inputs[1], c_inputs[2] = noun, verb
    while opcode != 99:
        int_1, int_2, int_3 = c_inputs[idx + 1], c_inputs[idx + 2], c_inputs[idx + 3]
        if opcode == 1:
            c_inputs[int_3] = c_inputs[int_1] + c_inputs[int_2]
        elif opcode == 2:
            c_inputs[int_3] = c_inputs[int_1] * c_inputs[int_2]
        idx += 4
        opcode = c_inputs[idx]
    return c_inputs[0]

def start():
    for x in range(0, 100):
        for y in range(0, 100):
            if calc(x, y) == 19690720:
                return x, y


noun, verb = start()
answer = 100 * noun + verb
print('The answer to day 2, part 2 is: {}'.format(answer))