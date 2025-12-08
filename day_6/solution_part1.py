def read_input(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

input_file = 'day_6/input.txt'
data = read_input(input_file)

ops_list = []
for line in data:
    nums = list(map(str, line.split()))
    while len(ops_list) != len(nums):
        ops_list.append([])
    for i in range(len(nums)):
        ops_list[i].append(nums[i])

ans = 0
for op in ops_list:
    res = 0
    if op[-1] == "*":
        res = 1
    for i in range(len(op) - 1):
        if op[-1] == "*":
            res *= int(op[i])
        elif op[-1] == "+":
            res += int(op[i])
    ans += res

print(ans)