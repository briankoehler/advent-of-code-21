
def part_one():
    horz_pos, depth = 0, 0

    with open('input.txt') as f:
        for line in f:
            tokens = line.split()
            command, num = tokens[0], int(tokens[1])

            if command == 'forward': horz_pos += num
            if command == 'up': depth -= num
            if command == 'down': depth += num

    print(f'Final product: {horz_pos * depth}')


def part_two():
    horz_pos, depth, aim = 0, 0, 0

    with open('input.txt') as f:
        for line in f:
            tokens = line.split()
            command, num = tokens[0], int(tokens[1])

            if command == 'down': aim += num
            if command == 'up': aim -= num
            if command == 'forward':
                horz_pos += num
                depth += aim * num

    print(f'Final product: {horz_pos * depth}')


if __name__ == '__main__':
    part_one()
    part_two()
