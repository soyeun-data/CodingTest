# 덩치 등수 = 자신보다 더 "큰 덩치"의 사람수
# weight_height에서 하나씩 빼내서 각각 값을 비교

n = int(input())

weight_height = [list(map(int, input().split())) for _ in range(n)]
result = [1]*n

for i in range(n):
    for j in range(n):
        if (weight_height[i][0] < weight_height[j][0]) and (weight_height[i][1] < weight_height[j][1]):
            result[i] += 1

print(*result)