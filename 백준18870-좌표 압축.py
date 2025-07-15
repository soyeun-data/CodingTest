# set으로 중복 제거한 후 정렬
from collections import defaultdict

n = int(input())
num_list = list(map(int, input().split()))
num_set = sorted(set(num_list))
num_dict = defaultdict(int)

for index, num in enumerate(num_set):
    num_dict[num] = index

result = []

for i in num_list:
    result.append(num_dict[i])

print(*result)