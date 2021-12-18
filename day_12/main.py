from collections import defaultdict


def part_one():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    # Construct adjacency lists
    adj = defaultdict(set)
    for line in lines:
        first, second = line.split(sep='-')
        adj[first].add(second)
        adj[second].add(first)

    stack = [('start', {'start'})]
    answer = 0

    # DFS from start
    while stack:
        start, visited = stack.pop()
        if start == 'end': answer += 1

        for a in adj[start]:
            if a.islower() and a in visited: continue
            stack.append((a, visited.copy() | {a}))

    print(f'Possible paths: {answer}')


def part_two():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    # Construct adjacency lists
    adj = defaultdict(set)
    for line in lines:
        first, second = line.split(sep='-')
        adj[first].add(second)
        adj[second].add(first)

    stack = [('start', {'start'}, False)]
    answer = 0

    # DFS from start
    while stack:
        start, visited, lock = stack.pop()
        if start == 'end':
            answer += 1
            continue

        for a in adj[start]:
            if a == 'start': continue
            if a.islower() and a in visited and lock: continue
            if a.islower() and a in visited and not lock:
                stack.append((a, visited.copy() | {a}, True))
                continue
            stack.append((a, visited.copy() | {a}, lock))

    print(f'Possible paths: {answer}')


if __name__ == '__main__':
    part_one()
    part_two()
