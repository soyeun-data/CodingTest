# 1. 몸무게와 키가 모두 크면 덩치 큰 것
# 2. 몸무게를 기준으로 정렬을 한 다음 키만 비교
# 3. 몸무게가 같은 경우가 있을 수 있으므로 if 문에 weight_height_list[i][1] < weight_height_list[j][1] 추가 필요

n = int(input())
result = [0]*n
weight_height_list = [[index, weight, height] for index, (weight, height) in enumerate(map(int, input().split()) for _ in range(n))]

weight_height_list = sorted(weight_height_list, key=lambda x:x[1])

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if weight_height_list[i][2] < weight_height_list[j][2] and weight_height_list[i][1] < weight_height_list[j][1]:
            cnt += 1

    result[weight_height_list[i][0]] = cnt + 1
    cnt = 0

print(*result)