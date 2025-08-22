# 리스트 슬라이싱 -> 시간초과
# 누적합
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0] * (n+1)
sum_list[1] = num_list[0]

for k in range(2, n+1):
    sum_list[k] = sum_list[k-1] + num_list[k-1]

for _ in range(m):
    i, j = map(int,input().split())
    print(sum_list[j] - sum_list[i-1])