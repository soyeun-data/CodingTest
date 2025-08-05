from collections import defaultdict

n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    num_dict = defaultdict(int)

    for num in num_list:
        num_dict[num] += 1

    num_dict = sorted(num_dict.items(), key = lambda x : x[1], reverse = True)
    army_num, cnt = num_dict[0]

    if (cnt/len(num_list) >= 0.5):
        print(army_num)
    else:
        print("SYJKGW")