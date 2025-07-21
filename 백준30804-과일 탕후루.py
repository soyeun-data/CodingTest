from collections import defaultdict

n = int(input())
fruit_list = list(map(int, input().split()))

fruit_dict = defaultdict(int)
max_fruit = 0
left = 0

for right in range(n):
    fruit_dict[fruit_list[right]] += 1

    while len(fruit_dict) > 2:
        fruit_dict[fruit_list[left]] -= 1
        if fruit_dict[fruit_list[left]] == 0:
            del fruit_dict[fruit_list[left]]
        left += 1
    max_fruit = max(max_fruit, right-left+1)


print(max_fruit)