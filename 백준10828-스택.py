n = int(input())
num_list = []
result = []

for _ in range(n):
    input_list = list(input().split())
    if input_list[0] == "push":
        num_list.append(int(input_list[1]))
    elif input_list[0] == "pop":
        if len(num_list) == 0:
            result.append(-1)
        else:
            result.append(num_list.pop())
    elif input_list[0] == "size":
        result.append(len(num_list))
    elif input_list[0] == "empty":
        if len(num_list) == 0:
            result.append(1)
        else:
            result.append(0)
    elif input_list[0] == "top":
        if len(num_list) == 0:
            result.append(-1)
        else:
            result.append(num_list[-1])

for res in result:
    print(res)