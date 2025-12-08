def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_6/input.txt'
data = read_input(input_file)

ops_list = []
for line in data:
    nums = line.split()
    while len(ops_list) < len(nums):
        ops_list.append([])
    for i, num in enumerate(nums):
        ops_list[i].append(num)

ans = 0

for op in ops_list:
    operation = op[-1]
    numbers = op[:-1]
    
    max_len = max(len(num) for num in numbers)
    digits = []
    
    for j in range(max_len):
        group = []
        if operation == "*":
            for num in numbers:
                ptr = len(num) - 1 - j
                if ptr >= 0:
                    group.append(num[ptr])
        else:
            for num in numbers:
                if j < len(num):
                    group.append(num[j])
        if group:
            digits.append(int("".join(group)))

    if operation == "*":
        res = 1
        for num in digits:
            res *= num
    else:
        res = sum(digits)
    ans += res

print(ans)