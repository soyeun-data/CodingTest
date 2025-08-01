from collections import defaultdict

tc = int(input())

for _ in range(tc):
    n = int(input())
    clo_dict = defaultdict(int)

    for i in range(n):
        clothes, clothes_type = input().split()
        clo_dict[clothes_type] += 1

    comb = 1

    for num in list(clo_dict.values()):
        comb *= (num + 1)
    
    print(comb - 1)