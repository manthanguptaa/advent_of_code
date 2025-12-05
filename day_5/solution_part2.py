def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_5/input.txt'
data = read_input(input_file)


ranges = []
nums = []
flag = True
for line in data:
    if line == '':
        flag = False
        continue
    if flag:
        start, end =line.split('-')
        ranges.append((int(start), int(end)))
    elif not flag:
        nums.append(int(line))

ranges.sort()
nums.sort()

merged_ranges = [ranges[0]]

for i in range(1, len(ranges)):
    if merged_ranges[-1][1] >= ranges[i][0]:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], ranges[i][1]))
    else:
        merged_ranges.append(ranges[i])

res = 0
for a, b in merged_ranges:
    res += b - a + 1

print(res)