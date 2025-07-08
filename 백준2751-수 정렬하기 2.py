import sys

n = int(input())
num_list = [int(sys.stdin.readline()) for _ in range(n)]
num_list = sorted(num_list)

for num in num_list:
    print(num)
