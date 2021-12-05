from collections import defaultdict


def part_one():
    with open('input.txt') as f:
        lines = f.readlines()

    counts = defaultdict(int)

    for line in lines:
        tokens = line.split()
        start, end = tokens[0].split(sep=','), tokens[2].split(sep=',')
        start, end = (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))

        if start[0] == end[0]:
            for y in range(min(start[1], end[1]), max(start[1] + 1, end[1] + 1)):
                counts[(start[0], y)] += 1

        if start[1] == end[1]:
            for x in range(min(start[0], end[0]), max(start[0] + 1, end[0] + 1)):
                counts[(x, start[1])] += 1

    print(f'Number of points with 2 or more overlaps: {sum(counts[key] >= 2 for key in counts)}')


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()

    counts = defaultdict(int)

    for line in lines:
        tokens = line.split()
        start, end = tokens[0].split(sep=','), tokens[2].split(sep=',')
        start, end = (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))

        if start[0] == end[0]:
            for y in range(min(start[1], end[1]), max(start[1] + 1, end[1] + 1)):
                counts[(start[0], y)] += 1

        elif start[1] == end[1]:
            for x in range(min(start[0], end[0]), max(start[0] + 1, end[0] + 1)):
                counts[(x, start[1])] += 1

        else:
            counts[start] += 1
            
            while start != end:
                if start[0] < end[0]: start = (start[0] + 1, start[1])
                else: start = (start[0] - 1, start[1])

                if start[1] < end[1]: start = (start[0], start[1] + 1)
                else: start = (start[0], start[1] - 1)

                counts[start] += 1
        
    print(f'Number of points with 2 or more overlaps: {sum(counts[key] >= 2 for key in counts)}')


if __name__ == '__main__':
    part_one()
    part_two()
