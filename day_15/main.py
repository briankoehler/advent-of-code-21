
def part_one():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    # Convert risks to 2d list of ints
    risks = [[int(r) for r in line] for line in lines]
    rows, cols = len(risks), len(risks[0])

    # Utilize bottom-up DP approach (start->end path = end->start path)
    # Initialize stack to 2 points adjacent to end point and set base case of costs (end point cost)
    stack = [(rows - 2, cols - 1), (rows - 1, cols - 2)]
    costs = {(rows - 1, cols - 1): risks[-1][-1]}

    while stack:
        curr = stack.pop()

        # Get all existing adjacent points
        adj = set()
        if curr[0] != rows - 1: adj.add((curr[0] + 1, curr[1]))
        if curr[0] != 0: adj.add((curr[0] - 1, curr[1]))
        if curr[1] != cols - 1: adj.add((curr[0], curr[1] + 1))
        if curr[1] != 0: adj.add((curr[0], curr[1] - 1))

        # Set the cost of current position by taking min adjacent cost and adding current cost
        costs[curr] = costs[min({a for a in adj if a in costs}, key=lambda p: costs[p])] + risks[curr[0]][curr[1]]

        # Push adjacent points with no established cost yet
        stack += {a for a in adj if a not in costs}

        # Push adjacent points that will need to have adjusted costs (better path found)
        for a in adj:
            if a in costs and risks[a[0]][a[1]] + costs[curr] < costs[a]: stack.append(a)

    print(f'Least cost: {costs[(0, 0)] - risks[0][0]}')


def part_two():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    # Convert risks to 2d list of ints
    risks = [[int(r) for r in line] for line in lines]
    rows = len(risks)

    # Get real map (5x larger)
    for r in range(rows):
        og = risks[r].copy()
        for i in range(1, 5):
            risks[r] += [(x + i) % 9 if (x + i) != 9 else 9 for x in og]
    for i in range(1, 5):
        for r in range(rows):
            risks += [[(x + i) % 9 if (x + i) != 9 else 9 for x in risks[r]]]
    rows, cols = len(risks), len(risks[0])

    # Utilize bottom-up DP approach (start->end path = end->start path)
    # Initialize stack to 2 points adjacent to end point and set base case of costs (end point cost)
    stack = [(rows - 2, cols - 1), (rows - 1, cols - 2)]
    costs = {(rows - 1, cols - 1): risks[-1][-1]}

    while stack:
        curr = stack.pop()

        # Get all existing adjacent points
        adj = set()
        if curr[0] != rows - 1: adj.add((curr[0] + 1, curr[1]))
        if curr[0] != 0: adj.add((curr[0] - 1, curr[1]))
        if curr[1] != cols - 1: adj.add((curr[0], curr[1] + 1))
        if curr[1] != 0: adj.add((curr[0], curr[1] - 1))

        # Set the cost of current position by taking min adjacent cost and adding current cost
        costs[curr] = costs[min({a for a in adj if a in costs}, key=lambda p: costs[p])] + risks[curr[0]][curr[1]]

        # Push adjacent points with no established cost yet
        stack += {a for a in adj if a not in costs}

        # Push adjacent points that will need to have adjusted costs (better path found)
        for a in adj:
            if a in costs and risks[a[0]][a[1]] + costs[curr] < costs[a]: stack.append(a)

    print(f'Least cost: {costs[(0, 0)] - risks[0][0]}')


if __name__ == '__main__':
    # part_one()
    part_two()