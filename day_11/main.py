
def add_neighbors(lines, flashed, stack, row, col):
    if lines[row][col] <= 9:
        return

    flashed.add((row, col))

    if row != 0 and col != 0 and (row - 1, col - 1) not in flashed:
        lines[row - 1][col - 1] += 1
        stack.append((row - 1, col - 1))

    if row != 0 and (row - 1, col) not in flashed:
        lines[row - 1][col] += 1
        stack.append((row - 1, col))

    if row != 0 and col != len(lines[row]) - 1 and (row - 1, col + 1) not in flashed:
        lines[row - 1][col + 1] += 1
        stack.append((row - 1, col + 1))

    if col != 0 and (row, col - 1) not in flashed:
        lines[row][col - 1] += 1
        stack.append((row, col - 1))

    if col != len(lines[row]) - 1 and (row, col + 1) not in flashed:
        lines[row][col + 1] += 1
        stack.append((row, col + 1))

    if row != len(lines) - 1 and col != 0 and (row + 1, col - 1) not in flashed:
        lines[row + 1][col - 1] += 1
        stack.append((row + 1, col - 1))

    if row != len(lines) - 1 and (row + 1, col) not in flashed:
        lines[row + 1][col] += 1
        stack.append((row + 1, col))

    if row != len(lines) - 1 and col != len(lines[row]) - 1 and (row + 1, col + 1) not in flashed:
        lines[row + 1][col + 1] += 1
        stack.append((row + 1, col + 1))

def part_one():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    lines = [[int(e) for e in line] for line in lines]
    flashes = 0

    for _ in range(100):
        stack, flashed = [], set()

        for row in range(len(lines)):
            for col in range(len(lines[row])):
                lines[row][col] += 1
                add_neighbors(lines, flashed, stack, row, col)

        while stack:
            row, col = stack.pop()
            if (row, col) in flashed: continue
            add_neighbors(lines, flashed, stack, row, col)

        flashes += len(flashed)
        for row, col in flashed:
            lines[row][col] = 0

    print(f'Number of flashes: {flashes}')
            

def part_two():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    lines = [[int(e) for e in line] for line in lines]
    step, flashed = 0, set()

    while len(flashed) != len(lines) * len(lines[0]):
        stack, flashed = [], set()

        for row in range(len(lines)):
            for col in range(len(lines[row])):
                lines[row][col] += 1
                add_neighbors(lines, flashed, stack, row, col)

        while stack:
            row, col = stack.pop()
            if (row, col) in flashed: continue
            add_neighbors(lines, flashed, stack, row, col)
        
        step += 1
        for row, col in flashed:
            lines[row][col] = 0

    print(f'Step of all flashes: {step}')


if __name__ == '__main__':
    part_one()
    part_two()
