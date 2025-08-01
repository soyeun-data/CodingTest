# 브루트포스로 풀기
# 모든 조합을 찾은 다음에 합이 s일 경우 cnt + 1

from itertools import combinations

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    for comb in combinations(num_list,i):
        if sum(comb) == s:
            cnt += 1

print(cnt)
