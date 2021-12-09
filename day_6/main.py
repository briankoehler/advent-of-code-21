from collections import defaultdict


def getFishCount(days: int) -> None:
    with open('input.txt') as f:
        fish = f.readline().split(sep=',')

    counts = defaultdict(int)

    for f in fish:
        counts[int(f)] += 1

    for day in range(days):
        new_fish = counts[0]
        for age in range(8):
            counts[age] = counts[age + 1]
        counts[6] += new_fish
        counts[8] = new_fish

    print(f'Number of lanternfish after {days} days: {sum(counts.values())}')


if __name__ == '__main__':
    getFishCount(80)
    getFishCount(256)
