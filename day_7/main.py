from collections import defaultdict


def part_one():
    with open('input.txt') as f:
        positions = f.readline().split(sep=',')

    positions = [int(p) for p in positions]
    fuel = defaultdict(int)

    smallest, largest = min(positions), max(positions)

    for p in positions:
        for i in range(p - 1, smallest - 1, -1):
            fuel[i] += p - i
        for i in range(p + 1, largest + 1):
            fuel[i] += i - p

    print(f'Fuel to align: {min(fuel.values())}')


def part_two():

    def get_fuel_consumption(start, end):
        difference = abs(end - start)
        return (difference ** 2 + difference) / 2

    with open('input.txt') as f:
        positions = f.readline().split(sep=',')

    positions = [int(p) for p in positions]
    fuel = defaultdict(int)
    
    smallest, largest = min(positions), max(positions)

    for p in positions:
        for i in range(p - 1, smallest - 1, -1):
            fuel[i] += get_fuel_consumption(p, i)
        for i in range(p + 1, largest + 1):
            fuel[i] += get_fuel_consumption(p, i)

    print(f'Fuel to align: {min(fuel.values())}')


if __name__ == '__main__':
    part_one()
    part_two()
