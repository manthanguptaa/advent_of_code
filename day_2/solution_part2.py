def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def has_repeating_pattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            pattern = s[:i]
            if pattern * (n // i) == s:
                return True
    return False


input_file = 'day_2/input.txt'
data = read_input(input_file)
ranges = data[0].split(',')

ans = 0

for r in ranges:
    start, end = r.split('-')
    for i in range(int(start), int(end) + 1):
        if has_repeating_pattern(str(i)):
            ans += i
print(ans)