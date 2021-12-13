import heapq
import math


def part_one():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    risk = 0

    for row, line in enumerate(lines):
        for col, num in enumerate(line):
            num = int(num)
            neighbors = set()
            
            if row != 0: neighbors.add(lines[row - 1][col])
            if row != len(lines) - 1: neighbors.add(lines[row + 1][col])
            if col != 0: neighbors.add(lines[row][col - 1])
            if col != len(line) - 1: neighbors.add(lines[row][col + 1])

            if all(int(n) > num for n in neighbors): risk += num + 1

    print(f'Risk sum: {risk}')


def part_two():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    largest = [0, 0, 0]
    heapq.heapify(largest)

    # DFS to get all points in a basin starting from a point
    def dfs(row, col):
        queued, stack = {(row, col)}, [(row, col)]

        while stack:
            top = stack.pop()
            r, c = top[0], top[1]

            # Check boundaries + flow + not a '9
            if r != 0 and lines[r - 1][c] > lines[r][c] and lines[r - 1][c] != '9':
                stack.append((r - 1, c))
                queued.add((r - 1, c))
            if r != len(lines) - 1 and lines[r + 1][c] > lines[r][c] and lines[r + 1][c] != '9':
                stack.append((r + 1, c))
                queued.add((r + 1, c))
            if c != 0 and lines[r][c - 1] > lines[r][c] and lines[r][c - 1] != '9':
                stack.append((r, c - 1))
                queued.add((r, c - 1))
            if c != len(line) - 1 and lines[r][c + 1] > lines[r][c] and lines[r][c + 1] != '9':
                stack.append((r, c + 1))
                queued.add((r, c + 1))

        heapq.heappushpop(largest, len(queued))

    for row, line in enumerate(lines):
        for col, num in enumerate(line):
            num = int(num)
            neighbors = set()

            if row != 0: neighbors.add(lines[row - 1][col])
            if row != len(lines) - 1: neighbors.add(lines[row + 1][col])
            if col != 0: neighbors.add(lines[row][col - 1])
            if col != len(line) - 1: neighbors.add(lines[row][col + 1])

            if all(int(n) > num for n in neighbors): dfs(row, col)

    print(f'Three largest basins product: {math.prod(largest)}')
    

if __name__ == '__main__':
    part_one()
    part_two()
