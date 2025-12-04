def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_4/input.txt'
data = read_input(input_file)

matrix = [list(line) for line in data]

result = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] != '@':
            continue

        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[nr]) and matrix[nr][nc] == '@':
                count += 1
        
        if count < 4:
            result += 1

print(result)
            