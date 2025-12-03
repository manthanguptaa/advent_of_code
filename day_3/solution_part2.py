def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_3/input.txt'
data = read_input(input_file)

result = 0

for line in data:
    max_joltage = 0
    pos = 0
    for j in range(12):
        max_digit, max_pos = -1, -1
        for i in range(pos, len(line) - (12 - j - 1)):
            if int(line[i]) > max_digit:
                max_digit = int(line[i])
                max_pos = i
        max_joltage = max_joltage * 10 + max_digit
        pos = max_pos + 1
    result += max_joltage

print(result)
    
