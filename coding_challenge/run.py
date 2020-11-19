from sys import stdin

if __name__ == "__main__":
	inputs = []
	line1 = stdin.readline()
	num_lines = int(line1)
	for i in range (0, num_lines):
		inputs.append(stdin.readline().strip())
	print(num_lines)
	for _ in inputs:
		print(_)
