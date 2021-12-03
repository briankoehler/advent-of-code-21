
def part_one():
	with open('input.txt', 'r') as f:
		lines = f.readlines()

	tracker = {}

	for line in lines:
		for index, c in enumerate(line.strip()):
			if index not in tracker:
				tracker[index] = {'0': 0, '1': 0}
			tracker[index][c] += 1

	gamma, epsilon = '', ''

	for i in range(len(lines[0].strip())):
		if tracker[i]['1'] > tracker[i]['0']:
			gamma += '1'
			epsilon += '0'
		else:
			gamma += '0'
			epsilon += '1'

	gamma, epsilon = int(gamma, 2), int(epsilon, 2)

	print(f'Power consumption: {gamma * epsilon}')


def part_two():
	with open('input.txt', 'r') as f:
		lines_ = f.readlines()

	def test(lines, criteria):
		for i in range(len(lines[0])):
			if len(lines) == 1:
				return int(lines[0], 2)

			zeros, ones = 0, 0
			for line in lines:
				if line[i] == '0': zeros += 1
				if line[i] == '1': ones += 1
			
			if criteria == 0:
				if zeros > ones:
					lines = [line for line in lines if line[i] == '0']
				else:
					lines = [line for line in lines if line[i] == '1']
			else:
				if ones < zeros:
					lines = [line for line in lines if line[i] == '1']
				else:
					lines = [line for line in lines if line[i] == '0']

	o_rating = test(lines_, 0)
	co2_rating = test(lines_, 1)

	print(f'Life support rating: {o_rating * co2_rating}')


if __name__ == '__main__':
	part_one()
	part_two()
