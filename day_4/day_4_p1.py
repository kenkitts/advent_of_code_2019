with open(file='input.txt', mode='rt') as file:
    start, stop = [int(x) for x in file.readline().split('-')]


def passcode_verification(passcode):
    passcode = str(passcode)
    validation_1, validation_2 = False, True
    for x, y in enumerate(passcode):
        if x + 1 == len(passcode):
            break
        if y == passcode[x + 1]:
            validation_1 = True
        if passcode[x + 1] < y:
            validation_2 = False
    if validation_1 and validation_2 is True:
        return True
    else:
        return False


passcode_success = []

for i in range(start, stop + 1):
    if passcode_verification(i) is True:
        passcode_success.append(i)

print(len(passcode_success))




