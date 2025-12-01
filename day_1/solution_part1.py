def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_1/input.txt'
data = read_input(input_file)

start_value = 50
password = 0

for line in data:
    if line[0] == "R":
        start_value = (start_value + int(line[1:])) % 100
    elif line[0] == "L":
        start_value = (100 + (start_value - int(line[1:]))) % 100
    
    if start_value == 0:
        password += 1

print(password)
