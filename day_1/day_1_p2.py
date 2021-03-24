from pprint import pprint as pp

with open('input.txt', 'rt') as f:
    inputs = [int(i.strip()) for i in f.readlines()]


def calc_fuel(mass, fuel_sum):
    fuel_required = (mass // 3) - 2
    if fuel_required > 0:
        return calc_fuel(fuel_required, fuel_sum + fuel_required)
    else:
        return fuel_sum


total = 0
for i in inputs:
    total += calc_fuel(i, 0)

pp(total)
