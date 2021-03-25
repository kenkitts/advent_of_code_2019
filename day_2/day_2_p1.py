with open('input.txt', 'rt') as file:
    inputs = []
    for i in file.readlines():
        for ii in i.split(','):
            inputs.append(int(ii))

idx = 0
opcode = 0
inputs[1], inputs[2] = 12, 2

while opcode != 99:
    opcode = inputs[idx]
    int_1, int_2, int_3 = inputs[idx + 1], inputs[idx + 2], inputs[idx + 3]
    if opcode == 1:
        inputs[int_3] = inputs[int_1] + inputs[int_2]
    elif opcode == 2:
        inputs[int_3] = inputs[int_1] * inputs[int_2]
    idx += 4
    opcode = inputs[idx]

print('The answer to day 2, part 1 is: {}'.format(inputs[0]))
