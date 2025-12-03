def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_3/input.txt'
data = read_input(input_file)

result = 0

for line in data:
    max_joltage = 0
    for i in range(len(line) - 1):
        first_digit = int(line[i])
        second_digit = max(int(line[j]) for j in range(i + 1, len(line)))
        joltage = first_digit * 10 + second_digit
        max_joltage = max(max_joltage, joltage)
    
    result += max_joltage

print(result)