def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_2/input.txt'
data = read_input(input_file)
ranges = data[0].split(',')

ans = 0

for r in ranges:
    start, end = r.split('-')
    for i in range(int(start), int(end) + 1):
        if len(str(i)) % 2 != 0:
            continue
        elif len(str(i)) % 2 == 0:
            mid_point = len(str(i)) // 2
            if str(i)[:mid_point] == str(i)[mid_point:]:
                ans += i
print(ans)